curl --location --request POST 'https://api.estuary.tech/content/create?ignore-dupes=' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <replaceapikey>' \
--data-raw '{
  "coluuid": "<string>",
  "dir": "<string>",
  "location": "<string>",
  "name": "<string>",
  "root": "<string>",
  "type": "<integer>"
}' --fail --no-progress-meter