const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const router = express.Router({ mergeParams: true })
const store = require('../../store/keys.json');

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
  var body = req.body;   
  
  var organization = req.query.organization;

  var bucket = organization;
  if(organization == 'api-evangelist'){
    bucket = organization;
  }
  else{
    bucket = 'apis-io';
  }  
  
  // pull changes
  var changes_sql = "SELECT * FROM changes WHERE aid = '" + aid + "'";
  connection.query(changes_sql, function (error, changes, fields) {   

    if(changes){   
      var change_count = changes.length + 1;
    }
    else{
      var change_count = 0;
    }

    var key = aid + '.yml';
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
  
            //var last = jsyaml.load(body);

            var response = {};
            response.changes = changes;
            response.change_count = change_count;
            response.last = body;
            resp.send(response);  

            // get s3 last

            // update s3 current

            // update database

            // insert change

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