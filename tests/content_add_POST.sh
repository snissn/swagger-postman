curl --location --request POST 'https://api.estuary.tech/content/add?coluuid=22aff2fd-4265-4bd0-9714-ecd159e759a5&replication=&ignore-dupes=&lazy-provide=&dir=' \
--header 'Content-Type: multipart/form-data' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <replaceapikey>' \
--form 'data=@"/path/to/file"' \
--form 'filename="<string>"' --fail --no-progress-meter