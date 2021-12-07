from os import read
from time import perf_counter as pfc

def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.read()
    positions = lines.split(",")
    positions = [int(x) for x in positions]

    return positions


# Part 1
def calculateFuelUsage(positions, targetPosition) -> int:
    fuelUsed = 0
    for pos in positions:
        fuelUsed += abs(pos - targetPosition)
    return fuelUsed

def solvePuzzle(puzzleInput) -> int:
    positions = readInput(puzzleInput)

    # Calculate the average position
    avg = sum(positions) // len(positions)

    previousTarget = avg
    previousUsage = calculateFuelUsage(positions, avg)
    currentUsage = 0

    # Get fuel values when going to higher values from average
    while True:
        currentUsage = calculateFuelUsage(positions, previousTarget - 1)
        previousTarget = previousTarget - 1
        if currentUsage > previousUsage:
            currentUsage = previousUsage
            break
        previousUsage = currentUsage

    # Get fuel values when going to lower values from average
    while True:
        currentUsage = calculateFuelUsage(positions, previousTarget + 1)
        previousTarget = previousTarget + 1
        if currentUsage > previousUsage:
            currentUsage = previousUsage
            break
        previousUsage = currentUsage
    
    return currentUsage

start_time = pfc()
print(solvePuzzle("input7.txt"))
print(pfc() - start_time)


# Part 2
def calculateFuelUsage2(positions, targetPosition) -> int:
    fuelUsed = 0
    for pos in positions:
        # Get the distance
        absoluteValue = abs(pos - targetPosition)

        # Calculate the sum of 1 + 2 +... absoluteValue
        sumToAdd = sum([i for i in range(1, absoluteValue + 1)])

        # Increase the amount of fuel used
        fuelUsed += sumToAdd
    return fuelUsed

def solvePuzzle2(puzzleInput) -> int:
    positions = readInput(puzzleInput)

    # Calculate the average position
    avg = sum(positions) // len(positions)

    # Set the average value as previousTarget
    previousTarget = avg

    # Set previous fuel usage to the fuel usage at average
    previousUsage = calculateFuelUsage2(positions, avg)

    # Initialize current usage to 0
    currentUsage = 0

    # Get fuel values when going to higher values from average
    while True:
        currentUsage = calculateFuelUsage2(positions, previousTarget - 1)
        previousTarget = previousTarget - 1
        if currentUsage > previousUsage:
            currentUsage = previousUsage
            break
        previousUsage = currentUsage

    # Get fuel values when going to lower values from average
    while True:
        currentUsage = calculateFuelUsage2(positions, previousTarget + 1)
        previousTarget = previousTarget + 1
        if currentUsage > previousUsage:
            currentUsage = previousUsage
            break
        previousUsage = currentUsage
    
    return currentUsage

start_time = pfc()
print(solvePuzzle2("input7.txt"))
print(pfc() - start_time)