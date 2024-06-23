#!/usr/bin/node
// create an add function
const firstDigit = Number(process.argv[2]);
const secondDigit = Number(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(firstDigit, secondDigit);
