from time import perf_counter as pfc

class Octopus:
    flashed = False
    def __init__(self, energy_level: int):
        self.energy_level = energy_level
    
    def increaseEnergyLevel(self):
        if not self.flashed:
            self.energy_level += 1

            if self.energy_level > 9:
                self.flash()


    def flash(self):
        self.energy_level = 0
        self.flashed = True

    def __str__(self) -> str:
        return str(self.energy_level)


def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    lines = [list(line.strip()) for line in lines]
    lines = [[int(x) for x in line] for line in lines]

    # Create octopusmap from the lines
    lines = [[Octopus(x) for x in line] for line in lines]

    return lines


def increaseAdjacentEnergyLevels(octopuses, row, col, new_flash):
    # Increase all around
    for (r, c) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        # Skip if OB or flashed
        if row + r < 0 or col + c < 0 or row+r > len(octopuses)-1 or col+c > len(octopuses[0])-1 or octopuses[row+r][col+c].flashed: continue

        # Otherwise increase energylevel
        octopuses[row + r][col + c].increaseEnergyLevel()

        # If we got a new flash, add it to the set new_flash
        if octopuses[row + r][col + c].flashed:
            new_flash.add((row + r, col + c))
    
    # If there are points in new_flash, remove one and increase its adjacent octopuses' energy levels
    if len(new_flash) > 0:
        new_point = new_flash.pop()
        octopuses = increaseAdjacentEnergyLevels(octopuses, new_point[0], new_point[1], new_flash)
    
    return octopuses



def increaseEnergyLevels(octopuses) -> list:
    # Increase energylevel of each octopus by one
    for row in range(len(octopuses)):
        for col in range(len(octopuses[0])):
            octopuses[row][col].increaseEnergyLevel()

    # Add flashed octopuses to new_flash set
    new_flash = set()
    for row in range(len(octopuses)):
        for col in range(len(octopuses[0])):
            if octopuses[row][col].flashed:
                new_flash.add((row, col))

    # If there happened flashes, increase their adjacent octopuses' energy levels
    if len(new_flash) > 0:
        new_point = new_flash.pop()
        octopuses = increaseAdjacentEnergyLevels(octopuses, new_point[0], new_point[1], new_flash)

    return octopuses

def countFlashes(octopuses) -> int:
    flashes = 0
    # Count flashes and set flashed of each octopus that flashed to False at the end of the step
    for octopusrow in octopuses:
        for octopus in octopusrow:
            if octopus.flashed:
                flashes += 1
                octopus.flashed = False
    return octopuses, flashes

# Part 1
def solvePuzzle(puzzleInput) -> int:
    octopuses = readInput(puzzleInput)

    flashCount = 0
    for _ in range(100):
        # Increase energylevel of each octopus by 1 and flash octopuses with energy_level > 9
        octopuses = increaseEnergyLevels(octopuses)

        # Count flashed octopuses and set them not flashed
        octopuses, flashes = countFlashes(octopuses)
        flashCount += flashes

    #print("\n".join(["".join([str(o) for o in olist]) for olist in octopuses]))
    return flashCount

# Part 2
def solvePuzzle2(puzzleInput) -> int:
    octopuses = readInput(puzzleInput)
    step = 1
    while True:
        octopuses = increaseEnergyLevels(octopuses)
        octopuses, flashes = countFlashes(octopuses)

        if flashes == 100:
            break
        step += 1
    return step


if __name__ == "__main__":
    # Part 1
    start_time = pfc()
    print(solvePuzzle("input11.txt"))
    print(pfc() - start_time)

    # Part 2
    start_time = pfc()
    print(solvePuzzle2("input11.txt"))
    print(pfc() - start_time)