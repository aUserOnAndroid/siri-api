Quick guide: call the API from Shortcuts and add a Siri phrase

1) Prepare the server
- Start the Flask server on your Windows machine (run.ps1 or run.bat).
- If your iPhone/iPad cannot reach your PC directly, run:
  ngrok http 5000
  and copy the https URL ngrok provides (e.g., https://abcd1234.ngrok.io)

2) Create a Shortcut that uses /say
- Open Shortcuts on iOS/macOS.
- Create a new Shortcut.
- Add an action: URL -> set to: https://YOUR_SERVER/say?text=Hello%20from%20Siri&api_key=YOUR_KEY
  (Prefer using headers: use 'Get Contents of URL' -> Headers -> add X-API-Key : YOUR_KEY)
- Add action: Get Contents of URL -> Method: GET, Headers: X-API-Key -> YOUR_KEY
- Add action: Get Dictionary Value -> Key: spoken
- Add action: Speak Text -> provided input: Dictionary Value

3) Assign to Siri
- In the Shortcut settings, tap Add to Siri and record a voice phrase (e.g., "Run my PC note").
- Now say “Hey Siri, Run my PC note” and the Shortcut will call your server.

4) Example: create a Note on Desktop
- Create URL: https://YOUR_SERVER/note
- Use POST with JSON body: { "text": "Hello from Siri at {current date/time}" }
- Include header X-API-Key: YOUR_KEY
- Use Get Contents of URL -> Method: POST -> Request Body: JSON -> Provide JSON
- Optionally show the result with Show Result action.

Security tips
- Do not commit your real API key to the repo.
- When testing remotely, use ngrok and rotate keys if they leak.
