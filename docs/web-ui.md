siri-api web UI

The small web UI in examples/web lets you test /say and /note from a browser. For security it requires an API key.

Notes
- The UI is intentionally minimal. Do NOT host this publicly with an API key embedded.
- To use it locally:
  - Open examples/web/index.html in a browser (file://) and provide the server base URL (http://localhost:5000) and API key.
  - Or host the examples/web folder on a static server you control and point the UI to your server URL.
- CORS: the Flask server enables CORS to make local testing easier; the API still enforces the API key.

Security checklist
- Keep the API key private. Do not commit it.
- When testing remotely, use ngrok and a short-lived key.
- Consider firewall rules to limit inbound traffic to your machine.
