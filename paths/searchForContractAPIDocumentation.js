const express = require('express');
const btoa = require('btoa');
const atob = require('atob');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const yaml = require('js-yaml');
const common = require('../../libraries/common');
const store = require('../../store/keys.json');
var github_token = store.github_token;

var jsonParser = bodyParser.json()

router.put('/', (req, resp)=>{ 
  
  var aid = req.params.aid;
  var name = req.body.name;    

  var bing_token = store.bing_token;
  
  var search = name + ' Documentation';
  search = encodeURIComponent(search);

  var search_count = "50";
  var search_offset = "0";

  var search_url = 'https://api.bing.microsoft.com/v7.0/search?q=' + search + '&mkt=en-US&offset=0&count=49&responseFilter=Webpages&freshness=Week&setLang=en&cc=us';
  //console.log(search_url);

  const options = {
      method: 'GET',
      headers: {
          "Accept": "application/json",
          "Ocp-Apim-Subscription-Key": bing_token                 
      }
  };  

  fetch(search_url,options)
  .then(function(response) {
      if (!response.ok) {
           //console.log('Error with Status Code: ' + response.status);
      }
      response.json().then(function(data) {   

        var results = [];
        for (let j = 0; j < data.webPages.value.length; j++) { 
            if(j < 5){
                var displayUrl = data.webPages.value[j].displayUrl;
                var url = new URL(displayUrl);
                var hostName = url.hostname;     
                var api_name = data.webPages.value[j].name;     
                            
                var e = {};
                e.displayUrl = displayUrl;
                e.url = url;
                e.hostName = hostName;
                e.api_name = api_name;    
                results.push(e);          
            }
          }

          var m = {};
          m.search = search;
          m.results = results;
          resp.send(m);  

      });
      })
      .catch(function(err) {
           //console.log('Error: ' + err);
  });

}); 

module.exports = router;