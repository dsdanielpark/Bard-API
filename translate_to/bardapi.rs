use reqwest::{blocking::Client, header::HeaderMap, StatusCode};
use serde_json::{json, Value};
use regex::Regex;

pub struct Bard {
    token: String,
    timeout: u64,
    proxies: Option<HeaderMap>,
    reqid: u32,
    conversation_id: String,
    response_id: String,
    choice_id: String,
    session: Client,
    snim0e: String,
}

impl Bard {
    const HEADERS: &str = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36";

    pub fn new(token: Option<String>, timeout: Option<u64>, proxies: Option<HeaderMap>) -> Result<Self, String> {
        let token = token
            .or_else(|| std::env::var("_BARD_API_KEY").ok())
            .ok_or_else(|| "Token not provided".to_string())?;

        let timeout = timeout.unwrap_or(20);

        let reqid: u32 = rand::random();

        let session = Client::new();

        let snim0e = Self::get_snim0e(&session, timeout, &proxies)?;

        Ok(Self {
            token,
            timeout,
            proxies,
            reqid,
            conversation_id: String::new(),
            response_id: String::new(),
            choice_id: String::new(),
            session,
            snim0e,
        })
    }

    fn get_snim0e(client: &Client, timeout: u64, proxies: &Option<HeaderMap>) -> Result<String, String> {
        let response = client
            .get("https://bard.google.com/")
            .timeout(std::time::Duration::from_secs(timeout))
            .header(reqwest::header::USER_AGENT, Self::HEADERS)
            .headers(proxies.clone().unwrap_or_default())
            .send()
            .map_err(|e| format!("Failed to send request: {}", e))?;

        if response.status() != StatusCode::OK {
            return Err(format!("Response code not 200. Response Status is {}", response.status()));
        }

        let response_text = response.text().map_err(|e| format!("Failed to read response body: {}", e))?;

        let re = Regex::new(r"SNlM0e\":\"(.*?)\"").unwrap();
        let snim0e = re
            .captures(&response_text)
            .and_then(|caps| caps.get(1))
            .map(|m| m.as_str().to_owned())
            .ok_or_else(|| "SNlM0e value not found in response. Check __Secure-1PSID value.".to_string())?;

        Ok(snim0e)
    }

    pub fn get_answer(&mut self, input_text: &str) -> Result<Value, String> {
        let reqid = self.reqid;
        self.reqid += 100_000;

        let params = [
            ("_reqid", &reqid.to_string()),
            ("rt", "c"),
        ];

        let input_text_struct = json!([
            [input_text],
            null,
            [self.conversation_id.clone(), self.response_id.clone(), self.choice_id.clone()],
        ]);

        let data = json!({
            "f.req": [null, json!(input_text_struct)],
            "at": &self.snim0e,
        });

        let response = self.session
            .post("https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate")
            .timeout(std::time::Duration::from_secs(self.timeout))
            .header(reqwest::header::USER_AGENT, Self::HEADERS)
            .headers(self.proxies.clone().unwrap_or_default())
            .query(&params)
            .form(&data)
            .send()
            .map_err(|e| format!("Failed to send request: {}", e))?;

        let response_text = response.text().map_err(|e| format!("Failed to read response body: {}", e))?;

        let resp_dict = response_text.lines().nth(3)
            .ok_or_else(|| format!("Failed to parse response: {}", response_text))?;

        let parsed_answer: Value = serde_json::from_str(resp_dict)
            .map_err(|e| format!("Failed to parse response JSON: {}", e))?;

        let parsed_answer = parsed_answer
            .as_array()
            .and_then(|array| array.get(0))
            .and_then(|value| value.as_array())
            .ok_or_else(|| format!("Invalid response format: {}", resp_dict))?;

        if parsed_answer.is_empty() {
            return Ok(json!({"content": format!("Response Error: {}.", response_text)}));
        }

        let parsed_answer = parsed_answer.as_slice().unwrap();

        let bard_answer = json!({
            "content": parsed_answer[0][0],
            "conversation_id": parsed_answer[1][0],
            "response_id": parsed_answer[1][1],
            "factualityQueries": parsed_answer[3],
            "textQuery": parsed_answer[2].get(0).cloned().unwrap_or_default(),
            "choices": parsed_answer[4]
                .as_array()
                .unwrap_or_default()
                .iter()
                .map(|choice| json!({"id": choice[0], "content": choice[1]}))
                .collect::<Vec<Value>>(),
        });

        self.conversation_id = bard_answer["conversation_id"].to_string();
        self.response_id = bard_answer["response_id"].to_string();
        self.choice_id = bard_answer["choices"][0]["id"].to_string();

        Ok(bard_answer)
    }
}
