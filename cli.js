'use strict';

process.argv.forEach((val, index) => {
    console.log(`${index}: ${val}`);
});

var args = process.argv.slice(2);

var mainProcess = {};
mainProcess.args = args;


console.log(`Hello abcd !!`);
console.log(args);
