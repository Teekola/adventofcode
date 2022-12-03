import fs from "fs";

const readFile = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  return file;
};

const parseInput = (file: string) => {
  const lines = file.split("\r\n");
  return lines.map((line) => [
    line.slice(0, line.length / 2),
    line.slice(line.length / 2, line.length),
  ]);
};

const parseInput2 = (file: string) => {
  const lines = file.split("\r\n");
  return lines;
};

const getItemPriority = (item: string) => {
  const charCode = item.charCodeAt(0);
  if (charCode >= 97) {
    return charCode - 96;
  }
  return charCode - 38;
};

const getCommonItems = (comp1: string, comp2: string) => {
  const commonItems = new Set<string>();
  for (const item of comp1) {
    if (comp2.includes(item)) {
      commonItems.add(item);
    }
  }
  return commonItems;
};

const getCommonItemsFromArray = (comps: string[]) => {
  const commonItems = new Set<string>();
  const longest = comps.reduce((a, b) => {
    return a.length > b.length ? a : b;
  });
  for (const item of longest) {
    let foundFrom = 0;
    for (const comp of comps) {
      if (!comp.includes(item)) {
        break;
      }
      foundFrom++;
    }
    if (foundFrom === comps.length) {
      commonItems.add(item);
    }
  }
  return commonItems;
};

const solvePuzzle1 = () => {
  const rucksacks = parseInput(readFile("input.txt"));

  let sum = 0;
  rucksacks.forEach((rucksack) => {
    const commonItems = getCommonItems(rucksack[0], rucksack[1]);
    commonItems.forEach((item) => {
      sum += getItemPriority(item);
    });
  });

  console.log(sum);
};
solvePuzzle1();

const solvePuzzle2 = () => {
  const rucksacks = parseInput2(readFile("input.txt"));
  let sum = 0;
  for (let i = 0; i < rucksacks.length; i += 3) {
    const groupsCommonItems = getCommonItemsFromArray([
      rucksacks[i],
      rucksacks[i + 1],
      rucksacks[i + 2],
    ]);
    groupsCommonItems.forEach((item) => {
      sum += getItemPriority(item);
    });
  }
  console.log(sum);
};
solvePuzzle2();
