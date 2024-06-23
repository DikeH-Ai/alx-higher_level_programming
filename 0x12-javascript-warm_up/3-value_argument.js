#!/usr/bin/node
// Print the first argument passed to script
// print no argument if none is passed
const { argv } = require('node:process');
if (argv[2] !== undefined) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
