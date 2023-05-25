package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
	"strings"
	"time"
)

const (
	bardURL         = "https://bard.google.com"
	streamGenerate  = "/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate"
	contentType     = "Content-Type"
	contentTypeValue = "application/x-www-form-urlencoded;charset=UTF-8"
	host            = "Host"
	xSameDomain     = "X-Same-Domain"
	referer         = "Referer"
	userAgent       = "User-Agent"
	origin          = "Origin"
	cookie          = "Cookie"
)

type BardAnswer struct {
	Content           string
	ConversationID    string
	ResponseID        string
	FactualityQueries []interface{}
	TextQuery         string
	Choices           []Choice
}

type Choice struct {
	ID      string
	Content string
}

type Bard struct {
	Token          string
	Timeout        time.Duration
	ReqID          int
	ConversationID string
	ResponseID     string
	ChoiceID       string
	Session        *http.Client
	SNlM0e         string
}

func NewBard(token string, timeout time.Duration, proxies map[string]string, session *http.Client) (*Bard, error) {
	b := &Bard{
		Token:   token,
		Timeout: timeout,
		ReqID:   rand.Intn(10000),
		Session: session,
	}

	if b.Token == "" || !strings.HasSuffix(b.Token, ".") {
		return nil, fmt.Errorf("__Secure-1PSID value must end with a single dot. Enter correct __Secure-1PSID value.")
	}

	if b.Session == nil {
		b.Session = &http.Client{Timeout: b.Timeout}
	}

	err := b.getSNlM0e()
	if err != nil {
		return nil, err
	}

	return b, nil
}

func (b *Bard) getSNlM0e() error {
	resp, err := b.Session.Get(bardURL)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("Response code not 200. Response Status is %d", resp.StatusCode)
	}

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return err
	}

	re := regexp.MustCompile(`SNlM0e":"(.*?)"`)
	matches := re.FindStringSubmatch(string(body))
	if len(matches) != 2 {
		return fmt.Errorf("SNlM0e value not found in response. Check __Secure-1PSID value.")
	}

	b.SNlM0e = matches[1]
	return nil
}

func (b *Bard) GetAnswer(inputText string) (BardAnswer, error) {
	params := url.Values{
		"_reqid": {strconv.Itoa(b.ReqID)},
		"rt":     {"c"},
	}

	inputTextStruct := [][]interface{}{
		{inputText},
		nil,
		{b.ConversationID, b.ResponseID, b.ChoiceID},
	}
	data := map[string]interface{}{
		"f.req": json.RawMessage("[null," + json.Marshal(inputTextStruct) + "]"),
		"at":    b.SNlM0e,
	}

	reqURL := bardURL + streamGenerate + "?" + params.Encode()
	reqBody := strings.NewReader(url.Values(data).Encode())

	req, err := http.NewRequest(http.MethodPost, reqURL, reqBody)
	if err != nil {
		return BardAnswer{}, err
	}

	req.Header.Set(contentType, contentTypeValue)
	req.Header.Set(host, "bard.google.com")
	req.Header.Set(xSameDomain, "1")
	req.Header.Set(referer, "https://bard.google.com/")
	req.Header.Set(userAgent, "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")
	req.Header.Set(origin, "https://bard.google.com")
	req.Header.Set(cookie, "__Secure-1PSID="+b.Token)

	resp, err := b.Session.Do(req)
	if err != nil {
		return BardAnswer{}, err
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return BardAnswer{}, err
	}

	var respDict []interface{}
	err = json.Unmarshal(body, &respDict)
	if err != nil {
		return BardAnswer{}, err
	}

	if len(respDict) < 4 || respDict[3] == nil {
		return BardAnswer{}, fmt.Errorf("Response Error: %s", string(body))
	}

	parsedAnswer := respDict[3].([]interface{})
	bardAnswer := BardAnswer{
		Content:        parsedAnswer[0].(string),
		ConversationID: parsedAnswer[1].([]interface{})[0].(string),
		ResponseID:     parsedAnswer[1].([]interface{})[1].(string),
	}

	if parsedAnswer[3] != nil {
		bardAnswer.FactualityQueries = parsedAnswer[3].([]interface{})
	}

	if parsedAnswer[2] != nil {
		bardAnswer.TextQuery = parsedAnswer[2].([]interface{})[0].(string)
	}

	if parsedAnswer[4] != nil {
		choices := parsedAnswer[4].([]interface{})
		bardAnswer.Choices = make([]Choice, len(choices))
		for i, choice := range choices {
			choiceMap := choice.([]interface{})
			bardAnswer.Choices[i] = Choice{
				ID:      choiceMap[0].(string),
				Content: choiceMap[1].(string),
			}
		}
	}

	b.ConversationID = bardAnswer.ConversationID
	b.ResponseID = bardAnswer.ResponseID
	b.ChoiceID = bardAnswer.Choices[0].ID
	b.ReqID += 100000

	return bardAnswer, nil
}

func main() {
	token := os.Getenv("_BARD_API_KEY")
	timeout := 20 * time.Second

	bard, err := NewBard(token, timeout, nil, nil)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	inputText := "Hello, Bard!"
	answer, err := bard.GetAnswer(inputText)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	fmt.Println("Bard Answer:")
	fmt.Println("Content:", answer.Content)
	fmt.Println("Conversation ID:", answer.ConversationID)
	fmt.Println("Response ID:", answer.ResponseID)
	fmt.Println("Factuality Queries:", answer.FactualityQueries)
	fmt.Println("Text Query:", answer.TextQuery)
	fmt.Println("Choices:")
	for _, choice := range answer.Choices {
		fmt.Println("  - ID:", choice.ID)
		fmt.Println("    Content:", choice.Content)
	}
}
