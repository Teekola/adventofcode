import fs from "fs";

const readFile = (filename: string) => {
  const file = fs.readFileSync(filename, "utf-8");
  return file;
};

const parseInput = (file: string) => {
  return file.split("\r\n");
};

// PT 1

const OPPONENT_VALUES = {
  A: 1,
  B: 2,
  C: 3,
};

const PLAYER_VALUES = {
  X: 1,
  Y: 2,
  Z: 3,
};

const OUTCOME_VALUES = {
  L: 0,
  T: 3,
  W: 6,
};

const OUTCOME_VALUES2 = {
  X: 0,
  Y: 3,
  Z: 6,
};

const determineOutcome = (
  opponent: keyof typeof OPPONENT_VALUES,
  player: keyof typeof PLAYER_VALUES
) => {
  if (!Object.keys(OPPONENT_VALUES).includes(opponent))
    throw Error("Wrong opponent value");
  if (!Object.keys(PLAYER_VALUES).includes(player))
    throw Error("Wrong player value");

  if (opponent === "A") {
    if (player === "X") return "T";
    if (player === "Y") return "W";
    if (player === "Z") return "L";
  }

  if (opponent === "B") {
    if (player === "X") return "L";
    if (player === "Y") return "T";
    if (player === "Z") return "W";
  }
  if (opponent === "C") {
    if (player === "X") return "W";
    if (player === "Y") return "L";
    if (player === "Z") return "T";
  }
};

const rounds = parseInput(readFile("./input.txt"));

const calculateScore = () => {
  let score = 0;
  rounds.forEach((round) => {
    const keys = round.split(" ");
    const opponent = keys[0] as keyof typeof OPPONENT_VALUES;
    const player = keys[1] as keyof typeof PLAYER_VALUES;
    const outcome = determineOutcome(opponent, player);
    if (!outcome) return -1;
    score += PLAYER_VALUES[player] + OUTCOME_VALUES[outcome];
  });
  return score;
};
const score = calculateScore();
console.log(score);

// PT 2

const determinePlayer = (
  opponent: keyof typeof OPPONENT_VALUES,
  outcome: keyof typeof OUTCOME_VALUES2
) => {
  if (outcome === "Z") {
    if (opponent === "A") return PLAYER_VALUES.Y;
    if (opponent === "B") return PLAYER_VALUES.Z;
    if (opponent === "C") return PLAYER_VALUES.X;
  }
  if (outcome === "Y") {
    if (opponent === "A") return PLAYER_VALUES.X;
    if (opponent === "B") return PLAYER_VALUES.Y;
    if (opponent === "C") return PLAYER_VALUES.Z;
  }
  if (outcome === "X") {
    if (opponent === "A") return PLAYER_VALUES.Z;
    if (opponent === "B") return PLAYER_VALUES.X;
    if (opponent === "C") return PLAYER_VALUES.Y;
  }
};

const calculateScore2 = () => {
  let score2 = 0;
  rounds.forEach((round) => {
    const keys = round.split(" ");
    const opponent = keys[0] as keyof typeof OPPONENT_VALUES;
    const outcome = keys[1] as keyof typeof OUTCOME_VALUES2;

    const player = determinePlayer(opponent, outcome);
    if (!player) return -1;
    score2 += player + OUTCOME_VALUES2[outcome];
  });

  return score2;
};
const score2 = calculateScore2();
console.log(score2);
