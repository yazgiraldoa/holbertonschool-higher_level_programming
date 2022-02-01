#!/usr/bin/node
// Script that reads and prints the content of a file.
const fs = require('fs');
const { argv } = require('process');

fs.readFile(argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data.toString());
});
