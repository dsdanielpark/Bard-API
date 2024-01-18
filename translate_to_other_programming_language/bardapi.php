<?php

class Bard {
    private const HEADERS = array(
        "Host" => "bard.google.com",
        "X-Same-Domain" => "1",
        "User-Agent" => "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Content-Type" => "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin" => "https://bard.google.com",
        "Referer" => "https://bard.google.com/"
    );

    private $token;
    private $proxies;
    private $timeout;
    private $reqid;
    private $conversation_id;
    private $response_id;
    private $choice_id;
    private $session;
    private $SNlM0e;

    public function __construct($token = null, $timeout = 20, $proxies = null, $session = null) {
        $this->token = $token ?: getenv("_BARD_API_KEY");
        $this->proxies = $proxies;
        $this->timeout = $timeout;
        $this->reqid = (int)str_pad(rand(0, 9999), 4, "0", STR_PAD_LEFT);
        $this->conversation_id = "";
        $this->response_id = "";
        $this->choice_id = "";
        $this->session = $session ?: new Requests_Session();
        $this->session->headers = self::HEADERS;
        $this->session->cookies->set("__Secure-1PSID", $this->token);
        $this->SNlM0e = $this->_get_snim0e();
    }

    private function _get_snim0e() {
        if (!$this->token || substr($this->token, -1) !== ".") {
            throw new Exception("__Secure-1PSID value must end with a single dot. Enter correct __Secure-1PSID value.");
        }
        $resp = $this->session->get("https://bard.google.com/", array("timeout" => $this->timeout, "proxies" => $this->proxies));
        if ($resp->status_code !== 200) {
            throw new Exception("Response code not 200. Response Status is " . $resp->status_code);
        }
        preg_match('/SNlM0e":"(.*?)"/', $resp->text, $matches);
        if (!$matches) {
            throw new Exception("SNlM0e value not found in response. Check __Secure-1PSID value.");
        }
        return $matches[1];
    }

    public function get_answer($input_text) {
        $params = array(
            "_reqid" => (string)$this->reqid,
            "rt" => "c"
        );
        $input_text_struct = array(
            array($input_text),
            null,
            array($this->conversation_id, $this->response_id, $this->choice_id)
        );
        $data = array(
            "f.req" => json_encode(array(null, json_encode($input_text_struct))),
            "at" => $this->SNlM0e
        );
        $resp = $this->session->post(
            "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate",
            array("timeout" => $this->timeout, "proxies" => $this->proxies),
            $params,
            $data
        );
        $resp_dict = json_decode(explode("\n", $resp->content)[3], true)[0][2];

        if (!$resp_dict) {
            return array("content" => "Response Error: " . $resp->content);
        }
        $parsed_answer = json_decode($resp_dict, true);
        $choices = array_map(function($item) {
            return array("id" => $item[0], "content" => $item[1]);
        }, $parsed_answer[4]);
        $bard_answer = array(
            "content" => $parsed_answer[0][0],
            "conversation_id" => $parsed_answer[1][0],
            "response_id" => $parsed_answer[1][1],
            "factualityQueries" => $parsed_answer[3],
            "textQuery" => $parsed_answer[2][0] ?: "",
            "choices" => $choices
        );
        $this->conversation_id = $bard_answer["conversation_id"];
        $this->response_id = $bard_answer["response_id"];
        $this->choice_id = $choices[0]["id"];
        $this->reqid += 100000;

        return $bard_answer;
    }
}

?>
