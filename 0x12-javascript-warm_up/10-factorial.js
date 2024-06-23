#!/usr/bin/node
// get the factorial using recussion
const value = process.argv[2];
function factorialRecursive (value) {
  if (value < 0) {
    console.log('Value must be greater than 0');
  } else if (isNaN(value) || (value === 0) || (value === 1)) {
    return 1;
  } else {
    return value * factorialRecursive(value - 1);
  }
}
console.log(factorialRecursive(value));
