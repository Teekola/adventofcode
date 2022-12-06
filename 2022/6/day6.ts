import fs from "fs";

const readFile = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  return file;
};

const solvePuzzle1 = () => {
  const data = readFile("input.txt");

  const buffer = new Set<string>();
  let firstMarkerPos = -1;
  for (let i = 0; i < data.length - 3; i++) {
    buffer.add(data[i]);
    buffer.add(data[i + 1]);
    buffer.add(data[i + 2]);
    buffer.add(data[i + 3]);

    if (buffer.size === 4) {
      firstMarkerPos = i + 4;
      break;
    }
    buffer.clear();
  }
  console.log(firstMarkerPos);
};
solvePuzzle1();

const solvePuzzle2 = () => {
  const data = readFile("input.txt");

  const buffer = new Set<string>();
  let firstMarkerPos = -1;
  for (let i = 0; i < data.length - 13; i++) {
    data
      .substring(i, i + 14)
      .split("")
      .forEach((char) => buffer.add(char));

    if (buffer.size === 14) {
      firstMarkerPos = i + 14;
      break;
    }
    buffer.clear();
  }
  console.log(firstMarkerPos);
};
solvePuzzle2();
