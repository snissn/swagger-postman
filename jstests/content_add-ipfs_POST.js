var request = require('request');
var options = {
   'method': 'POST',
   'url': 'https://api.estuary.tech/content/add-ipfs?ignore-dupes=',
   'headers': {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   },
   body: JSON.stringify({
      "root": "bafkreifvxooyaffa7gy5mhrb46lnpdom34jvf4r42mubf5efbodyvzeujq",
      "filename": "@testfile",
      "coluuid": "22aff2fd-4265-4bd0-9714-ecd159e759a5"
   })

};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
