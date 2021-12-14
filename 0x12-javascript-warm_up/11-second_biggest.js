#!/usr/bin/node

const { argv } = require('process');
let i = 2;
let sorted = [];
const arr = [];

if (!argv[2]) {
  console.log('0');
} else if (argv[2] && !argv[3]) {
  console.log('0');
} else {
  while (i <= argv.length) {
    arr.push(parseInt(argv[i]));
    i++;
  }

  sorted = arr.sort(function (a, b) { return b - a; });
  console.log(sorted[1]);
}
