curl --location --request DELETE 'https://api.estuary.tech/admin/peering/peers' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <replaceapikey>' \
--data-raw '[
  "<string>",
  "<string>"
]' --fail --no-progress-meter