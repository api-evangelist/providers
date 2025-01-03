const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
const common = require('../../libraries/common');

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

router.put('/', jsonParser, function (req, resp) {
  
  var aid = req.params.aid;
  var organization = req.query.organization;
  var change_name = req.query.name;
  var change_description = req.query.description;

  var readme = req.body; 
  var markdown = readme.markdown;
  
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

    var key = aid + '/README.md';
    // update s3 current
    var params = {
        Bucket : bucket,
        Key : key,
        Body : markdown
    };

    const put_command = new PutObjectCommand(params);

    client.send(put_command).then(
      (put) => {                                           
    
          // update database
          var update_contracts = "UPDATE contracts SET changes = 1,readme = " + connection.escape(markdown) + " WHERE aid = " + connection.escape(aid);
          connection.query(update_contracts, function (error, changes, fields) {                   

            // insert change    
            var insert_changes = "INSERT INTO contract_changes(contractId,name,description,file) VALUES (" + connection.escape(aid) + "," + connection.escape(change_name) + "," + connection.escape(change_description) + ",'README.md')";
            connection.query(insert_changes, function (error, changes, fields) {                                                   

              var response = {};
              response.readme = readme;
              response.update_contracts = update_contracts;
              response.insert_changes = insert_changes;
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

module.exports = router;