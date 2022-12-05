import fs from "fs";

const readFile = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  return file;
};

type Instruction = {
  move: number;
  from: number;
  to: number;
};

const parseFile = (filename: string) => {
  const file = readFile(filename);
  const [stackStr, instructionsStr] = file.split("\r\n\r\n");

  const stackRows = stackStr.split("\r\n");
  const indexes = stackRows
    .pop()!
    .split("   ")
    .map((ind) => Number(ind.trim()));

  const stacks = new Map<number, (string | null)[]>();
  stackRows
    .map((row) =>
      row.match(/.{1,4}/g)!.map((str) => {
        let result = str.trim();
        if (result.includes("[")) {
          return result.split("[")[1].split("]")[0];
        }
        return null;
      })
    )
    .forEach((row) => {
      row.forEach((crate, i) => {
        if (crate !== null) {
          stacks.set(i + 1, (stacks.get(i + 1) ?? []).concat([crate]));
        }
      });
    });

  stacks.forEach((arr) => arr.reverse());

  const instructionRows = instructionsStr.split("\r\n");
  const instructions: Instruction[] = instructionRows.map((row) => ({
    move: Number(row.split("move ")[1].split(" from")[0]),
    from: Number(row.split("move ")[1].split(" from ")[1].split(" to")[0]),
    to: Number(row.split("from ")[1].split(" to ")[1]),
  }));

  return { stacks, instructions, indexes };
};

const solvePuzzle1 = () => {
  const { stacks, instructions, indexes } = parseFile("input.txt");

  instructions.forEach((instruction) => {
    const fromStack = stacks.get(instruction.from)!;
    const toStack = stacks.get(instruction.to)!;
    const amount = instruction.move;
    for (let i = 0; i < amount; i++) {
      toStack.push(fromStack.pop()!);
    }
  });
  let result = "";
  indexes.forEach((index) => {
    const stack = stacks.get(index)!;
    const topCrate = stack[stack.length - 1];
    result += topCrate;
  });
  console.log(result);
};
solvePuzzle1();

const solvePuzzle2 = () => {
  const { stacks, instructions, indexes } = parseFile("input.txt");

  instructions.forEach((instruction) => {
    const fromStack = stacks.get(instruction.from)!;
    const toStack = stacks.get(instruction.to)!;
    const amount = instruction.move;
    const selectedCrates = fromStack.splice(-amount, amount);
    stacks.set(instruction.to, toStack.concat(selectedCrates));
  });
  let result = "";
  indexes.forEach((index) => {
    const stack = stacks.get(index)!;
    const topCrate = stack[stack.length - 1];
    result += topCrate;
  });
  console.log(result);
};
solvePuzzle2();
