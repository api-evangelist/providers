const express = require('express');
const cors = require('cors');
const app = express();

const getContracts = require('./paths/getContracts.js');
app.use('/contracts', getContracts);

app.use(cors({
  origin: '*', // Allow requests from this origin
  methods: ['GET', 'POST', 'PUT', 'DELETE'], // Allowed methods
  allowedHeaders: ['Content-Type', 'Authorization'], // Allowed headers
  credentials: true // Allow credentials (cookies, authorization headers)
}));

app.listen(3300, () => {
  console.log('Server listening on port 3300');
});