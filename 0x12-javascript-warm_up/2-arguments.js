#!/usr/bin/node

const len = process.argv;
if (len.length === 0) {
  console.log('No argument');
} else if (len.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
