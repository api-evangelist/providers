const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const fs = require('fs');
const express = require('express');
const mysql = require('mysql');
const yaml = require('js-yaml');
const router = express.Router();
const store = require('../../store/keys.json'); 
const common = require('../../libraries/common');
const shell = require('shelljs');

var connection = mysql.createConnection({
  host     : store.api_search_database_host,
  database : store.api_search_database_database,
  user: store.api_search_database_user,
  password: store.api_search_database_password
  });


router.get('/', (req, resp)=>{ 

  var path = "/laneworks/api-evangelist/contracts";
  shell.cd(path);
  shell.exec("git pull");
  shell.cd("/");    

  var contract_sql = "SELECT * FROM contracts;";
  connection.query(contract_sql, function (error, contracts, fields) {

    for (let i = 0; i < contracts.length; i++) {       

      var aid = contracts[i].aid;          
      var contract = JSON.parse(contracts[i].contract);
        
      var contract_path = '/laneworks/api-evangelist/contracts/_store/' + aid + '.md'
      
      var contract_markdown = "---\r\n" + yaml.dump(contract) + "\r\n---";
       
      fs.writeFile(contract_path, contract_markdown, (err) => {
        if (err) console.log(err);
        if(i == contracts.length-1){


          var path = "/laneworks/api-evangelist/contracts";
          shell.cd(path);
          shell.exec("git add *");
          shell.exec("git commit -m 'rebuild'");
          shell.exec("git push");

          var m = {};
          m.message = "published " + contracts.length + " contracts.";
          resp.send(m);    
        }
      });  

    }

  }).on('error', err => {
    resp.send(err);
  });     
     

})

module.exports = router;