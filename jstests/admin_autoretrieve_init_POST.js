var request = require('request');
var options = {
   'method': 'POST',
   'url': 'https://api.estuary.tech/admin/autoretrieve/init',
   'headers': {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Accept': 'application/json',
      'Authorization': 'Bearer <replaceapikey>'
   },
   form: {
      'addresses': '<string>',
      'pubKey': '<string>'
   }
};
request(options, function (error, response) {
   if (error) throw new Error(error);
   console.log(response.body);
});
