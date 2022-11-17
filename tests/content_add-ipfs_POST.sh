curl --location --request POST 'https://api.estuary.tech/content/add-ipfs?ignore-dupes=' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer <replaceapikey>' \
--data-raw '{"root":"bafkreifvxooyaffa7gy5mhrb46lnpdom34jvf4r42mubf5efbodyvzeujq","filename":"@testfile","coluuid":"22aff2fd-4265-4bd0-9714-ecd159e759a5"}' --fail --no-progress-meter