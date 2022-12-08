import fs from "fs";

const readFileToArray = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  const lines = file.split("\r\n");
  return lines;
};

// Key is row, value is column
const notVisibleRangeLeft = new Map<number, number>();
// Key is row, value is column
const notVisibleRangeRight = new Map<number, number>();
// Key is col, value is row
const notVisibleRangeTop = new Map<{ row: number; col: number }, number>();
// Key is col, value is row
const notVisibleRangeBottom = new Map<number, number>();

const getTreeHeight = (row: number, col: number, map: string[]) => {
  return Number(map[row][col]);
};

const treeIsVisible = (row: number, col: number, map: string[]) => {
  const treeHeight = getTreeHeight(row, col, map);

  let isVisibleFromTop = true;
  let isVisibleFromBottom = true;
  let isVisibleFromLeft = true;
  let isVisibleFromRight = true;

  let currentRow = row;
  while (currentRow > 0) {
    currentRow--;
    if (treeHeight <= getTreeHeight(currentRow, col, map)) {
      isVisibleFromTop = false;
      break;
    }
  }
  if (isVisibleFromTop) return true;

  currentRow = row;
  while (currentRow < map.length - 1) {
    currentRow++;
    if (treeHeight <= getTreeHeight(currentRow, col, map)) {
      isVisibleFromBottom = false;
      break;
    }
  }
  if (isVisibleFromBottom) return true;

  let currentCol = col;
  while (currentCol < map.length - 1) {
    currentCol++;
    if (treeHeight <= getTreeHeight(row, currentCol, map)) {
      isVisibleFromRight = false;
      break;
    }
  }
  if (isVisibleFromRight) return true;

  currentCol = col;
  while (currentCol > 0) {
    currentCol--;
    if (treeHeight <= getTreeHeight(row, currentCol, map)) {
      isVisibleFromLeft = false;
      break;
    }
  }

  if (isVisibleFromLeft) {
    return true;
  }
  return false;
};

const solvePuzzle1 = () => {
  const allTrees = readFileToArray("input.txt");

  let visibleTrees = 0;
  for (let i = 0; i < allTrees.length; i++) {
    for (let j = 0; j < allTrees[0].length; j++) {
      const isVisible = treeIsVisible(i, j, allTrees);
      if (isVisible) visibleTrees++;
    }
  }
  console.log(visibleTrees);
};
solvePuzzle1();

const getScenicScore = (row: number, col: number, map: string[]) => {
  const treeHeight = getTreeHeight(row, col, map);

  let isVisibleFromTop = true;
  let isVisibleFromBottom = true;
  let isVisibleFromLeft = true;
  let isVisibleFromRight = true;

  const visibleTrees = {
    top: 0,
    left: 0,
    bottom: 0,
    right: 0,
  };

  let currentRow = row;
  while (currentRow > 0) {
    currentRow--;
    visibleTrees.top++;
    if (treeHeight <= getTreeHeight(currentRow, col, map)) {
      isVisibleFromTop = false;
      break;
    }
  }

  currentRow = row;
  while (currentRow < map.length - 1) {
    currentRow++;
    visibleTrees.bottom++;
    if (treeHeight <= getTreeHeight(currentRow, col, map)) {
      isVisibleFromBottom = false;
      break;
    }
  }

  let currentCol = col;
  while (currentCol < map[0].length - 1) {
    currentCol++;
    visibleTrees.right++;
    if (treeHeight <= getTreeHeight(row, currentCol, map)) {
      isVisibleFromRight = false;
      break;
    }
  }

  currentCol = col;
  while (currentCol > 0) {
    currentCol--;
    visibleTrees.left++;
    if (treeHeight <= getTreeHeight(row, currentCol, map)) {
      isVisibleFromLeft = false;
      break;
    }
  }

  return (
    visibleTrees.left *
    visibleTrees.top *
    visibleTrees.right *
    visibleTrees.bottom
  );
};

const solvePuzzle2 = () => {
  const allTrees = readFileToArray("input.txt");

  let highScore = -1;
  for (let i = 0; i < allTrees.length; i++) {
    for (let j = 0; j < allTrees[0].length; j++) {
      const score = getScenicScore(i, j, allTrees);
      if (score > highScore) highScore = score;
    }
  }
  console.log(highScore);
};
solvePuzzle2();
