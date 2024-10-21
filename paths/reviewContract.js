const spectralCore = require('@stoplight/spectral-core')
const { Spectral, Document } = spectralCore
const Parsers = require('@stoplight/spectral-parsers')
const { truthy, pattern, xor } = require('@stoplight/spectral-functions')
const {
  bundleAndLoadRuleset
} = require('@stoplight/spectral-ruleset-bundler/with-loader')
const spectralRuntime = require('@stoplight/spectral-runtime')
const { fetch } = spectralRuntime
const fs = require('fs');
const path = require('path');
const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
var github_token = store.github_token;

const spectral = new Spectral();

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

router.put('/', jsonParser, async (req, res,next) => {

  try {

    var aid = req.params.aid;
    var organization = req.query.organization;    

    var apis_json = req.body; 

    var bucket = organization;
    if(organization == 'api-evangelist'){
      bucket = organization;
    }
    else{
      bucket = 'apis-io';
    }     
  
    var rules_path = '/laneworks/api-evangelist/rules/operational-rules.yml';
    var ruleset = await bundleAndLoadRuleset(rules_path, { fs, fetch });
    res.send(ruleset);
    spectral.setRuleset(ruleset);

    spectral.run(apis_json).then(results => {

      const event = new Date();
      
      var review = {};
      review.executed = event.toISOString();
      review.results = results;
      
      // update s3 current
      key = aid + '/review.yml';
      var params = {
        Bucket : bucket,
        Key : key,
        Body : yaml.dump(review)
      };

      const put_command = new PutObjectCommand(params);

      client.send(put_command).then(
        (put) => {                           

          // update database
          var update_contracts = "UPDATE contracts SET changes = 1,review = " + connection.escape(JSON.stringify(review)) + " WHERE aid = '" + aid + "'";
          connection.query(update_contracts, function (error, changes, fields) {                   
            // insert change    
            var insert_changes = "INSERT INTO changes(aid,name,description,file) VALUES (" + connection.escape(aid) + ",'APIs.json Review','This was an automated review of the APIs.json contract using relevant ruleset','review.yml')";
            connection.query(insert_changes, function (error, changes, fields) {                                                   
              resp.send(review);                       
            }).on('error', err => {
              resp.send(err);
            });  
            // End insert change

          }).on('error', err => {
            resp.send(err);
          });  
          // End Update Database     

      },
      (error) => {
        resp.send(error);
      }
      );                           
      // End Write Last      
      
    });  
    
  } catch (err) {
    next(err);
  } 

}); 

module.exports = router;