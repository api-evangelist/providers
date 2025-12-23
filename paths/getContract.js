const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
const common = require('../../libraries/common');
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

router.get('/', (req, resp)=>{ 

  var aid = req.params.aid;

  var contracts_sql = "SELECT * FROM contracts WHERE aid = '" + aid + "'";
  connection.query(contracts_sql, function (error, contracts, fields) { 

    var totalPages = 1;

    var meta = {};
    meta.limit = 1;
    meta.page = 0;
    meta.totalPages = 1;

    var response = {};
    response.meta = meta;
    response.data = contracts[0];
    //response.contracts_sql = contracts_sql;
    //response.params = req.params;
    //response.error = error;
    
    resp.send(response);    
    
  }).on('error', err => {
    resp.send(err);
  });                           

});

router.put('/', jsonParser, function (req, resp) {
  
  var aid = req.params.aid;
  var organization = req.query.organization;
  var change_name = req.query.name;
  var change_description = req.query.description;

  var apis_json = req.body; 
  
  var bucket = 'api-evangelist';
  
  // pull changes
  var changes_sql = "SELECT * FROM contract_changes WHERE contractId = " + connection.escape(aid);
  connection.query(changes_sql, function (error, changes, fields) {   

    if(changes){   
      var change_count = changes.length + 1;
    }
    else{
      var change_count = 0;
    }

    var key = aid + '/apis.yml';
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
  
            var last = yaml.load(body);

            // Begin Write Latest

            // update s3 current
            var params = {
                Bucket : bucket,
                Key : key,
                Body : yaml.dump(apis_json)
            };

            const put_command = new PutObjectCommand(params);

            client.send(put_command).then(
              (put) => {        
                  
                // Begin Write Last

                // update s3 current
                key = aid + '/' + change_count + "/apis.yml";
                var params = {
                  Bucket : bucket,
                  Key : key,
                  Body : yaml.dump(last)
              };

              const put_command = new PutObjectCommand(params);

              client.send(put_command).then(
                (put) => {                                       

                  // Write Local
                  var path = '/laneworks/api-evangelist/all';
                  shell.cd(path);
                  shell.exec('git clone https://github.com/api-evangelist/' + aid); 
                  path = '/laneworks/api-evangelist/all/' + aid;
                  shell.cd(path);
                  path = '/laneworks/api-evangelist/all/' + aid + '/apis.yml';
                  var save_content = yaml.dump(apis_json); 
                  fs.writeFileSync(path, save_content, (err) => { });                   

                  var modified = apis_json.modified;
                  var modified_split = modified.split("T");
                  modified = modified_split[0];

                  // update database
                  var update_contracts = "UPDATE contracts SET changes = 1,name = " + connection.escape(apis_json.name) + ",description = " + connection.escape(apis_json.description) + ",modified = " + connection.escape(modified) + ",contract = " + connection.escape(JSON.stringify(apis_json)) + " WHERE aid = '" + aid + "'";
                  connection.query(update_contracts, function (error, changes, fields) {                   

                    // insert change    
                    var insert_changes = "INSERT INTO contract_changes(contractId,name,description,file) VALUES (" + connection.escape(aid) + "," + connection.escape(change_name) + "," + connection.escape(change_description) + ",'apis.yml')";
                    connection.query(insert_changes, function (error, changes, fields) {                                                   

                      var response = {};
                      //response.changes = changes;
                      //response.change_count = change_count;
                      //response.data = last;
                      response.apis_json = apis_json;
                      //response.update_contracts = update_contracts;
                      //response.insert_changes = insert_changes;
                      resp.send(response);                       

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

            },
            (error) => {
              resp.send(error);
            }
            );            
            // End Write Latest

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

  }).on('error', err => {
    resp.send(err);
  });   

});  

module.exports = router;