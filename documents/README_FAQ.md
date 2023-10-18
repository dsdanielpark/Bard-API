Development Status :: 5 - Production/Stable

# FAQ

## Troubleshooting Google Account-Related Issues with Bard API

```python
Response Error: b')]}\\'\\n\\n38\\n[[\"wrb.fr\",null,null,null,null,[8]]]\\n54\\n[[\"di\",59],
[\"af.httprm\",59,\"4239016509367430469\",0]]\\n25\\n[[\"e\",4,null,null,129]]\\n'. 
Temporarily unavailable due to traffic or an error in cookie values. Please double-check the cookie values and verify your network environment.
```

The error you're experiencing isn't originating from the package itself; it's related to your Google account and may be due to various factors like your country or region settings, which can prevent you from receiving accurate results from Bard. Therefore, it's beyond the scope of the package to resolve, but please consider checking the following:

1. First, thoroughly read the readme and see if it pertains to cases of temporary abnormal responses from the package. Try again after some time or a few hours: [Before using Bard API](https://github.com/dsdanielpark/Bard-API/blob/main/README.md#before-using-the-bard-api)
2. Bypass proxies: [Behind a proxy](https://github.com/dsdanielpark/Bard-API#behind-a-proxy)
3. Try using an account from a different region or change the language settings of your Google account.
4. Restart your browser to refresh the cookie values and use the new __Secure-1PSID.
5. Try passing three or more cookies using [Multi-cookie Bard](https://github.com/dsdanielpark/Bard-API/blob/main/documents/README_DEV.md#multi-cookie-bard). If that doesn't work, consider passing almost all cookie values.

Please let me know if you need further assistance.



## Before using the Bard API
- Google Bard can return different responses based on various factors such as account, country, region, IP, etc., following Google's policies. This means that even well-functioning methods, especially the `ask_about_image` method, can encounter Response Errors, which are caused by various reasons related to Google's policies, not package errors. It cannot be resolved at the package level. (e.g., CAPTCHA or HTTP 429 error)
- The API token(__Secure-1PSID cookie value) for this service is unofficial. Additionally, exposing it can allow others to easily use the Bard service with your Google ID, so never expose it.
- This service has very limited and variable call limits per unit of time, and exceeding rate limiting temporarily prevents obtaining normal response results.
- Sending the same question multiple times in requests can also temporarily prevent obtaining normal response results.
- Some regions may require additional cookie values besides __Secure-1PSID; refer to the issue page.
- The __Secure-1PSID cookie value may change frequently. Logout, restart your web browser, and enter the new __Secure-1PSID cookie value.
- Using this package for real-world applications is highly inappropriate. Due to rate limiting and variable API policies, it will only function temporarily.
- If the time interval between requests is very short, the Google API process may interpret it as performing a large number of requests and may not return normal responses.
- All these policies are subject to change, and the interface is also variable.


<br>
