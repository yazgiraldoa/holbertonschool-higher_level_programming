#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const { argv } = require('process');
const url = argv[2] + '?id=18';

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const json = JSON.parse(body);
  console.log(json.count);
});
