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

  var organization = req.query.organization;
  var search = req.query.search;

  var limit = req.query.limit;
  if(!limit){
    if(limit == ''){
      limit = 25;
    }
  }

  var page = req.query.page;
  if(!page){
    if(page == ''){
      page = 0;
    }
  }

  var contracts_sql = "SELECT COUNT(*) FROM contracts WHERE name IS NOT NULL";
  if(search!=''){
    contracts_sql += " AND (name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' OR tags LIKE '%" + search + "%')";
  }
  connection.query(contracts_sql, function (error, total, fields) { 

    contracts_sql = "SELECT * FROM contracts WHERE name IS NOT NULL";
    if(search!=''){
      contracts_sql += " AND (name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' OR tags LIKE '%" + search + "%')";
    }    
    //contracts_sql += " LIMIT " + page + "," + limit;
    contracts_sql += " LIMIT 0,25";

    connection.query(contracts_sql, function (error, contracts, fields) { 

      var meta = {};
      meta.search = search;
      meta.limit = limit;
      meta.page = page;
      meta.totalPages = total;

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

})

module.exports = router;