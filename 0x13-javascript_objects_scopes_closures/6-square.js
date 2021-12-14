#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;

      while (i < this.height) {
        console.log(c.repeat(this.height));
        i++;
      }
    }
  }
};
