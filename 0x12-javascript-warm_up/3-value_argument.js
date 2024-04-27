#!/usr/bin/node
// Prints the first argument passed to it
const x = process.argv;
if (x[2] === undefined) {
  console.log('No argument');
} else {
  console.log(x[2]);
}
