#!/usr/bin/node
// Print second biggest digit
let argList = process.argv.slice(2).map(Number);
argList = argList.sort();
if (argList.length < 2) {
  console.log(0);
} else {
  argList.sort((a, b) => b - a);
  console.log(argList[1]);
}
