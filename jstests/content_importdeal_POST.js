var request = require('request');
var options = {
   'method': 'POST',
   'url': 'https://api.estuary.tech/content/importdeal',
   'headers': {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   },
   body: JSON.stringify({
      "coluuid": "22aff2fd-4265-4bd0-9714-ecd159e759a5",
      "name": "testname",
      "dealIDs": []
   })

};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
