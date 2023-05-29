using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace BardNamespace
{
    public class Bard
    {
        private const string BARD_HOST = "bard.google.com";
        private const string BARD_URL = "https://bard.google.com/";
        private const string STREAM_GENERATE_URL = "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate";

        private static readonly Dictionary<string, string> HEADERS = new Dictionary<string, string>()
        {
            { "Host", BARD_HOST },
            { "X-Same-Domain", "1" },
            { "User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36" },
            { "Content-Type", "application/x-www-form-urlencoded;charset=UTF-8" },
            { "Origin", BARD_URL },
            { "Referer", BARD_URL }
        };

        private readonly string token;
        private readonly int timeout;
        private readonly Dictionary<string, string> proxies;
        private int reqId;
        private string conversationId;
        private string responseId;
        private string choiceId;
        private readonly HttpClient client;

        public Bard(string token = null, int timeout = 20, Dictionary<string, string> proxies = null, HttpClient session = null)
        {
            this.token = token ?? Environment.GetEnvironmentVariable("_BARD_API_KEY");
            this.timeout = timeout;
            this.proxies = proxies;
            this.reqId = new Random().Next(1000, 9999);
            this.conversationId = "";
            this.responseId = "";
            this.choiceId = "";
            this.client = session ?? new HttpClient();
            this.client.DefaultRequestHeaders.Clear();
            foreach (var header in HEADERS)
            {
                this.client.DefaultRequestHeaders.Add(header.Key, header.Value);
            }
            this.client.DefaultRequestHeaders.Add("Cookie", $"__Secure-1PSID={this.token}");
            this.SNlM0e = GetSnim0eAsync().GetAwaiter().GetResult();
        }

        private async Task<string> GetSnim0eAsync()
        {
            if (string.IsNullOrEmpty(token) || token[token.Length - 1] != '.')
            {
                throw new Exception("__Secure-1PSID value must end with a single dot. Enter correct __Secure-1PSID value.");
            }

            HttpResponseMessage response = await client.GetAsync(BARD_URL);
            response.EnsureSuccessStatusCode();
            string responseBody = await response.Content.ReadAsStringAsync();
            Match match = Regex.Match(responseBody, @"SNlM0e\":\"(.*?)\"");
            if (!match.Success)
            {
                throw new Exception("SNlM0e value not found in response. Check __Secure-1PSID value.");
            }
            return match.Groups[1].Value;
        }

        public async Task<Dictionary<string, object>> GetAnswer(string inputText)
        {
            var parameters = new Dictionary<string, string>()
            {
                { "_reqid", reqId.ToString() },
                { "rt", "c" }
            };
            var inputTextStruct = new List<object[]>
            {
                new object[]
                {
                    new List<string> { inputText },
                    null,
                    new List<string> { conversationId, responseId, choiceId }
                }
            };
            var data = new Dictionary<string, string>()
            {
                { "f.req", $"[null, {JsonSerializer.Serialize(inputTextStruct)}]" },
                { "at", SNlM0e }
            };
            var response = await client.PostAsync(STREAM_GENERATE_URL + GetQueryString(parameters), new FormUrlEncodedContent(data));
            response.EnsureSuccessStatusCode();
            var responseContent = await response.Content.ReadAsStringAsync();
            var responseArray = JArray.Parse(responseContent);
            var parsedAnswer = (JArray)responseArray[0][2];
            if (parsedAnswer == null)
            {
                return new Dictionary<string, object> { { "content", $"Response Error: {responseContent}." } };
            }

            var choices = new List<Dictionary<string, object>>();
            foreach (var choice in parsedAnswer[4])
            {
                choices.Add(new Dictionary<string, object> { { "id", choice[0] }, { "content", choice[1] } });
            }

            var bardAnswer = new Dictionary<string, object>
            {
                { "content", parsedAnswer[0][0] },
                { "conversation_id", parsedAnswer[1][0] },
                { "response_id", parsedAnswer[1][1] },
                { "factualityQueries", parsedAnswer[3] },
                { "textQuery", parsedAnswer[2][0]?.ToString() ?? "" },
                { "choices", choices }
            };

            conversationId = (string)bardAnswer["conversation_id"];
            responseId = (string)bardAnswer["response_id"];
            choiceId = (string)choices[0]["id"];
            reqId += 100000;

            return bardAnswer;
        }

        private string GetQueryString(Dictionary<string, string> parameters)
        {
            var stringBuilder = new StringBuilder("?");
            foreach (var parameter in parameters)
            {
                stringBuilder.Append($"{Uri.EscapeDataString(parameter.Key)}={Uri.EscapeDataString(parameter.Value)}&");
            }
            return stringBuilder.ToString().TrimEnd('&');
        }
    }
}