#!/usr/bin/node
// Script that computes the number of tasks completed by user id.
const request = require('request');
const { argv } = require('process');
const url = argv[2];
const dict = {};

request.get(url, function (error, body) {
  if (error) {
    console.log(error);
    return;
  }
  const json = JSON.parse(body.body);
  for (const tasks of json) {
    if (tasks.completed === true) {
      if (dict[tasks.userId] === undefined) {
        dict[tasks.userId] = 1;
      } else {
        dict[tasks.userId] += 1;
      }
    }
  }
  console.log(dict);
});
