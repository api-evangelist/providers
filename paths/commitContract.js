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
    var changes_sql = "SELECT DISTINCT file FROM contract_changes WHERE aid = " + connection.escape(aid) + " AND committed = 0";
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
                          

              const options = {
                  method: 'get',
                  headers: {
                      "Accept": "application/vnd.github+json",
                      "Authorization": 'Bearer ' + github_token
                  }
              }; 
                            

            var path = '/repos/' + organization + '/' + aid + '/contents/' + file;
            var github_url = 'https://api.github.com' + path;                        
            fetch(github_url,options)
                .then(function(response) {
                    if (!response.ok) {
                      
                        //console.log('Error with Status Code: ' + response.status);
                        var c = {};
                        c.name = "Kin Lane";
                        c.email = "kinlane@gmail.com";
  
                        var m = {};
                        m.message = 'Writing ' + file;
                        m.committer = c;
                        m.content = btoa(body);
  
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
  
                                // BEGIN UPDATE changes
                                var update_changes = "UPDATE contract_changes SET committed = 1 WHERE aid = " + connection.escape(aid) + " AND file = " + connection.escape(file);
                                connection.query(update_changes, function (error, changes_results, fields) { 
  
                                  // BEGIN PULL FILE
                                  var changes_sql = "SELECT DISTINCT file FROM contract_changes WHERE aid = " + connection.escape(aid) + " AND committed = 0";
                                  connection.query(changes_sql, function (error, changes, fields) { 
  
                                    if(changes[0]){
  
                                      var file = changes[0].file;
  
                                      var meta = {};
                                      meta.limit = 1;
                                      meta.page = 0;
                                      meta.totalPages = totalPages;
                          
                                      var response = {};
                                      response.meta = meta;
                                      response.data = [{"file":file}];       
                                      response.here = "1";
                                      resp.send(response); 
  
                                      // MORE TO DO
  
                                    }
                                  else{
  
                                    // BEGIN PULL FILE
                                    var changes_sql = "SELECT * FROM contract_changes WHERE aid = " + connection.escape(aid) + " AND committed = 1";
                                    connection.query(changes_sql, function (error, changes, fields) { 
  
                                      var issue_body = '';
                                      for (let i = 0; i < changes.length; i++) {
                                        issue_body += ' - **' + changes[i].name + '** - ' + changes[i].description + '\r\n';
                                      }                                    
  
                                      var github_url = 'https://api.github.com/repos/' + organization + '/' + aid + '/issues'; 
  
                                      // Success - Issue
                                      var m = {};
                                      m.title = "Change Log Entry";
                                      m.body = issue_body;
                                      m.assignees = ['kinlane'];
                                      m.labels = ['change-log'];
                
                                      // BEGIN COMMIT TO GITHUB
                                      const options = {
                                          method: 'post',
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
                                                resp.send(m); 
                                            }
                                            response.json().then(function(data) {                                      
  
                                              // BEGIN UPDATE CONTRACTS
                                              var update_changes = "UPDATE contracts SET contract_changes = 0 WHERE aid = " + connection.escape(aid);
                                              connection.query(update_changes, function (error, changes_results, fields) { 
  
                                                // BEGIN UPDATE CONTRACTS
                                                var update_changes = "DELETE FROM contract_changes WHERE aid = " + connection.escape(aid);
                                                connection.query(update_changes, function (error, changes_results, fields) { 
  
                                                  var totalPages = 1;
  
                                                  var meta = {};
                                                  meta.limit = 1;
                                                  meta.page = 0;
                                                  meta.totalPages = totalPages;
                                      
                                                  var response = {};
                                                  response.meta = meta;
                                                  response.data = [];
                                                  
                                                  resp.send(response); 
  
                                                }).on('error', err => {
                                                  resp.send(err);
                                                });                                             
                                                // END UPDATE CONTRACTS                                              
  
                                              }).on('error', err => {
                                                resp.send(err);
                                              });                                             
                                              // END UPDATE CONTRACTS
  
                                            });
                                          })
                                          .catch(function(err) {
                                            console.log('Error: ' + err);
                                            var response = {};
                                            response.data = err;               
                                            resp.send(response);                     
                                      });                                             
  
                                    }).on('error', err => {
                                      resp.send(err);
                                    });                                       
  
                                  }
  
                                  }).on('error', err => {
                                    resp.send(err);
                                  });                                 
  
                                }).on('error', err => {
                                  resp.send(err);
                                }); 
                                
                                // END Update contract_changes                        
  
                              });
                            })
                            .catch(function(err) {
                                console.log('Error: ' + err);
                                var response = {};
                                response.data = err; 
                                response.here = '1'; 
                                resp.send(response);                     
                        });

                    }
                    response.json().then(function(data) {                       
                      
                      var sha = data.sha;
                                            
                      var c = {};
                      c.name = "Kin Lane";
                      c.email = "kinlane@gmail.com";

                      var m = {};
                      m.message = 'Writing ' + file;
                      m.committer = c;
                      m.sha = sha;
                      m.content = btoa(body);

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

                              // BEGIN UPDATE changes
                              var update_changes = "UPDATE contract_changes SET committed = 1 WHERE aid = " + connection.escape(aid) + " AND file = " + connection.escape(file);                              
                              connection.query(update_changes, function (error, changes_results, fields) { 

                                // BEGIN PULL FILE
                                var changes_sql = "SELECT DISTINCT file FROM contract_changes WHERE aid = " + connection.escape(aid) + " AND committed = 0";
                                connection.query(changes_sql, function (error, changes, fields) { 

                                  if(changes[0]){

                                    var file = changes[0].file;

                                    var meta = {};
                                    meta.limit = 1;
                                    meta.page = 0;
                                    meta.totalPages = totalPages;
                        
                                    var response = {};
                                    response.meta = meta;
                                    response.data = [{"file":file}];       
                                    response.here = "1";
                                    resp.send(response); 

                                    // MORE TO DO

                                  }
                                else{

                                  // BEGIN PULL FILE
                                  var changes_sql = "SELECT * FROM contract_changes WHERE aid = " + connection.escape(aid) + " AND committed = 1";
                                  connection.query(changes_sql, function (error, changes, fields) { 

                                    var issue_body = '';
                                    for (let i = 0; i < changes.length; i++) {
                                      issue_body += ' - **' + changes[i].name + '** - ' + changes[i].description + '\r\n';
                                    }                                    

                                    var github_url = 'https://api.github.com/repos/' + organization + '/' + aid + '/issues'; 

                                    // Success - Issue
                                    var m = {};
                                    m.title = "Change Log Entry";
                                    m.body = issue_body;
                                    m.assignees = ['kinlane'];
                                    m.labels = ['change-log'];
              
                                    // BEGIN COMMIT TO GITHUB
                                    const options = {
                                        method: 'post',
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
                                              resp.send(m); 
                                          }
                                          response.json().then(function(data) {                                      

                                            // BEGIN UPDATE CONTRACTS
                                            var update_changes = "UPDATE contracts SET contract_changes = 0 WHERE aid = " + connection.escape(aid);
                                            connection.query(update_changes, function (error, changes_results, fields) { 

                                              // BEGIN UPDATE CONTRACTS
                                              var update_changes = "DELETE FROM contract_changes WHERE aid = " + connection.escape(aid);
                                              connection.query(update_changes, function (error, changes_results, fields) { 

                                                var totalPages = 1;

                                                var meta = {};
                                                meta.limit = 1;
                                                meta.page = 0;
                                                meta.totalPages = totalPages;
                                    
                                                var response = {};
                                                response.meta = meta;
                                                response.data = [];
                                                
                                                resp.send(response); 

                                              }).on('error', err => {
                                                resp.send(err);
                                              });                                             
                                              // END UPDATE CONTRACTS                                              

                                            }).on('error', err => {
                                              resp.send(err);
                                            });                                             
                                            // END UPDATE CONTRACTS

                                          });
                                        })
                                        .catch(function(err) {
                                          console.log('Error: ' + err);
                                          var response = {};
                                          response.data = err;               
                                          resp.send(response);                     
                                    });                                             

                                  }).on('error', err => {
                                    resp.send(err);
                                  });                                       

                                }

                                }).on('error', err => {
                                  resp.send(err);
                                });                                 

                              }).on('error', err => {
                                resp.send(err);
                              }); 
                              
                              // END Update contract_changes                        

                            });
                          })
                          .catch(function(err) {
                              console.log('Error: ' + err);
                              var response = {};
                              response.data = err; 
                              response.here = '1'; 
                              resp.send(response);                     
                      }); 
                    
                  });
                })
                .catch(function(err) {
                    console.log('Error: ' + err);
                    var response = {};
                    response.data = err;               
                    resp.send(response);                     
              }); 

              // END COMMIT TO GITHUB
              
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