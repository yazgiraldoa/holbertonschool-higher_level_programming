#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  let times = 0;

  while (times < x) {
    theFunction();
    times++;
  }
};
