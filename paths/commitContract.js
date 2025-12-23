const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const btoa = require('btoa');
const atob = require('atob');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const common = require('../../libraries/common');
const store = require('../../store/keys.json');
var github_token = store.github_token;
const shell = require('shelljs');
var fs = require('fs');
var path = require('path');

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

router.put('/', (req, resp)=>{ 
  
  var aid = req.params.aid;

  // BEGIN PULL CONTRACT
  var contracts_sql = "SELECT aid,organization FROM contracts WHERE aid = " + connection.escape(aid);
  connection.query(contracts_sql, function (error, contract, fields) { 

    var aid = contract[0].aid;
    var organization = contract[0].organization;
    var bucket = 'api-evangelist';

    // BEGIN PULL FILE
    var changes_sql = "SELECT DISTINCT file FROM contract_changes WHERE contractId = " + connection.escape(aid) + " AND committed = 0";
    connection.query(changes_sql, function (error, changes, fields) { 

      var file = changes[0].file;    

      // BEGIN PULL FILE FROM S3   

      file = file.replace(aid + "/","");

      var key = aid + '/' + file;      
      const params = {
        Bucket: bucket,
        Key: key, 
      };            
    
      const streamToString = (stream) =>
        new Promise((resolve, reject) => {
          const chunks = [];
          stream.on("data", (chunk) => chunks.push(chunk));
          stream.on("error", reject);
          stream.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
        });  
    
      const command = new GetObjectCommand(params);
    
      client.send(command).then(
        (data) => { 
    
          streamToString(data.Body).then(
            (body) => {   
                          
            const path = '/laneworks/api-evangelist/all/' + aid;
            shell.cd(path);
            shell.exec("git add *");
            shell.exec("git commit -m 'API Evangelist Update'");
            shell.exec("git push");
            shell.cd("/");

            var response = {};
            response.message = "Committed";
            resp.send(response);               
              
            },
            (error) => {
              resp.send(error);
            }
            );      
          },
          (error) => {
            resp.send(error);
          }
        );
      // END PULL FILE FROM S3           
      
    }).on('error', err => {
      resp.send(err);
    }); 
    
    // END PULL FILE

  }).on('error', err => {
    resp.send(err);
  }); 

// END PULL CONTRACT 

}); 

module.exports = router;