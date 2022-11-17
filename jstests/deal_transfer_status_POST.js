var request = require('request');
var options = {
   'method': 'POST',
   'url': 'https://api.estuary.tech/deal/transfer/status',
   'headers': {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   },
   body: JSON.stringify({
      "id": "<integer>",
      "initiator": "<string>",
      "responder": "<string>"
   })

};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
