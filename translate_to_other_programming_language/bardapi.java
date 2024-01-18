import okhttp3.*;
import org.json.*;

import java.io.IOException;
import java.util.*;

public class Bard {
    private String token;
    private int timeout;
    private Map<String, String> proxies;
    private int reqId;
    private String conversationId;
    private String responseId;
    private String choiceId;
    private OkHttpClient client;
    private String snim0e;

    public Bard(String token, int timeout, Map<String, String> proxies) {
        this.token = token;
        this.timeout = timeout;
        this.proxies = proxies;
        this.reqId = new Random().nextInt(10000);
        this.conversationId = "";
        this.responseId = "";
        this.choiceId = "";
        this.client = new OkHttpClient.Builder().cookieJar(new CookieJar() {
            @Override
            public void saveFromResponse(HttpUrl httpUrl, List<Cookie> list) {
            }

            @Override
            public List<Cookie> loadForRequest(HttpUrl httpUrl) {
                if (token != null) {
                    return Collections.singletonList(new Cookie.Builder().name("__Secure-1PSID").value(token).build());
                }
                return Collections.emptyList();
            }
        }).build();
        this.snim0e = getSNlM0e();
    }

    private String getSNlM0e() {
        if (this.token == null || !this.token.endsWith(".")) {
            throw new IllegalArgumentException("__Secure-1PSID value must end with a single dot. Enter correct __Secure-1PSID value.");
        }

        Request request = new Request.Builder()
                .url("https://bard.google.com/")
                .build();

        try (Response response = client.newCall(request).execute()) {
            if (!response.isSuccessful()) {
                throw new IOException("Response code not 200. Response Status is " + response.code());
            }

            String responseBody = response.body().string();
            Matcher matcher = Pattern.compile("SNlM0e\":\"(.*?)\"").matcher(responseBody);
            if (!matcher.find()) {
                throw new RuntimeException("SNlM0e value not found in response. Check __Secure-1PSID value.");
            }

            return matcher.group(1);
        } catch (IOException e) {
            throw new RuntimeException("Error occurred while fetching SNlM0e value: " + e.getMessage());
        }
    }

    public JSONObject getAnswer(String inputText) {
        try {
            String inputTextStruct = "[[\"" + inputText + "\"],null,[\"" + conversationId + "\",\"" + responseId + "\",\"" + choiceId + "\"]]";

            JSONObject data = new JSONObject()
                    .put("f.req", new JSONArray().put(null).put(inputTextStruct))
                    .put("at", snim0e);

            RequestBody requestBody = RequestBody.create(data.toString(), MediaType.parse("application/json; charset=utf-8"));

            Request request = new Request.Builder()
                    .url("https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate")
                    .post(requestBody)
                    .build();

            try (Response response = client.newCall(request).execute()) {
                if (!response.isSuccessful()) {
                    throw new IOException("Response code not 200. Response Status is " + response.code());
                }

                String responseBody = response.body().string();
                JSONArray parsedAnswer = new JSONArray(new JSONArray(responseBody).getJSONArray(0).getString(2));

                if (parsedAnswer.isEmpty()) {
                    return new JSONObject().put("content", "Response Error: " + responseBody);
                }

                JSONObject bardAnswer = new JSONObject();
                bardAnswer.put("content", parsedAnswer.getJSONArray(0).getString(0));
                bardAnswer.put("conversation_id", parsedAnswer.getJSONArray(1).getString(0));
                bardAnswer.put("response_id", parsedAnswer.getJSONArray(1).getString(1));
                bardAnswer.put("factualityQueries", parsedAnswer.getJSONArray(3));
                bardAnswer.put("textQuery", parsedAnswer.getJSONArray(2).optString(0, ""));

                JSONArray choicesArray = new JSONArray();
                JSONArray parsedChoices = parsedAnswer.getJSONArray(4);
                for (int i = 0; i < parsedChoices.length(); i++) {
                    JSONArray choice = parsedChoices.getJSONArray(i);
                    JSONObject choiceObject = new JSONObject();
                    choiceObject.put("id", choice.getString(0));
                    choiceObject.put("content", choice.getString(1));
                    choicesArray.put(choiceObject);
                }
                bardAnswer.put("choices", choicesArray);

                this.conversationId = bardAnswer.getString("conversation_id");
                this.responseId = bardAnswer.getString("response_id");
                this.choiceId = bardAnswer.getJSONArray("choices").getJSONObject(0).getString("id");
                this.reqId += 100000;

                return bardAnswer;
            }
        } catch (IOException e) {
            throw new RuntimeException("Error occurred while fetching Bard answer: " + e.getMessage());
        }
    }
}
