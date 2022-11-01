import os
import json

import importlib
import estuary_client


data = {}

configuration = estuary_client.Configuration()
configuration.host = "http://localhost:3004"
configuration.api_key['Authorization'] = os.environ['APIKEY']
configuration.api_key_prefix['Authorization'] = 'Bearer'

api_instance = estuary_client.CollectionsApi(estuary_client.ApiClient(configuration))
body = estuary_client.MainCreateCollectionBody(name="postman test", description="Created using automated postman test") # MainCreateCollectionBody | Collection name and description

api_response = api_instance.collections_post(body)
coluuid = api_response.uuid

#TODO
body = '{}'
cid = "bafkreifvxooyaffa7gy5mhrb46lnpdom34jvf4r42mubf5efbodyvzeujq"
contentid = "contentid"
dealid = "dealid"
empty = ""
addresses = json.dumps(["127.0.0.1"])
testfilename="testfile"
apikey="foo" # todo create api key then get it
name="testname"
pinid = 1 #todo
propcid = 1 #todo
pubkey = ""
chanid = ""
ContentCreateBody = {} # there's a lot in this data structure

miner="f02620"
#todo http://localhost:3004/public/miners/deals/f02620 isn't working

data['addresses'] = addresses
data['all'] = empty
data['begin'] = empty
data['body'] = body
data['chanid'] = chanid
data['cid'] = cid
data['coluuid'] = coluuid
data['cont'] = contentid
data['content'] = contentid
data['contentIDs'] = [contentid]
data['contentid'] = contentid
data['datacid'] = cid
data['deal'] = dealid
data['dealRequest'] =  {"content_id": contentid}
data['dealid'] = dealid
data['dir'] =  empty
data['duration'] = empty
data['expiry'] = empty
data['filename'] = testfilename
data['id'] =  1 # this may be context dependent
data['ignore-dupes'] = empty
data['ignore-failed'] = empty
data['key'] =  apikey
data['lazy-provide'] =  empty
data['limit'] = empty
data['miner'] = miner # auto come from get miners
data['name'] = name
data['offset'] = empty
data['path'] = testfilename
data['peerIds'] = addresses
data['perms'] =  empty
data['pinid'] = pinid
data['propcid'] = propcid
data['pubKey'] = pubkey
data['replication'] = empty
data['req'] = ContentCreateBody
