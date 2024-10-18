const express = require('express');
const mysql = require('mysql');
const router = express.Router({ mergeParams: true })
const store = require('../../store/keys.json');

var connection = mysql.createConnection({
  host     : store.api_search_database_host,
  database : store.api_search_database_database,
  user: store.api_search_database_user,
  password: store.api_search_database_password
  });

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

router.put('/', (req, resp)=>{ 

  var body = resp.body;

  resp.send(body);       

});  

module.exports = router;