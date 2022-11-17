var request = require('request');
var options = {
   'method': 'POST',
   'url': 'https://api.estuary.tech/collections/',
   'headers': {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   },
   body: JSON.stringify({
      "name": "name",
      "description": "description"
   })

};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
