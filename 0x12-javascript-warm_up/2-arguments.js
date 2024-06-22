#!/usr/bin/node
// Print response for different number of args
const { argv } = require('node:process');
const argvLen = argv.length;

if (argvLen === 3) {
  console.log('Argument found');
} else if (argvLen > 2) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
