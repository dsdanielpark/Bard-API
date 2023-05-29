const os = require('os');
const randomstring = require('randomstring');
const axios = require('axios');

class Bard {
  HEADERS = {
    Host: 'bard.google.com',
    'X-Same-Domain': '1',
    'User-Agent':
      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    Origin: 'https://bard.google.com',
    Referer: 'https://bard.google.com/',
  };

  constructor(token = null, timeout = 20, proxies = null, session = null) {
    this.token = token || process.env._BARD_API_KEY;
    this.proxies = proxies;
    this.timeout = timeout;
    this._reqid = parseInt(randomstring.generate({ length: 4, charset: 'numeric' }));
    this.conversation_id = '';
    this.response_id = '';
    this.choice_id = '';
    this.session = session || axios.create({
      headers: this.HEADERS,
      withCredentials: true,
      timeout: this.timeout * 1000,
      proxy: this.proxies,
    });
    this.SNlM0e = null;
  }

  async _get_snim0e() {
    if (!this.token || this.token[this.token.length - 1] !== '.') {
      throw new Error('__Secure-1PSID value must end with a single dot. Enter correct __Secure-1PSID value.');
    }
    const resp = await this.session.get('https://bard.google.com/');
    if (resp.status !== 200) {
      throw new Error(`Response code not 200. Response Status is ${resp.status}`);
    }
    const snim0eMatch = resp.data.match(/SNlM0e":"(.*?)"/);
    if (!snim0eMatch) {
      throw new Error('SNlM0e value not found in response. Check __Secure-1PSID value.');
    }
    this.SNlM0e = snim0eMatch[1];
  }

  async get_answer(input_text) {
    if (!this.SNlM0e) {
      await this._get_snim0e();
    }

    const params = {
      bl: 'boq_assistant-bard-web-server_20230419.00_p1',
      _reqid: this._reqid.toString(),
      rt: 'c',
    };
    const input_text_struct = [
      [input_text],
      null,
      [this.conversation_id, this.response_id, this.choice_id],
    ];
    const data = {
      'f.req': JSON.stringify([null, JSON.stringify(input_text_struct)]),
      at: this.SNlM0e,
    };
    const resp = await this.session.post(
      'https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate',
      { params, data }
    );
    const [, , resp_dict] = JSON.parse(resp.data.split('\n')[3]);

    if (!resp_dict) {
      return { content: `Response Error: ${resp.data}` };
    }
    const parsed_answer = JSON.parse(resp_dict);
    const bard_answer = {
      content: parsed_answer[0][0],
      conversation_id: parsed_answer[1][0],
      response_id: parsed_answer[1][1],
      factualityQueries: parsed_answer[3],
      textQuery: parsed_answer[2][0] || '',
      choices: parsed_answer[4].map(([id, content]) => ({ id, content })),
    };
    this.conversation_id = bard_answer.conversation_id;
    this.response_id = bard_answer.response_id;
    this.choice_id = bard_answer.choices[0].id;
    this._reqid += 100000;

    return bard_answer;
  }
}

module.exports = Bard;
