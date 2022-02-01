#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const { argv } = require('process');
const url = argv[2];
let count = 0;

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const json = JSON.parse(body).results;
  for (const movie of json) {
    for (const person of movie.characters) {
      if (person.includes('18')) { count += 1; }
    }
  }
  console.log(count);
});
