import fs from "fs";

class Item {
  readonly name: string;
  readonly parent: Folder;
  constructor(parent: Folder, name: string) {
    this.parent = parent;
    this.name = name;
  }

  toString() {
    return this.name;
  }
}

interface Folder {
  readonly items: Item[];
  readonly name: string;
  addItem: (item: Item) => void;
}

class RootFolder implements Folder {
  name: string;
  items: Item[];
  constructor() {
    this.items = [];
    this.name = "/";
  }

  addItem(item: Item) {
    this.items.push(item);
  }

  public toString() {
    return this.name;
  }
}

class IFolder extends Item implements Folder {
  items: Item[];
  constructor(parent: Folder, name: string) {
    super(parent, name);
    this.items = [];
  }

  addItem(item: Item) {
    this.items.push(item);
  }

  public toString() {
    return this.name;
  }
}

class IFile extends Item {
  readonly size: number;
  constructor(parent: Folder, name: string, size: number) {
    super(parent, name);
    this.size = size;
  }
}

function cd(root: RootFolder, currentDir: Folder, folderName: string) {
  switch (folderName) {
    case "/":
      root = new RootFolder();
      //console.log("created root folder");
      currentDir = root;
      break;

    case "..":
      if (currentDir instanceof IFolder) {
        currentDir = currentDir.parent;
        //console.log("moved up to " + currentDir);
      } else {
        console.log("Already in root node");
      }
      break;

    // The folderName is an actual name of a folder.
    // The name should be already added to the currentDir's
    // items so we need to find it and set it as the new currentDir.
    default:
      currentDir = currentDir.items.find(
        (item) => item.name === folderName
      ) as IFolder;
      break;
  }
  return [root, currentDir];
}

function generateFileStructure(lines: string[]) {
  let root: RootFolder;
  let currentDir: Folder;
  lines.forEach((line) => {
    // Check if line is command
    if (line.startsWith("$")) {
      const [command, arg] = line.split("$ ")[1].split(" ");

      if (command.startsWith("cd")) {
        [root, currentDir] = cd(root, currentDir, arg);
      }
    }
    // If the line is not a command,
    // we have items from ls so we should
    // add the items to currentDir's items array
    else {
      const [size, name] = line.split(" ");

      if (size === "dir") {
        currentDir.addItem(new IFolder(currentDir, name));
      } else {
        currentDir.addItem(new IFile(currentDir, name, Number(size)));
      }
    }
  });
  return root!;
}

function calculateSizeOfFolder(folder: Folder): number {
  return folder.items.reduce((sum, curr) => {
    if (curr instanceof IFile) {
      return sum + curr.size;
    } else if (curr instanceof IFolder) {
      return sum + calculateSizeOfFolder(curr);
    }
    return sum;
  }, 0);
}

function addFoldersToArray(folder: Folder, folders: Folder[]) {
  folders.push(folder);
  folder.items.forEach((item) => {
    if (item instanceof IFolder) {
      addFoldersToArray(item, folders);
    }
  });
}

function solvePuzzle1() {
  const file = fs.readFileSync("input.txt", { encoding: "utf-8" });
  const lines = file.split("\r\n");
  const root = generateFileStructure(lines);
  const folders = [] as Folder[];
  addFoldersToArray(root, folders);
  const sizes = folders.map((folder) => calculateSizeOfFolder(folder));

  const sum = sizes.reduce(
    (sum, curr) => (curr > 100000 ? sum : sum + curr),
    0
  );
  console.log(sum);
}
solvePuzzle1();

function solvePuzzle2() {
  const file = fs.readFileSync("input.txt", { encoding: "utf-8" });
  const lines = file.split("\r\n");
  const root = generateFileStructure(lines);

  const currentSpace = 70000000 - calculateSizeOfFolder(root);
  const spaceToBeFreed = 30000000 - currentSpace;

  const folders = [] as Folder[];
  addFoldersToArray(root, folders);
  const sizes = folders.map((folder) => calculateSizeOfFolder(folder));
  const bigEnoughFolders = sizes.filter((size) => size >= spaceToBeFreed);
  const smallest = Math.min(...bigEnoughFolders);
  console.log(smallest);
}
solvePuzzle2();
