const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
var github_token = store.github_token;

function slugify(str) {
  return String(str)
      .normalize('NFKD') // split accented characters into their base characters and diacritical marks
      .replace(/[\u0300-\u036f]/g, '') // remove all the accents, which happen to be all in the \u03xx UNICODE block.
      .trim() // trim leading or trailing whitespace
      .toLowerCase() // convert to lowercase
      .replace(/[^a-z0-9 -]/g, '-') // remove non-alphanumeric characters
      .replace(/\s+/g, '-') // replace spaces with hyphens
      .replace(/-+/g, '-'); // remove consecutive hyphens
  } 

var jsonParser = bodyParser.json();  

var connection = mysql.createConnection({
  host     : store.api_search_database_host,
  database : store.api_search_database_database,
  user: store.api_search_database_user,
  password: store.api_search_database_password
  });

  const client = new S3Client({ 
    region: "us-east-1", 
    credentials: {
        accessKeyId: store.aws_access_key,
        secretAccessKey: store.aws_secret_key
    }}); 

router.get('/', (req, resp)=>{ 

  var organization = req.query.organization;
  var search = req.query.search;
  
  var limit = req.query.limit;
  if(limit){
    if(limit == ''){
      limit = 25;
    }
  }
  else{
    limit = 25;
  }

  var page = req.query.page;
  if(page){
    if(page == ''){
      page = 0;
    }
  }
  else{
    page = 0;
  }

  var count_sql = "SELECT count(name) as contractCount FROM contracts WHERE name IS NOT NULL";
  if(search){
    count_sql += " AND (name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' OR tags LIKE '%" + search + "%')";
  }
  connection.query(count_sql, function (error, total, fields) { 

    var contracts_sql = "SELECT * FROM contracts WHERE name IS NOT NULL";
    if(search){
      contracts_sql += " AND (name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' OR tags LIKE '%" + search + "%')";
    }    
    contracts_sql += " LIMIT " + page + "," + limit;
    //contracts_sql += " LIMIT 0,25";

    connection.query(contracts_sql, function (error, contracts, fields) { 

      var totalRecords = total[0].contractCount;
      var totalPages = Math.round(totalRecords/limit);

      var meta = {};
      if(search){
        meta.search = search;
      }
      meta.limit = limit;
      meta.page = page;
      meta.totalPages = totalPages;
      meta.count_sql = count_sql;
      meta.contracts_sql = contracts_sql;

      var response = {};
      response.meta = meta;
      response.data = contracts;
      
      resp.send(response);    
      
    }).on('error', err => {
      resp.send(err);
    });         
  }).on('error', err => {
    resp.send(err);
  });                   

});

router.post('/', jsonParser, (req, resp)=>{ 

  var organization = req.query.organization;
  var bucket = organization;
  if(organization == 'api-evangelist'){
    bucket = organization;
  }
  else{
    bucket = 'apis-io';
  }    

  var contract = req.body;   

  var contract_name = contract.name;
  var contract_description = contract.description;
                                         
  var check_contract_sql = "SELECT * FROM contracts WHERE aid = " +  connection.escape(slugify(contract_name));
  connection.query(check_contract_sql, function (error, contracts, fields) {                   

    if(contracts.length > 0){
      resp.send(contracts);
    }
    else{
      resp.send("NONE!");
    }      

  }).on('error', err => {
    resp.send(err);
  });  
        

});

module.exports = router;