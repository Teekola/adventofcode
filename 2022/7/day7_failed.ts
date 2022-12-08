import fs from "fs";

const readFile = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  return file;
};

class File {
  dir: Directory;
  size: number;

  constructor(dir: Directory, size: string) {
    this.dir = dir;
    this.size = Number(size);
  }
}

class Directory {
  dir: Directory | null;
  items: (File | Directory)[];

  constructor(dir: Directory | null, items: (File | Directory)[]) {
    this.dir = dir;
    this.items = items;
  }

  public addItem(item: File | Directory) {
    this.items.push(item);
  }
}

const generateDirSet = (fileString: string) => {
  const lines = fileString.split("\r\n");
  let currentDir = new Directory(null, []);
  const tree = currentDir;
  for (const line of lines) {
    // Set new current directory
    if (line.startsWith("$ cd")) {
      if (line.includes("..")) {
        currentDir = currentDir.dir!;
      } else {
        currentDir = new Directory(currentDir, []);
        tree.addItem(currentDir);
      }
    }
    // Add new directory to current directory
    else if (line.startsWith("dir ")) {
      currentDir.addItem(new Directory(currentDir, []));
    }
    // Add new file to current directory
    else if (!line.startsWith("$ ls")) {
      const [size] = line.split(" ");
      currentDir.addItem(new File(currentDir, size));
    }
  }

  // Remove the first, empty dir
  return tree;
};

const MAX_SIZE = 100000;

const calculateSizeOfDir = (dir: Directory) => {
  const total = dir.items.reduce((prev, curr) => {
    let size = 0;
    if (curr instanceof File) {
      size = curr.size;
    } else {
      size = calculateSizeOfDir(curr);
    }
    return prev + size;
  }, 0);
  return total <= 100000 ? total : Infinity;
};

/* Works if the names of the directories are unique
const readFile = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8") + "\r\n$";
  return file;
};


const calculateSizeOfDir = (dirname: string, file: string, currentSize = 0) => {
  const dir = file
    .split("cd " + dirname + "\r\n$ ls\r\n")[1]
    .split("$")[0]
    .split("\r\n")
    .slice(0, -1);

  if (currentSize > MAX_SIZE) {
    return Infinity;
  }

  return dir.reduce((prev, curr) => {
    const [size, name] = curr.split(" ");

    let value = 0;
    if (size === "dir") {
      value = calculateSizeOfDir(name, file, currentSize);
    } else {
      value = Number(size);
    }
    currentSize += value;
    return prev + value;
  }, 0);
};

const solvePuzzle1 = () => {
  const file = readFile("input.txt");

  const dirnames = file
    .split("$ cd ")
    .slice(1)
    .map((cd) => cd.split("\r\n")[0])
    .filter((dir) => dir !== "..");

  const sizes = dirnames.map((dirname) => calculateSizeOfDir(dirname, file));

  const sum = sizes.reduce(
    (prev, curr) => (curr >= MAX_SIZE ? prev + 0 : prev + curr),
    0
  );
  console.log(sum);
};
solvePuzzle1();
*/

const solvePuzzle1 = () => {
  const fileString = readFile("input.txt");
  const tree = generateDirSet(fileString);
  const sizes = [] as number[];
  console.log(tree);

  const total = sizes.reduce(
    (prev, curr) => (curr > MAX_SIZE ? prev : prev + curr),
    0
  );

  console.log(total);
};
solvePuzzle1();

const solvePuzzle2 = () => {};
solvePuzzle2();
