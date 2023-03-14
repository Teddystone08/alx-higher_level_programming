#!/usr/bin/node
const len = process.argv;
const i = parseInt(len[2]);
if (isNaN(i)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + i);
}
