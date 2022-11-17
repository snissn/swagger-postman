var request = require('request');
var options = {
   'method': 'DELETE',
   'url': 'https://api.estuary.tech/admin/peering/peers',
   'headers': {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   },
   body: JSON.stringify([
      "<string>",
      "<string>"
   ])

};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
