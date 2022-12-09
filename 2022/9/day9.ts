import fs from "fs";

const readFileToArray = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  const lines = file.split("\r\n");
  return lines;
};

type Move = {
  direction: "R" | "L" | "U" | "D";
  amount: number;
};

type Position = {
  x: number;
  y: number;
};

const horizontalDistance = (pos1: Position, pos2: Position) => {
  return Math.abs(pos1.x - pos2.x);
};

const verticalDistance = (pos1: Position, pos2: Position) => {
  return Math.abs(pos1.y - pos2.y);
};

const mustMoveDiagonally = (pos1: Position, pos2: Position) => {
  return (
    (horizontalDistance(pos1, pos2) === 2 &&
      verticalDistance(pos1, pos2) === 1) ||
    (horizontalDistance(pos1, pos2) === 1 && verticalDistance(pos1, pos2) === 2)
  );
};

const addTailPosition = (visited: Set<string>, tailPosition: Position) => {
  visited.add(JSON.stringify(tailPosition));
};

const moveDiagonally = (tailPosition: Position, headPosition: Position) => {
  // Is Above => Move one down
  if (tailPosition.y > headPosition.y) {
    tailPosition.y--;
  }
  // Is Below => Move one up
  else if (tailPosition.y < headPosition.y) {
    tailPosition.y++;
  }
  // Is Left side => Move one right
  if (tailPosition.x < headPosition.x) {
    tailPosition.x++;
  }
  // Is Right side => Move one left
  else if (tailPosition.x > headPosition.x) {
    tailPosition.x--;
  }
};

const moveLeft = (
  tailPosition: Position,
  headPosition: Position,
  steps: number,
  visited: Set<string>
) => {
  for (let i = 0; i < steps; i++) {
    // Move head
    headPosition.x--;

    // Diagonally too far
    if (mustMoveDiagonally(tailPosition, headPosition)) {
      moveDiagonally(tailPosition, headPosition);
      addTailPosition(visited, tailPosition);
    }
    // If horizontally too far
    else if (horizontalDistance(tailPosition, headPosition) === 2) {
      tailPosition.x--;
      addTailPosition(visited, tailPosition);
    }
  }
};

const moveRight = (
  tailPosition: Position,
  headPosition: Position,
  steps: number,
  visited: Set<string>
) => {
  for (let i = 0; i < steps; i++) {
    // Move Head
    headPosition.x++;

    // Diagonally too far
    if (mustMoveDiagonally(tailPosition, headPosition)) {
      moveDiagonally(tailPosition, headPosition);
      addTailPosition(visited, tailPosition);
    }
    // If horizontally too far
    else if (horizontalDistance(tailPosition, headPosition) === 2) {
      tailPosition.x++;
      addTailPosition(visited, tailPosition);
    }
  }
};
const moveUp = (
  tailPosition: Position,
  headPosition: Position,
  steps: number,
  visited: Set<string>
) => {
  for (let i = 0; i < steps; i++) {
    headPosition.y++;

    // Diagonally too far
    if (mustMoveDiagonally(tailPosition, headPosition)) {
      moveDiagonally(tailPosition, headPosition);
      addTailPosition(visited, tailPosition);
    }
    // If horizontally too far
    else if (verticalDistance(tailPosition, headPosition) === 2) {
      tailPosition.y++;
      addTailPosition(visited, tailPosition);
    }
  }
};
const moveDown = (
  tailPosition: Position,
  headPosition: Position,
  steps: number,
  visited: Set<string>
) => {
  for (let i = 0; i < steps; i++) {
    headPosition.y--;

    // Diagonally too far
    if (mustMoveDiagonally(tailPosition, headPosition)) {
      moveDiagonally(tailPosition, headPosition);
      addTailPosition(visited, tailPosition);
    }
    // If vertically too far
    else if (verticalDistance(tailPosition, headPosition) === 2) {
      tailPosition.y--;
      addTailPosition(visited, tailPosition);
    }
  }
};

const moveFnc = {
  L: moveLeft,
  R: moveRight,
  U: moveUp,
  D: moveDown,
};

const solvePuzzle1 = () => {
  const moves = readFileToArray("input.txt").map((move) => {
    const [direction, amount] = move.split(" ");
    return { direction, amount: Number(amount) };
  }) as Move[];

  const visited = new Set<string>();
  const tailPosition = { x: 0, y: 0 };
  const headPosition = { x: 0, y: 0 };
  visited.add(JSON.stringify(tailPosition));

  // Go through each move
  moves.forEach((move: Move) => {
    moveFnc[move.direction](tailPosition, headPosition, move.amount, visited);
  });
  console.log(visited.size);
};
solvePuzzle1();

const solvePuzzle2 = () => {};
solvePuzzle2();
