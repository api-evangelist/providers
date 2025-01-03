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
const common = require('../../libraries/common');
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

router.put('/', jsonParser, async (req, res, next) => {

  try {

    var aid = req.params.aid;
    var organization = req.query.organization;    

    var apis_json = req.body; 
    var apis_yaml = yaml.dump(apis_json)

    var bucket = 'api-evangelist';    
  
    var rules_path = '/laneworks/api-evangelist/rules/operational-rules.yml';
    var ruleset = await bundleAndLoadRuleset(rules_path, { fs, fetch });

    spectral.setRuleset(ruleset);

    return spectral.run(apis_yaml).then(results => {

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
    
          var update_contracts = "UPDATE contracts SET changes = 1,review = " + connection.escape(JSON.stringify(review)) + " WHERE aid = " +  connection.escape(aid);   
          connection.query(update_contracts, function (error, changes, fields) {                   
            var insert_changes = "INSERT INTO contract_changes(contractId,name,description,file) VALUES (" + connection.escape(aid) + ",'APIs.json Review','This was an automated review of the APIs.json contract using relevant ruleset','review.yml')";
            connection.query(insert_changes, function (error, changes, fields) {
              
              var insert_review = "INSERT INTO contract_reviews(contractId,code) VALUES";
              for (let i = 0; i < review.results.length; i++) {  
                insert_review += "(" + connection.escape(aid) + "," + connection.escape(review.results[i].code) + "),";
              }
              insert_review = insert_review.substring(0,insert_review.length-1);
              connection.query(insert_review, function (error, results, fields) {
                res.send(review);    
              }).on('error', err => {
                res.send(err);
              });                                   

            }).on('error', err => {
              res.send(err);
            });  
            // End insert change

          }).on('error', err => {
            res.send(err);
          });  
          // End Update Database     

      },
      (error) => {
        res.send(error);
      }
      );                           
      // End Write Last      
      
    });  
    
  } catch (err) {
    res.send(err);
  } 

}); 

module.exports = router;