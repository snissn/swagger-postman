var request = require('request');
var options = {
   'method': 'POST',
   'url': 'https://api.estuary.tech/deals/make/f02620',
   'headers': {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   },
   body: '<string>'

};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
