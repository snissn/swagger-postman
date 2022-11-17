var request = require('request');
var options = {
   'method': 'GET',
   'url': 'https://api.estuary.tech/deal/status/f02620/:propcid',
   'headers': {
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   }
};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
