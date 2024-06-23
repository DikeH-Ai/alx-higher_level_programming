#!/usr/bin/node
// prints x times "C is fun"
const myVar = process.argv[2];
if (!isNaN(myVar)) {
  for (let a = 0; a <= (myVar - 1); a++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
