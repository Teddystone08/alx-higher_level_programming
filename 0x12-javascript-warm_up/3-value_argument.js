#!/usr/bin/node
const len = process.argv;
if (len === undefined) {
  console.log('No argument');
} else {
  console.log(len);
}
