curl --location --request DELETE 'https://api.estuary.tech/collections/22aff2fd-4265-4bd0-9714-ecd159e759a5/contents' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <replaceapikey>' \
--data-raw '{"By":"content_id","Value":"1"}' --fail --no-progress-meter