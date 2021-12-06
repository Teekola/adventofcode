from time import perf_counter as pfc

# Class used for part 1
class Lanternfish:
    # Timer has the value of the internal timer
    def __init__(self, timer: int):
        self.timer = timer
        self.new = True

    # Increase age by decreasing the timer, return a new Lanternfish when needed
    def grow(self):
        if self.timer == 0:
            self.timer = 6
            return Lanternfish(8)
        elif self.new:
            self.new = False
        else:
            self.timer -= 1
            return None

    def __str__(self):
        return str(self.timer)


# Read the input to a list of Lanterfish objects
def readInput(fileName):
    # Create a list of Lanternfish objects from the input
    with open(fileName, 'r') as file:
        start_list = file.read()
        start_list = start_list.split(",")
        start_list = [int(x) for x in start_list]
        start_list = [Lanternfish(x) for x in start_list]
    
    return start_list


# Part 1
def solvePuzzle(puzzleInput) -> int:

    fishlist = readInput(puzzleInput)

    # Iterate days
    for day in range(80 + 1):
        # Grow each fish
        for fish in fishlist:
            # If a new fish is created, add it to the list
            newfish = fish.grow()
            if isinstance(newfish, Lanternfish):
                fishlist.append(newfish)

    return len(fishlist)

start_time = pfc()
print(solvePuzzle("input6.txt"))
print(pfc() - start_time)



# Read the input to a dictionary
def readInput2(fileName) -> dict:
    with open(fileName, 'r') as file:
        fishlist = file.read()

    fishlist = fishlist.split(",")
    fishlist = [int(x) for x in fishlist]

    # Set  keys from 0 to 9 as 0 in fishdict
    fishdict = {}
    for i in range(9):
        fishdict[i] = 0
    
    # Add the amount of specific aged fish to the dict
    for fish in fishlist:
        fishdict[fish] += 1

    return fishdict


# Part 2
def solvePuzzle2(puzzleInput) -> int:
    fishdict = readInput2(puzzleInput)

    # Iterate through days
    for day in range(256):

        # Iterate through keys 0-8
        for key in range(9):
            
            # Shift the values of keys to left by one
            if 1 <= key <= 8:
                fishdict[key - 1] += fishdict[key]
                fishdict[key] = 0

            # Store the value of zeroes and set zeroes to 0
            elif key == 0:
                sum_of_zeroes = fishdict[0]
                fishdict[0] = 0
    
        # Set the value of 8s to the amount of zeroes and increase the value of 6s by the amount of zeroes
        fishdict[8] = sum_of_zeroes
        fishdict[6] += sum_of_zeroes

    return sum(fishdict.values())

start_time = pfc()
print(solvePuzzle2("input6.txt"))
print(pfc() - start_time)