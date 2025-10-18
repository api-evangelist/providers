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

  resp.send(name); 

}); 

module.exports = router;