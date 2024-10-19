const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
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

router.put('/', (req, resp)=>{ 

  var aid = req.params.aid;

  var changes_sql = "SELECT * FROM changes WHERE aid = '" + aid + "'";
  connection.query(changes_sql, function (error, changes, fields) { 

    var totalPages = 1;

    var meta = {};
    meta.limit = 1;
    meta.page = 0;
    meta.totalPages = 1;

    var response = {};
    response.meta = meta;
    response.data = changes;
    //response.changes_sql = changes_sql;
    //response.params = req.params;
    //response.error = error;
    
    resp.send(response);    
    
  }).on('error', err => {
    resp.send(err);
  });                           

}); 

module.exports = router;