#!/usr/bin/node
let myVar = process.argv.length;
if (myVar > 2) {
  console.log('Argument' + (argc > 3 ? 's' : '') + ' found');
}else{
  console.log('No argument');
};
