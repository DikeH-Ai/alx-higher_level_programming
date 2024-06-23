#!/usr/bin/node
// Print second biggest digit
let argList = process.argv.slice(2);
argList = argList.sort();
if (argList.length < 2) {
  console.log(0);
} else {
  console.log(argList[argList.length - 2]);
}
