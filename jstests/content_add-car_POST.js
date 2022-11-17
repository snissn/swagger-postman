var request = require('request');
var options = {
   'method': 'POST',
   'url': 'https://api.estuary.tech/content/add-car?ignore-dupes=&filename=@testfile',
   'headers': {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   }
};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
