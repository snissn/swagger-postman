curl --location --request POST 'https://api.estuary.tech/collections/22aff2fd-4265-4bd0-9714-ecd159e759a5' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <replaceapikey>' \
--data-raw '[
  "<integer>",
  "<integer>"
]' --fail --no-progress-meter