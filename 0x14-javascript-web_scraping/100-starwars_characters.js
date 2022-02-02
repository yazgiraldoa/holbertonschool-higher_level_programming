#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:
const request = require('request');
const { argv } = require('process');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request.get(url, function (error, response, body) {
  if (error) { console.log(error); return; }

  const json = JSON.parse(body).characters;
  for (const person of json) {
    request.get(person, function (error, response, body) {
      if (error) { console.log(error); return; }
      console.log(JSON.parse(body).name);
    });
  }
});
