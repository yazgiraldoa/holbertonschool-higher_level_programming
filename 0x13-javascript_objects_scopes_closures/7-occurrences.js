#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;

  for (const element of list) {
    if (element === searchElement) {
      ocurrences += 1;
    }
  }

  return ocurrences;
};
