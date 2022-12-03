import fs from "fs";

const readFile = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  return file;
};

const parseInput = (file: string) => {
  return file.split("\r\n");
};

// PT 1
