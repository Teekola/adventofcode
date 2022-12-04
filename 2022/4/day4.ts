import fs from "fs";

const readFileToArray = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  const lines = file.split("\r\n");
  return lines;
};

const parseLinesToRangePairs = (lines: string[]): Range[][] => {
  return lines.map((line) => {
    const [first, second] = line.split(",");
    const [start1, end1] = first.split("-");
    const [start2, end2] = second.split("-");
    return [
      {
        start: Number(start1),
        end: Number(end1),
      },
      {
        start: Number(start2),
        end: Number(end2),
      },
    ];
  });
};

type Range = {
  start: number;
  end: number;
};

const oneRangeContainsOther = (range1: Range, range2: Range) => {
  if (range1.start <= range2.start && range1.end >= range2.end) {
    return true;
  }

  if (range2.start <= range1.start && range2.end >= range1.end) {
    return true;
  }

  return false;
};

const solvePuzzle1 = () => {
  const linesArray = readFileToArray("input.txt");
  const rangesArray = parseLinesToRangePairs(linesArray);

  let sum = 0;
  for (const pair of rangesArray) {
    if (oneRangeContainsOther(pair[0], pair[1])) sum++;
  }
  console.log(sum);
};
solvePuzzle1();

const oneRangeOverlapsOther = (range1: Range, range2: Range) => {
  if (range1.start <= range2.end && range1.end >= range2.start) return true;
  if (range2.start <= range1.end && range2.end >= range1.start) return true;
  return false;
};

const solvePuzzle2 = () => {
  const linesArray = readFileToArray("input.txt");
  const rangesArray = parseLinesToRangePairs(linesArray);
  let sum = 0;
  for (const pair of rangesArray) {
    if (oneRangeOverlapsOther(pair[0], pair[1])) sum++;
  }
  console.log(sum);
};
solvePuzzle2();
