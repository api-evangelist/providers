const express = require('express');
var cors = require('cors');
const app = express();

app.use(cors());

const getContracts = require('./paths/getContracts.js');
app.use('/contracts', getContracts);

const getContract = require('./paths/getContract.js');
app.use('/contracts/:aid', getContract);

app.listen(3300, () => {
  console.log('Server listening on port 3300');
});

