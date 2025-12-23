const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
const common = require('../../libraries/common');
var github_token = store.github_token;
const shell = require('shelljs');

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

router.patch('/', jsonParser, function (req, resp) {
  
  var aid = req.params.aid;

  var organization = 'api-evangelist';

  var body = req.body; 
  var description = body.description;

  var path = '/laneworks/api-evangelist/all';
  shell.cd(path);
  shell.exec('git clone https://github.com/api-evangelist/' + aid); 
  path = '/laneworks/api-evangelist/all/' + aid;
  shell.cd(path);
  path = '/laneworks/api-evangelist/all/' + aid + '/apis.yml';
  var save_content = yaml.dump(body); 
  fs.writeFileSync(path, save_content, (err) => { }); 
  
  var response = {};
  response.message = "Saved";
  resp.send(response);      

}); 

module.exports = router;