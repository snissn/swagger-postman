var request = require('request');
var options = {
   'method': 'DELETE',
   'url': 'https://api.estuary.tech/user/api-keys/foo',
   'headers': {
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   }
};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
