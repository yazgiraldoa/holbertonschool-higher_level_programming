#!/usr/bin/node
// Script that display the status code of a GET request.
const request = require('request');
const { argv } = require('process');

request.get(argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:', response.statusCode);
});
