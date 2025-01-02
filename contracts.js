const express = require('express');
var cors = require('cors');
const app = express();

app.use(cors()); 
app.use(express.json({ limit: '50mb' }));

const getContracts = require('./paths/getContracts.js');
app.use('/contracts', getContracts);

const rebuildContracts = require('./paths/rebuildContracts.js');
app.use('/contracts/rebuild', rebuildContracts);

const getContract = require('./paths/getContract.js');
app.use('/contracts/:aid', getContract);

const commitContract = require('./paths/commitContract.js');
app.use('/contracts/:aid/commit', commitContract);

const reviewContract = require('./paths/reviewContract.js');
app.use('/contracts/:aid/review', reviewContract);

const saveContractReadMe = require('./paths/saveContractReadMe.js');
app.use('/contracts/:aid/readme', saveContractReadMe);

const writeContractDescription = require('./paths/writeContractDescription.js');
app.use('/contracts/:aid/write/description', writeContractDescription);

const searchForContractAPIDocumentation = require('./paths/searchForContractAPIDocumentation.js');
app.use('/contracts/:aid/search/for/documentation', searchForContractAPIDocumentation);

app.listen(3300, () => {
  console.log('Server listening on port 3300');
});

