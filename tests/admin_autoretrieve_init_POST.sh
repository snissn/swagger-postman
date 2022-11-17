curl --location --request POST 'https://api.estuary.tech/admin/autoretrieve/init' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <replaceapikey>' \
--data-urlencode 'addresses=<string>' \
--data-urlencode 'pubKey=<string>' --fail --no-progress-meter