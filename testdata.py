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
content_id = "1"#todo
dealid = "1" #todo
empty = ""
addresses = "127.0.0.1"
filename="testfile"
apikey="foo" # todo create api key then get it
name="testname"
pinid = 1 #todo
propcid = 1 #todo
pubkey = ""
chanid = ""
ContentCreateBody = {} # there's a lot in this data structure

dealIDs = [] #todo

miner="f02620"
#todo http://localhost:3004/public/miners/deals/f02620 isn't working

dealbodysize = 100
dealbodyreplication = 1
dealbodydurationBlks = 100
dealbodyverified = True

data['#/definitions/main.createCollectionBody'] = json.dumps({"name":"name","description":"description"})
data['#/definitions/main.deleteContentFromCollectionBody'] = json.dumps({"By":"content_id", "Value": str(content_id)})
data['#/definitions/util.ContentAddIpfsBody'] = json.dumps({"root":cid, "filename": filename, "coluuid": coluuid })
data['#/definitions/main.importDealBody'] = json.dumps({"coluuid": coluuid, "name": name, "dealIDs" : dealIDs })
data['#/definitions/main.estimateDealBody'] = json.dumps({ "size": dealbodysize, "replication" : dealbodyreplication, "durationBlks": dealbodydurationBlks, "verified": dealbodyverified })

data['addresses'] = addresses
data['all'] = empty
data['begin'] = empty
data['body'] = body
data['chanid'] = chanid
data['cid'] = cid
data['coluuid'] = coluuid
data['cont'] = content_id
data['content'] = content_id
data['contentIDs'] = [content_id]
data['content_id'] = content_id
data['contentid'] = content_id
data['datacid'] = cid
data['deal'] = dealid
data['dealRequest'] =  {"content_id": content_id}
data['dealid'] = dealid
data['dir'] =  empty
data['duration'] = empty
data['expiry'] = empty
data['filename'] = filename
data['id'] =  1 # this may be context dependent
data['ignore-dupes'] = empty
data['ignore-failed'] = empty
data['key'] =  apikey
data['lazy-provide'] =  empty
data['limit'] = empty
data['miner'] = miner # auto come from get miners
data['name'] = name
data['offset'] = empty
data['path'] = filename
data['peerIds'] = addresses
data['perms'] =  empty
data['pinid'] = pinid
data['propcid'] = propcid
data['pubKey'] = pubkey
data['replication'] = empty
data['req'] = ContentCreateBody
data['origins'] = addresses
data['meta'] = empty
data['key_or_hash'] = empty


data['pin'] = {"cid":cid, "name":name}
