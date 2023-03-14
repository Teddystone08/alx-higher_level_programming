#!/usr/bin/node
const len = process.argv;
if (len[2] === undefined) {
  console.log('No argument');
} else {
  console.log(len[2]);
}
