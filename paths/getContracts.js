const express = require('express');
const mysql = require('mysql');
const router = express.Router();
const store = require('../../store/keys.json');

var connection = mysql.createConnection({
  host     : store.api_search_database_host,
  database : store.api_search_database_database,
  user: store.api_search_database_user,
  password: store.api_search_database_password
  });

router.get('/', (req, resp)=>{ 

  var contracts_sql = "SELECT * FROM contracts;";
  connection.query(contracts_sql, function (error, contracts, fields) { 
    resp.send(contracts);    
  }).on('error', err => {
    //resp.send(err);
  });                   

})

module.exports = router;