#!/usr/bin/node

const req = require('request');
req.get('https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/', function (error, response, body) {
  if (error) throw error;
  else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
