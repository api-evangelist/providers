const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
var github_token = store.github_token;

const today = new Date();
const year = today.getFullYear();
const month = String(today.getMonth() + 1).padStart(2, '0'); // JavaScript months are 0-indexed
const day = String(today.getDate()).padStart(2, '0');
const formattedDate = `${year}-${month}-${day}`;

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

  var body = req.body;   

  var contract_name = body.name;
  var contract_description = body.description;
  var contract_url = body.humanUrl;
  var contract_position = body.position;
  var contract_access = body.access;
          
  var contract = {};
  contract.aid = slugify(contract_name);
  contract.name = contract_name;
  contract.description = contract_description;

  contract.type = "Index";
  contract.position = contract_position;
  contract.access = contract_access;

  contract.image = 'https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg';
  
  contract.tags = [];
  contract.tags.push('API');

  contract.created = formattedDate;
  contract.modified = formattedDate;

  contract.url = 'https://raw.githubusercontent.com/api-search/' + slugify(contract_name) + '/refs/heads/main/apis.yml';
  contract.specificationVersion = '0.19';
  
  contract.apis = [];

  var a = {};
  a.aid = slugify(contract_name) + ':' + slugify(contract_name);
  a.name = contract_name;
  a.description = contract_description;
  a.humanURL = contract_url;
  a.tags = [];
  a.tags.push('API');

  a.properties = [];
  var p = {};
  p.type = 'Documentation';
  p.url = contract_url;
  a.properties.push(p);

  contract.apis.push(a);

  contract.maintainers = [];
  var m = {};
  m.FN = 'Kin Lane';
  m.email = 'info@apievangelist.com';
  contract.maintainers.push(m);

  var check_contract_sql = "SELECT * FROM contracts WHERE aid = " +  connection.escape(slugify(contract_name));
  connection.query(check_contract_sql, function (error, contracts, fields) {                   

    if(contracts.length > 0){
      //Already Exists
      resp.send(contracts);
    }
    else{


      var insert_contract_sql = "INSERT INTO contracts(aid,name,description,contract) VALUES(" +  connection.escape(slugify(contract_name)) + "," +  connection.escape(slugify(contract_name)) + "," + connection.escape(slugify(contract_name)) + "," + connection.escape(JSON.stringify(contract)) + ")";
      connection.query(insert_contract_sql, function (error, contracts, fields) {     

        var github_url = 'https://api.github.com/orgs/' + organization + '/repos';
        
        var r = {};
        r.name = slugify(contract_name);

        const options = {
          method: 'post',
          headers: {
          "Accept": "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "Authorization": 'Bearer ' + github_token                
          },
          body: JSON.stringify(r)
        };                    

        fetch(github_url,options)
          .then(function(response) {
              if (!response.ok) {      
                  var status = response.status;  
                  var m = {};
                  m.status = status;
                  m.github_url = github_url;                         
                  m.repo = r;            
                  resp.send(m); 
              }
              response.json().then(function(data) { 

                var m = {};
                m.data = data;
                m.message = "GO";
                resp.send(m); 

              });
            })
            .catch(function(err) {
                console.log('Error: ' + err);            
                resp.send(err);                     
          });                 

      }).on('error', err => {
        resp.send(err);
      }); 

    }      

  }).on('error', err => {
    resp.send(err);
  });  
        

});

module.exports = router;