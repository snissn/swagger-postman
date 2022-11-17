var request = require('request');
var options = {
   'method': 'DELETE',
   'url': 'https://api.estuary.tech/collections/22aff2fd-4265-4bd0-9714-ecd159e759a5',
   'headers': {
      'Accept': '*/*',
      'Authorization': 'Bearer <replaceapikey>'
   }
};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
