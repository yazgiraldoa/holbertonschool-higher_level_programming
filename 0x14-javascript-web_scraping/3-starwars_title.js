#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const { argv } = require('process');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
