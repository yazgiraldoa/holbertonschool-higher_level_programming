#!/usr/bin/node
const { argv } = require('process');
let i = 0;

if (!(parseInt(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  while (i < argv[2]) {
    console.log('C is fun');
    i++;
  }
}
