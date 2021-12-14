#!/usr/bin/node

const { argv } = require('process');
const num = parseInt(argv[2]);

function factorial (argv) {
  if (!argv) {
    return 1;
  }

  if (argv < 0) {
    return -1;
  } else if (argv === 0) {
    return 1;
  } else {
    return (argv * factorial(argv - 1));
  }
}

console.log(factorial(num));
