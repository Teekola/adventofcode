from time import perf_counter as pfc

# Read input to a clean list
def readInput(filename):
    with open(filename, "r") as file:
        # Read the lines into a list
        lines = file.read()
        
        # Create a list of lines on line break
        lines = lines.split("\n")

        # Remove whitespace from lines
        lines = [int(line.strip()) for line in lines]
    return lines


## Iterate through the input and count and return the number of times a depth measurement increases
def solvePuzzle(puzzleInput):
    # Read file
    lines = readInput(puzzleInput)

    # Store the amount of increases
    increases = 0

    # Check if the value in the next index is greater than current and increase the counter if so
    for i in range(1, len(lines)):
        if (lines[i-1] < lines[i]):
            increases += 1
    return increases

# Get the function start time
start_time = pfc()

# Print the solution
print(solvePuzzle("input1.txt"))

# Print the solve time
print(pfc()-start_time)


## PART 2
def solvePuzzle2(puzzleInput):
    # Read file
    lines = readInput(puzzleInput)

    # Initialize counter
    increases = 0

    # Initialize the previous sum to first one
    sum_prev = lines[0] + lines[1] + lines[2]

    # Iterate through the list
    for i in range(1, len(lines)-2):

        # Calculate the sum of new 3 members
        sum_new = lines[i] + lines[i+1] + lines[i+2]

        # If the sum is bigger than previous, increase counter
        if (sum_new > sum_prev):
            increases += 1

        # Set the new sum to be the previous for next round
        sum_prev = sum_new

    return increases


start_time = pfc()
print(solvePuzzle2("input1.txt"))
print(pfc()-start_time)

## DIFFERENT (FASTER OR MORE ADVANCED) SOLUTIONS

def solvePuzzle1v2(puzzleInput) -> int:
    lines = readInput(puzzleInput)
    
    increases = 0

    # Create tuples of the consecutive members and check if the 2nd member is greater, if so, increase counter
    for i, j in zip(lines, lines[1:]):
        if j > i:
            increases += 1
    return increases

start_time = pfc()
print(solvePuzzle1v2("input1.txt"))
print(pfc()-start_time)



def solvePuzzle2v2(puzzleInput) -> int:
    lines = readInput(puzzleInput)
    
    increases = 0

    # Create a list to store all sums
    windows = []

    # Create the sums by zipping the lines list so that every 3 consecutive members will be in one case
    for i, j, k in zip(lines, lines[1:], lines[2:]):
        windows.append(i + j + k)

    # Create tuples of the consecutive members and check if the 2nd member is greater, if so, increase counter
    for i, j in zip(windows, windows[1:]):
        if j > i:
            increases += 1
    return increases


start_time = pfc()
print(solvePuzzle2v2("input1.txt"))
print(pfc()-start_time)