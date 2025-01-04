const express = require('express');
const btoa = require('btoa');
const atob = require('atob');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const yaml = require('js-yaml');
const common = require('../../libraries/common');
const store = require('../../store/keys.json');
var serp_api_key = store.serp_api_key;

var jsonParser = bodyParser.json()

router.put('/', (req, resp)=>{ 
  
  var aid = req.params.aid;
  var name = req.body.name;    

  var search = name + ' Documentation';
  var search_encoded = encodeURIComponent(search);

  var search_count = "5";
  var search_offset = "0";

  var search_url = 'https://serpapi.com/search?engine=google&q=' + search_encoded + '&start=' + search_offset + '&num=' + search_count + '&api_key=' + serp_api_key;
  console.log(search_url);

  const options = {
      method: 'get'
  };  

  fetch(search_url,options)
  .then(function(response) {
      if (!response.ok) {
          console.log('Error with Status Code: ' + response.status);
      }
      response.json().then(function(data) {   

        var m = {};
        m.search = search;
        m.data = data;
        m.results = data.organic_results;
        resp.send(m);  

        });
        })
        .catch(function(err) {
            resp.send(err); 
    });  

}); 

module.exports = router;