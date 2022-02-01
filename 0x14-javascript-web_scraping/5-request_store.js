#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.
const fs = require('fs');
const request = require('request');
const { argv } = require('process');
const url = argv[2];
const file = argv[3];

request.get(url, function (error, body) {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(file, body.body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
