const express = require('express');
const btoa = require('btoa');
const atob = require('atob');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const yaml = require('js-yaml');
const common = require('../../libraries/common');
const store = require('../../store/keys.json');
var github_token = store.github_token;

var jsonParser = bodyParser.json()

router.put('/', (req, resp)=>{ 
  
  var aid = req.params.aid;
  var name = req.body.name;    

  var openai_token = store.openai_token;

  var open_ai_url = "https://api.openai.com/v1/chat/completions";

  var chat = {};
  chat.model = "gpt-4o";
  chat.messages = [];

  var question = "Can you write a paragraph about what " + name + " does?";

  var message = {};
  message.role = "user";
  message.content = question;
  chat.messages.push(message);
  chat = JSON.stringify(chat);

  const options = {
      method: 'POST',
      headers: {
          "Content-Type": "application/json",
          "Authorization": 'Bearer ' + openai_token
      },
      body: chat
  };

  fetch(open_ai_url, options)
    .then(function (response) {
        if (!response.ok) {
            //console.log('Error with Status Code: ' + response.status);
        }
        response.json().then(function (data) {
            resp.send(data);              
        });
    })
    .catch(function (err) {
        if (err == 'TypeError: Failed to fetch') {
            //document.getElementById("alert").innerHTML = err;
        }
    });

}); 

module.exports = router;