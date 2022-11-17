curl --location --request POST 'https://api.estuary.tech/deal/transfer/status' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <replaceapikey>' \
--data-raw '{
  "id": "<integer>",
  "initiator": "<string>",
  "responder": "<string>"
}' --fail --no-progress-meter