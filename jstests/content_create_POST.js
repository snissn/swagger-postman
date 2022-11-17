var request = require('request');
var options = {
   'method': 'POST',
   'url': 'https://api.estuary.tech/content/create?ignore-dupes=',
   'headers': {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   },
   body: JSON.stringify({
      "coluuid": "<string>",
      "dir": "<string>",
      "location": "<string>",
      "name": "<string>",
      "root": "<string>",
      "type": "<integer>"
   })

};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
