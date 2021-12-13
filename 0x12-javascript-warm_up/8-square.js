#!/usr/bin/node
const { argv } = require('process');
let i = 0;

if (!(parseInt(argv[2]))) {
  console.log('Missing size');
} else {
  while (i < argv[2]) {
    console.log('X'.repeat(argv[2]));
    i++;
  }
}
