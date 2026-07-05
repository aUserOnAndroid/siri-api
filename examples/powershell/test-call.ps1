# PowerShell: test calling the API endpoints
$base = Read-Host "Base URL (e.g. http://localhost:5000 or https://abcd.ngrok.io)"
$key = Read-Host "API Key"

Write-Host "Calling /say"
Invoke-RestMethod -Uri "$base/say?text=Hello from PowerShell" -Headers @{ 'X-API-Key' = $key }

Write-Host "Creating a note"
Invoke-RestMethod -Uri "$base/note" -Method POST -Headers @{ 'X-API-Key' = $key } -Body (@{ text = "Hello from PowerShell" } | ConvertTo-Json)
