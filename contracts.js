const express = require('express');
var cors = require('cors');
const app = express();

app.use(cors());

const getContracts = require('./paths/getContracts.js');
app.use('/contracts', getContracts);

const getContract = require('./paths/getContract.js');
app.use('/contracts/:aid', getContract);

const commitContract = require('./paths/commitContract.js');
app.use('/contracts/:aid/commit', commitContract);

const reviewContract = require('./paths/reviewContract.js');
app.use('/contracts/:aid/review', reviewContract);


app.listen(3300, () => {
  console.log('Server listening on port 3300');
});

