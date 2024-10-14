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
    //contracts_sql += " LIMIT " + page + "," + limit;
    contracts_sql += " LIMIT 0,25";

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

})

module.exports = router;