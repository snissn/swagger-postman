

const coluuid = "22aff2fd-4265-4bd0-9714-ecd159e759a5" //todo get this from api

var data = {}
const body = '{}'
const cid = "bafkreifvxooyaffa7gy5mhrb46lnpdom34jvf4r42mubf5efbodyvzeujq"
const content_id = "1"
const dealid = "1" 
const empty = ""
const addresses = "127.0.0.1"
const filename="@testfile"
const apikey="foo" 
const name="testname"
const pinid = 1 
const propcid = 1 
const pubkey = ""
const chanid = ""
const ContentCreateBody = {} 

const dealIDs = [] 

const miner="f02620"

const dealbodysize = 100
const dealbodyreplication = 1
const dealbodydurationBlks = 100
const dealbodyverified = true

data['#/definitions/main.createCollectionBody'] = {"name":"name","description":"description"}
data['#/definitions/main.deleteContentFromCollectionBody'] = {"By":"content_id", "Value": content_id}
data['#/definitions/util.ContentAddIpfsBody'] = {"root":cid, "filename": filename, "coluuid": coluuid }
data['#/definitions/main.importDealBody'] = {"coluuid": coluuid, "name": name, "dealIDs" : dealIDs }
data['#/definitions/main.estimateDealBody'] = { "size": dealbodysize, "replication" : dealbodyreplication, "durationBlks": dealbodydurationBlks, "verified": dealbodyverified }

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
data['id'] =  1 
data['ignore-dupes'] = empty
data['ignore-failed'] = empty
data['key'] =  apikey
data['lazy-provide'] =  empty
data['limit'] = empty
data['miner'] = miner 
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


module.exports = { data };

