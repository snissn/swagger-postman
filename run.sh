set -eux

export APIKEY=$(cat APIKEY)
#curl -s https://raw.githubusercontent.com/application-research/estuary-clients/main/swagger.json -o swagger.json
cp ../estuary/docs/swagger.json swagger.json




openapi2postmanv2 -s swagger.json -o posty.json -O includeReferenceMap=true
python3 postman.py > newman.json



sed -i  -e 's/api.estuary.tech/localhost:3004/g' newman.json
newman run newman.json
