import axios, { AxiosInstance, AxiosResponse } from 'axios';

class Bard {
  private token: string | null;
  private session: AxiosInstance;
  private conversation_id: string = '';
  private response_id: string = '';
  private choice_id: string = '';
  private SNlM0e: string = '';

  private static HEADERS = {
    'Host': 'bard.google.com',
    'X-Same-Domain': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Origin': 'https://bard.google.com',
    'Referer': 'https://bard.google.com/',
  };

  constructor(token: string | null = null, private timeout: number = 20, private proxies?: { [key: string]: string }) {
    this.token = token || process.env._BARD_API_KEY || null;
    this.session = axios.create({
      headers: Bard.HEADERS,
      timeout: this.timeout * 1000,
      proxy: this.proxies,
      withCredentials: true,
    });
  }

  private async getSNlM0e(): Promise<string> {
    if (!this.token || !this.token.endsWith('.')) {
      throw new Error('__Secure-1PSID value must end with a single dot. Enter correct __Secure-1PSID value.');
    }
    try {
      const resp: AxiosResponse<string> = await this.session.get('https://bard.google.com/');
      if (resp.status !== 200) {
        throw new Error(`Response code not 200. Response Status is ${resp.status}`);
      }
      const snim0eMatch = resp.data.match(/SNlM0e":"(.*?)"/);
      if (!snim0eMatch) {
        throw new Error('SNlM0e value not found in response. Check __Secure-1PSID value.');
      }
      return snim0eMatch[1];
    } catch (error) {
      throw new Error(`Error occurred while fetching SNlM0e value: ${error.message}`);
    }
  }

  public async getAnswer(inputText: string): Promise<object> {
    const params = {
      bl: 'boq_assistant-bard-web-server_20230419.00_p1',
      _reqid: String(Math.floor(Math.random() * 10000)),
      rt: 'c',
    };
    const inputTextStruct = [
      [inputText],
      null,
      [this.conversation_id, this.response_id, this.choice_id],
    ];
    const data = {
      'f.req': JSON.stringify([null, JSON.stringify(inputTextStruct)]),
      at: this.SNlM0e,
    };
    try {
      const resp: AxiosResponse<string> = await this.session.post(
        'https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate',
        null,
        { params, data }
      );
      const respDict = JSON.parse(resp.data.split('\n')[3])[0][2];
      if (!respDict) {
        return { content: `Response Error: ${resp.data}.` };
      }
      const parsedAnswer = JSON.parse(respDict);
      const bardAnswer = {
        content: parsedAnswer[0][0],
        conversation_id: parsedAnswer[1][0],
        response_id: parsedAnswer[1][1],
        factualityQueries: parsedAnswer[3],
        textQuery: parsedAnswer[2][0] || '',
        choices: parsedAnswer[4].map((i: any) => ({ id: i[0], content: i[1] })),
      };
      this.conversation_id = bardAnswer.conversation_id;
      this.response_id = bardAnswer.response_id;
      this.choice_id = bardAnswer.choices[0].id;
      return bardAnswer;
    } catch (error) {
      throw new Error(`Error occurred while fetching Bard answer: ${error.message}`);
    }
  }
}
