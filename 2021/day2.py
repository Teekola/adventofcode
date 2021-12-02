from time import perf_counter as pfc

def readInput(fileName):
    with open(fileName, "r") as file:
        lines = file.read().split("\n")
        lines = [line.strip() for line in lines]

        # Create a tuple list from the input
        tuples = []
        for line in lines:
            (dir, amount) = line.split(" ")
            tuples.append((dir, int(amount)))

        return tuples


# Solution for Part 1
def solvePuzzle(puzzleInput) -> int:
    # Read input
    tuples = readInput(puzzleInput)

    # Initialize variables for horizontal position and depth
    hpos = 0
    depth = 0

    # Calculate horizontal position and depth after instructions
    for pair in tuples:
        if pair[0] == "forward":
            hpos += pair[1]
        elif pair[0] == "down":
             depth += pair[1]
        else:
            depth -= pair[1]

    # Multiply the result
    return hpos * depth

# Solve the puzzle and count the time
start_time = pfc()
print(solvePuzzle("input2.txt"))
print(pfc()-start_time)


# Solution for Part 2
def solvePuzzle2(puzzleInput) -> int:
    # Read input
    tuples = readInput(puzzleInput)

    # Initialize variables for horizontal position, depth and aim
    hpos = 0
    depth = 0
    aim = 0

    # Calculate horizontal position and depth after instructions
    for pair in tuples:
        if pair[0] == "forward":
            hpos += pair[1]
            depth += aim * pair[1]
        elif pair[0] == "down":
            aim += pair[1]
        else:
            aim -= pair[1]

    # Multiply the result
    return hpos * depth

# Solve the puzzle and count the time
start_time = pfc()
print(solvePuzzle2("input2.txt"))
print(pfc()-start_time)