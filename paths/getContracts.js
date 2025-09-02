const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
var github_token = store.github_token;
const common = require('../../libraries/common');

const today = new Date();
const year = today.getFullYear();
const month = String(today.getMonth() + 1).padStart(2, '0'); // JavaScript months are 0-indexed
const day = String(today.getDate()).padStart(2, '0');
const formattedDate = `${year}-${month}-${day}`;    

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

  var organization = 'api-evangelist';
  var search = req.query.search;
  var searchFields = req.query.searchFields;
  var noTags = req.query.noTags;
  var latest = req.query.latest;
  
  var limit = req.query.limit;
  if(limit){
    if(limit == ''){
      limit = 5000;
    }
  }
  else{
    limit = 5000;
  }

  if(req.query.page){
    page = req.query.page;
    page = page - 0;
  }
  else{
    page = 0;
  }

  var type = req.query.type;  
  var position = req.query.position;  
  var access = req.query.access;  

  var count_sql = "SELECT count(name) as contractCount FROM contracts WHERE name IS NOT NULL";
  if(search){
    count_sql += " AND (";  
    var first = 0;    
    if(searchFields.includes("name")){
      count_sql += "name LIKE '%" + search + "%'";
      first = 1;
    }
    if(searchFields.includes("description")){
      if(first == 1){ count_sql += " OR "; }
      count_sql += "description LIKE '%" + search + "%'";
    }
    if(searchFields.includes("tags")){
      if(first == 1){ count_sql += " OR "; }
      count_sql += "tags LIKE '%" + search + "%'";
    } 
    count_sql += ")";           
  } 
  if(type && type.length > 1){
    count_sql += " AND type = '" + type + "'";
  }  
  if(position && position.length > 1){
    count_sql += " AND position = '" + position + "'";
  } 
  if(access && access.length > 1){
    count_sql += " AND access = '" + access + "'";
  }   
  if(noTags && noTags == 1){
    count_sql += " AND (tags is null or tags = 'API' or tags = '' or tags = 'Tag')";
  }      
  connection.query(count_sql, function (error, total, fields) { 

    var contracts_sql = "SELECT id,aid,name,description,image,tags,type,position,access FROM contracts WHERE name IS NOT NULL";
    if(search){
      contracts_sql += " AND (";  
      var first = 0;    
      if(searchFields == 'name' || searchFields.includes("name")){
        contracts_sql += "name LIKE '%" + search + "%'";
        first = 1;
      }
      if(searchFields.includes("description")){
        if(first == 1){ contracts_sql += " OR "; }
        contracts_sql += "description LIKE '%" + search + "%'";
      }
      if(searchFields.includes("tags")){
        if(first == 1){ contracts_sql += " OR "; }
        contracts_sql += "tags LIKE '%" + search + "%'";
      } 
      contracts_sql += ")";           
    } 
    if(type && type.length > 1){
      contracts_sql += " AND type = '" + type + "'";
    }  
    if(position && position.length > 1){
      contracts_sql += " AND position = '" + position + "'";
    } 
    if(access && access.length > 1){
      contracts_sql += " AND access = '" + access + "'";
    }         
    if(noTags && noTags == 1){
      contracts_sql += " AND (tags is null or tags = 'API' or tags = '' or tags = 'Tag')";
    }   

    if(latest == 1){
      contracts_sql += " ORDER BY ID DESC";
    }
    else{
      contracts_sql += " ORDER BY name ASC";
    }

    contracts_sql += " LIMIT " + page + "," + limit;

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
      meta.totalRecords = totalRecords;
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

  var organization = 'api-evangelist';
  var bucket = organization;
  var body = req.body;   

  var contract_name = body.name;
  var contract_slug = common.slugify(contract_name);
  var contract_description = body.description;
  var contract_url = body.humanUrl;
  var contract_position = body.position;
  var contract_access = body.access;
          
  var contract = {};
  contract.aid = common.slugify(contract_name);
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

  contract.url = 'https://raw.githubusercontent.com/api-evangelist/' + common.slugify(contract_name) + '/refs/heads/main/apis.yml';
  contract.specificationVersion = '0.19';
  
  contract.apis = [];

  var a = {};
  a.aid = common.slugify(contract_name) + ':' + common.slugify(contract_name);
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

  var check_contract_sql = "SELECT * FROM contracts WHERE aid = " +  connection.escape(common.slugify(contract_name));
  connection.query(check_contract_sql, function (error, contracts, fields) {                   

    if(contracts.length > 0){
      //Already Exists
      resp.send(contracts);
    }
    else{


      var insert_contract_sql = "INSERT INTO contracts(aid,name,description,contract) VALUES(" +  connection.escape(common.slugify(contract_name)) + "," +  connection.escape(common.slugify(contract_name)) + "," + connection.escape(common.slugify(contract_name)) + "," + connection.escape(JSON.stringify(contract)) + ")";
      connection.query(insert_contract_sql, function (error, contracts, fields) {     

        var github_url = 'https://api.github.com/orgs/' + organization + '/repos';
        
        var r = {};
        r.name = common.slugify(contract_name);

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
                  m.options = options;    
                  m.repo = r;            
                  resp.send(m); 
                   
              }
              response.json().then(function(data) { 


                var github_url = 'https://api.github.com/repos/' + organization + '/' + common.slugify(contract_name) + '/contents/apis.yml';
                var c = {};
                c.name = "Kin Lane";
                c.email = "kinlane@gmail.com";

                var m = {};
                m.message = 'Writing APIs.yml';
                m.committer = c;
                m.content = btoa(yaml.dump(contract));

                // BEGIN COMMIT TO GITHUB
                const options = {
                    method: 'PUT',
                    headers: {
                        "Accept": "application/vnd.github+json",
                        "X-GitHub-Api-Version": "2022-11-28",
                        "Authorization": 'Bearer ' + github_token                
                    },
                    body: JSON.stringify(m)
                  };                    

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

                        var github_url = 'https://api.github.com/repos/' + organization + '/' + common.slugify(contract_name) + '/contents/README.md';

                        var readme = '# ' + contract_name + '\n';
                        readme += 'This is a repo for managing the APIs.io listing for ' + contract_name + '.';

                        var c = {};
                        c.name = "Kin Lane";
                        c.email = "kinlane@gmail.com";
        
                        var m = {};
                        m.message = 'Writing README';
                        m.committer = c;
                        m.content = btoa(readme);
        
                        // BEGIN COMMIT TO GITHUB
                        const options = {
                            method: 'PUT',
                            headers: {
                                "Accept": "application/vnd.github+json",
                                "X-GitHub-Api-Version": "2022-11-28",
                                "Authorization": 'Bearer ' + github_token                
                            },
                            body: JSON.stringify(m)
                          };                    
        
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
    
                                resp.send(contract); 
                                      
                
                              });
                            })
                            .catch(function(err) {
                                console.log('Error: ' + err);            
                                resp.send(err);                     
                          });  


                      });
                    })
                    .catch(function(err) {
                        console.log('Error: ' + err);            
                        resp.send(err);                     
                  });                         

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