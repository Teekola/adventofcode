import fs from "fs";

const readFileToArray = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  const lines = file.split("\r\n");
  return lines;
};

const solvePuzzle1 = () => {
  const linesArray = readFileToArray("input.txt");

  console.log(linesArray);
};
solvePuzzle1();

const solvePuzzle2 = () => {
  const linesArray = readFileToArray("input.txt");

  console.log(linesArray);
};
solvePuzzle2();
