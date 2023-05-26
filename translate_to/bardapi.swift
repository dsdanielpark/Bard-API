import Foundation

class Bard {
    static let HEADERS: [String: String] = [
        "Host": "bard.google.com",
        "X-Same-Domain": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://bard.google.com",
        "Referer": "https://bard.google.com/"
    ]
    
    let token: String?
    let timeout: TimeInterval
    let proxies: [String: String]?
    let session: URLSession
    
    private var reqid: Int
    private var conversationId: String
    private var responseId: String
    private var choiceId: String
    private var snim0e: String
    
    init(token: String? = nil, timeout: TimeInterval = 20, proxies: [String: String]? = nil, session: URLSession? = nil) {
        self.token = token ?? ProcessInfo.processInfo.environment["_BARD_API_KEY"]
        self.timeout = timeout
        self.proxies = proxies
        self.session = session ?? URLSession.shared
        
        self.reqid = Int.random(in: 0..<10_000)
        self.conversationId = ""
        self.responseId = ""
        self.choiceId = ""
        self.snim0e = ""
    }
    
    private func getSNlM0e(completion: @escaping (Result<String, Error>) -> Void) {
        guard let token = token, token.hasSuffix(".") else {
            completion(.failure(BardError.invalidToken))
            return
        }
        
        guard let url = URL(string: "https://bard.google.com/") else {
            completion(.failure(BardError.invalidURL))
            return
        }
        
        var request = URLRequest(url: url)
        request.timeoutInterval = timeout
        request.allHTTPHeaderFields = Bard.HEADERS
        request.httpMethod = "GET"
        request.setValue(token, forHTTPHeaderField: "__Secure-1PSID")
        
        let task = session.dataTask(with: request) { data, response, error in
            if let error = error {
                completion(.failure(error))
                return
            }
            
            guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
                completion(.failure(BardError.invalidResponse))
                return
            }
            
            guard let data = data,
                  let htmlString = String(data: data, encoding: .utf8),
                  let snim0e = Bard.extractSNlM0e(from: htmlString) else {
                completion(.failure(BardError.snim0eNotFound))
                return
            }
            
            completion(.success(snim0e))
        }
        
        task.resume()
    }
    
    private static func extractSNlM0e(from htmlString: String) -> String? {
        let pattern = #"SNlM0e":"(.*?)""#
        let regex = try! NSRegularExpression(pattern: pattern)
        if let match = regex.firstMatch(in: htmlString, range: NSRange(htmlString.startIndex..., in: htmlString)),
           let range = Range(match.range(at: 1), in: htmlString) {
            return String(htmlString[range])
        }
        return nil
    }
    
    private func generateRequest(inputText: String, completion: @escaping (Result<[String: Any], Error>) -> Void) {
        let params = [
            "bl": "boq_assistant-bard-web-server_20230419.00_p1",
            "_reqid": "\(reqid)",
            "rt": "c"
        ]
        
        let inputTextStruct = [
            [inputText],
            NSNull(),
            [conversationId, responseId, choiceId]
        ]
        
        let data = [
            "f.req": "[null, \(Bard.jsonString(inputTextStruct))]",
            "at": snim0e
        ]
        
        guard let url = URL(string: "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate") else {
            completion(.failure(BardError.invalidURL))
            return
        }
        
        var request = URLRequest(url: url)
        request.timeoutInterval = timeout
        request.allHTTPHeaderFields = Bard.HEADERS
        request.httpMethod = "POST"
        request.httpBody = try! JSONSerialization.data(withJSONObject: data)
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.url = URL(string: url.absoluteString + "?" + params.map { "\($0.key)=\($0.value)" }.joined(separator: "&"))
        
        let task = session.dataTask(with: request) { data, response, error in
            if let error = error {
                completion(.failure(error))
                return
            }
            
            guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
                completion(.failure(BardError.invalidResponse))
                return
            }
            
            guard let data = data,
                  let jsonResponse = try? JSONSerialization.jsonObject(with: data, options: []),
                  let responseArray = jsonResponse as? [Any],
                  let respDict = responseArray[3] as? [String: Any] else {
                completion(.failure(BardError.invalidResponseData))
                return
            }
            
            completion(.success(respDict))
        }
        
        task.resume()
    }
    
    func getAnswer(inputText: String, completion: @escaping (Result<[String: Any], Error>) -> Void) {
        getSNlM0e { [weak self] result in
            switch result {
            case .success(let snim0e):
                self?.snim0e = snim0e
                self?.generateRequest(inputText: inputText, completion: completion)
            case .failure(let error):
                completion(.failure(error))
            }
        }
    }
    
    private static func jsonString(_ object: Any) -> String {
        guard let data = try? JSONSerialization.data(withJSONObject: object) else {
            return ""
        }
        return String(data: data, encoding: .utf8) ?? ""
    }
}

enum BardError: Error {
    case invalidToken
    case invalidURL
    case invalidResponse
    case snim0eNotFound
    case invalidResponseData
}
