#!/usr/bin/node
// create a square
const squareSize = process.argv[2];
if (!isNaN(squareSize)) {
  for (let a = 0; a <= (squareSize - 1); a++) {
    console.log('X'.repeat(squareSize));
  }
} else {
  console.log('Missing size');
}
