#!/usr/bin/node
// Print digit to stdout
const myVar = process.argv[2];
if (typeof myVar === 'number') {
  console.log(myVar);
} else if (isNaN(Number(myVar))) {
  console.log('Not a number');
} else if (myVar === undefined) {
  console.log('Not a number');
} else {
  console.log(myVar);
}
