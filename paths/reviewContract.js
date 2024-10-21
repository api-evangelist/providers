const spectralCore = require('@stoplight/spectral-core')
const { Spectral, Document } = spectralCore
const Parsers = require('@stoplight/spectral-parsers')
const { truthy, pattern, xor } = require('@stoplight/spectral-functions')
const {
  bundleAndLoadRuleset
} = require('@stoplight/spectral-ruleset-bundler/with-loader')
const spectralRuntime = require('@stoplight/spectral-runtime')
const { fetch } = spectralRuntime
const fs = require('fs');
const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
var github_token = store.github_token;

const spectral = new Spectral();

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

    var apis_json = req.body; 
    console.log(apis_json);  
  
    var rules_path = '../rules/operational-rules.yml';
    var ruleset = bundleAndLoadRuleset(path.resolve(rules_path), { fs, fetch });
    //var ruleset = validate(path);

    spectral.setRuleset(ruleset);

    return spectral.run(apis_json).then(results => {
        resp.send(results);
    });    

}); 

async function validate(path) {
    var rulesetFile = await bundleAndLoadRuleset(path.resolve(path), { fs, fetch });
    return rulesetFile;
  }
  

module.exports = router;