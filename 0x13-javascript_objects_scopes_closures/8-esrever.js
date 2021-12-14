#!/usr/bin/node

exports.esrever = function (list) {
  let last = list.length - 1;
  let first = 0;
  const arr = [];

  while (first < list.length) {
    arr[first] = list[last];
    last--;
    first++;
  }

  return arr;
};
