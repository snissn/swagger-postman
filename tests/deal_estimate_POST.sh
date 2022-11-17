curl --location --request POST 'https://api.estuary.tech/deal/estimate' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <replaceapikey>' \
--data-raw '{"size":100,"replication":1,"durationBlks":100,"verified":true}' --fail --no-progress-meter