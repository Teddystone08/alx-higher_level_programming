#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const ab = parseInt(process.argv[2]);
const ba = parseInt(process.argv[3]);
console.log(add(ab, ba));
