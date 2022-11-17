var request = require('request');
var options = {
   'method': 'POST',
   'url': 'https://api.estuary.tech/collections/fs/add?coluuid=22aff2fd-4265-4bd0-9714-ecd159e759a5&content=1&path=@testfile',
   'headers': {
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   }
};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
