const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
const common = require('../../libraries/common');
var github_token = store.github_token;

const client = new S3Client({ 
  region: "us-east-1", 
  credentials: {
      accessKeyId: store.aws_access_key,
      secretAccessKey: store.aws_secret_key
  }});

var connection = mysql.createConnection({
  host     : store.api_search_database_host,
  database : store.api_search_database_database,
  user: store.api_search_database_user,
  password: store.api_search_database_password
  });

var jsonParser = bodyParser.json()

router.patch('/', jsonParser, function (req, resp) {
  
  var aid = req.params.aid;

  var organization = 'api-evangelist';

  var body = req.body; 
  var description = body.description;
  var url = 'https://contracts.apievangelist.com/store/' + aid;
  var m = {};
  m.description = description;
  m.homepage = url;

  const options = {
      method: 'PATCH',
      headers: {
          "Accept": "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "Authorization": 'Bearer ' + github_token                
      },
      body: JSON.stringify(m)
    };                    

  var github_url = 'https://api.github.com/repos/' + organization + '/' + aid;    

  fetch(github_url,options)
    .then(function(response) {
        if (!response.ok) {
            //console.log('Error with Status Code: ' + response.status);          
            var status = response.status;  
            var m = {};
            m.status = status;
            m.github_url = github_url;                         
            resp.send(m); 
        }
        response.json().then(function(data) {   

          var m = {};
          m.description = description; 
          m.url = url; 
          resp.send(m);         
  
        });
      })
      .catch(function(err) {
          console.log('Error: ' + err);
          var m = {};
          m.description = description; 
          m.err = err; 
          m.url = url; 
          resp.send(m);                     
  });



}); 

module.exports = router;