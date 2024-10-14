const express = require('express');
const app = express();

const getContracts = require('./paths/getContracts.js');
app.use('/contracts', getContracts);

app.listen(1300, () => {
  console.log('Server listening on port 1300');
});