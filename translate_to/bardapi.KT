import okhttp3.*
import org.json.JSONArray
import org.json.JSONObject
import kotlin.random.Random

class Bard(
    private val token: String? = null,
    private val timeout: Int = 20,
    private val proxies: Map<String, String>? = null,
    private val client: OkHttpClient = OkHttpClient.Builder().build()
) {
    companion object {
        private const val BARD_URL = "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate"
        private val HEADERS = mapOf(
            "Host" to "bard.google.com",
            "X-Same-Domain" to "1",
            "User-Agent" to "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type" to "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin" to "https://bard.google.com",
            "Referer" to "https://bard.google.com/"
        )
    }

    private var reqId: Int = Random.nextInt(10000)
    private var conversationId: String = ""
    private var responseId: String = ""
    private var choiceId: String = ""
    private val snim0e: String

    init {
        require(token != null && token.endsWith("."))
        snim0e = getSNlM0e()
    }

    private fun getSNlM0e(): String {
        val request = Request.Builder()
            .url("https://bard.google.com/")
            .headers(Headers.of(HEADERS))
            .build()

        client.newCall(request).execute().use { response ->
            require(response.isSuccessful) { "Response code not 200. Response Status is ${response.code()}" }

            val responseBody = response.body()?.string() ?: throw RuntimeException("Response body is null")
            val pattern = "SNlM0e\":\"(.*?)\"".toRegex()
            val matchResult = pattern.find(responseBody)
                ?: throw RuntimeException("SNlM0e value not found in response. Check __Secure-1PSID value.")

            return matchResult.groupValues[1]
        }
    }

    fun getAnswer(inputText: String): Map<String, Any> {
        val inputTextStruct = "[[\"$inputText\"],null,[\"$conversationId\",\"$responseId\",\"$choiceId\"]]"
        val data = mapOf("f.req" to listOf(null, inputTextStruct), "at" to snim0e)

        val requestBody = FormBody.Builder()
            .add("f.req", "[null,\"$inputTextStruct\"]")
            .add("at", snim0e)
            .build()

        val request = Request.Builder()
            .url(BARD_URL)
            .headers(Headers.of(HEADERS))
            .post(requestBody)
            .build()

        client.newCall(request).execute().use { response ->
            require(response.isSuccessful) { "Response code not 200. Response Status is ${response.code()}" }

            val responseBody = response.body()?.string() ?: throw RuntimeException("Response body is null")
            val parsedAnswer = JSONArray(JSONArray(responseBody).getJSONArray(0).getString(2))

            require(parsedAnswer.isNotEmpty()) { "Response Error: $responseBody" }

            val bardAnswer = mutableMapOf<String, Any>()
            bardAnswer["content"] = parsedAnswer.getJSONArray(0).getString(0)
            bardAnswer["conversation_id"] = parsedAnswer.getJSONArray(1).getString(0)
            bardAnswer["response_id"] = parsedAnswer.getJSONArray(1).getString(1)
            bardAnswer["factualityQueries"] = parsedAnswer.getJSONArray(3)

            val textQuery = parsedAnswer.getJSONArray(2).optString(0, "")
            bardAnswer["textQuery"] = textQuery

            val choicesArray = JSONArray()
            val parsedChoices = parsedAnswer.getJSONArray(4)
            for (i in 0 until parsedChoices.length()) {
                val choice = parsedChoices.getJSONArray(i)
                val choiceObject = JSONObject()
                choiceObject.put("id", choice.getString(0))
                choiceObject.put("content", choice.getString(1))
                choicesArray.put(choiceObject)
            }
            bardAnswer["choices"] = choicesArray

            conversationId = bardAnswer["conversation_id"].toString()
            responseId = bardAnswer["response_id"].toString()
            choiceId = bardAnswer.getJSONArray("choices").getJSONObject(0).getString("id")
            reqId += 100000

            return bardAnswer
        }
    }
}
