'''
curl -X POST "https://graph.facebook.com/v17.0/979232561930143/messages" \
-H "Authorization: Bearer EAAM0599SPNEBQYzS0bYsUx6VMLZB7pG7inzaZA6II7K7ZCgGbBgWYEmvfrt1KZAqZBZCT9MxZCXQHYMnUZBZBSbZAZCZCannmgGsUNIaUsTVcH5zbmIm8VnCKdHA18fnm9vr2drLN9ZBQC2mMlxlSOXPZAGqMXSI1TujMwe4KciDJqcyW5Jy3tF5JZC2fsl1QfYniRZAUNfRZBwZDZD" \
-H "Content-Type: application/json" \
-d '{
  "messaging_product": "whatsapp",
  "to": "212644700110",
  "type": "text",
  "text": {"body": "Hello from test"}
}'



$token = "EAAM0599SPNEBQYzS0bYsUx6VMLZB7pG7inzaZA6II7K7ZCgGbBgWYEmvfrt1KZAqZBZCT9MxZCXQHYMnUZBZBSbZAZCZCannmgGsUNIaUsTVcH5zbmIm8VnCKdHA18fnm9vr2drLN9ZBQC2mMlxlSOXPZAGqMXSI1TujMwe4KciDJqcyW5Jy3tF5JZC2fsl1QfYniRZAUNfRZBwZDZD"
$phoneId = "979232561930143"
$toNumber = "212644700110"
$message = "Hello from test"

$body = @{
    messaging_product = "whatsapp"
    to = $toNumber
    type = "text"
    text = @{ body = $message }
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://graph.facebook.com/v17.0/$phoneId/messages" `
    -Method POST `
    -Headers @{ Authorization = "Bearer $token"; "Content-Type" = "application/json" } `
    -Body $body
'''