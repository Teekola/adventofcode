const fs = require("fs");

const readFile = (filename) => {
   const file = fs.readFileSync(filename, "utf-8");
   return file;
}
const file = readFile("./input.txt");

// PT 1
const elves = file.split("\r\n\r\n");
let largestSum = -1;
elves.forEach(elf => {
   let currentSum = elf.split("\r\n").reduce((p, c) => p + Number(c), 0);
   if (currentSum > largestSum) {
      largestSum = currentSum;
   }
})

console.log(largestSum);

// PT 2
const elfTotals = elves.map(elf => elf.split("\r\n").reduce((p, c) => p + Number(c), 0));
elfTotals.sort((a, b) => a > b ? -1 : 1);

const sumOfTopThree = elfTotals.splice(0, 3).reduce((p, c) => p + c, 0);

console.log(sumOfTopThree);

