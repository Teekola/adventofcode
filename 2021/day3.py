from time import perf_counter as pfc

def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.read()
    lines = lines.split("\n")
    lines = [line.strip() for line in lines]

    return lines


# Returns the most frequent number out of 1 and 0 at number[index] out of all numbers
def getMostFrequent(index, numbers)-> int:
    zeros = 0
    ones = 0
    for number in numbers:
        if number[index] == "1":
            ones += 1
        else:
            zeros += 1
    
    return 1 if ones > zeros else 0


# Solution for Part 1
def solvePuzzle(puzzleInput) -> int:
    numbers = readInput(puzzleInput)

    length = len(numbers[0])

    gamma_rate = 0
    epsilon_rate = 0

    # Iterate as many times as there are digits in the binary number
    for index in range(0, length):
        # Get the most frequent number and add to the gamma_rate
        mostFrequent = getMostFrequent(index, numbers)
        gamma_rate += mostFrequent * 2**(length-1 - index)

        # Get the least frequent number and add to the epsilon_rate
        leastFrequent = 0 if mostFrequent == 1 else 1
        epsilon_rate += leastFrequent * 2**(length-1 - index)

    # Return the product of gamma_rate and epsilon_rate
    return gamma_rate * epsilon_rate

start_time = pfc()
print(solvePuzzle("input3.txt"))
print(pfc() - start_time)



def BinaryToDecimal(binary: str) -> int:
    decimal = 0
    length = len(binary)

    for i in range(length):
        decimal += int(binary[i]) * 2**(length-1-i)
    return decimal


def getOxygenFrequent(index, numbers)-> int:
    zeros = 0
    ones = 0
    for number in numbers:
        if number[index] == "1":
            ones += 1
        else:
            zeros += 1
    
    return 1 if ones >= zeros else 0

def getCO2Frequent(index, numbers)-> int:
    zeros = 0
    ones = 0
    for number in numbers:
        if number[index] == "1":
            ones += 1
        else:
            zeros += 1
    
    return 0 if zeros <= ones else 1

def determineOxygenGeneratorRating(numbers) -> int:
    # Copy the original list to prevent side-effects
    numlist = numbers.copy()
    
    # Iterate through digits
    for i in range(len(numlist[0])):
        # If length is 1, stop
        if len(numlist) == 1:
            break
        
        mostCommon = getOxygenFrequent(i, numlist)
        # filter out least common digits having numbers
        numlist = [ num for num in numlist if int(num[i]) == mostCommon ]

    return BinaryToDecimal(numlist[0])


def determineCO2ScrubberRating(numbers) -> int:
    # Copy the original list to prevent side-effects
    numlist = numbers.copy()
    
    # Iterate through digits
    for i in range(len(numlist[0])):
        # If lengths is 1, stop
        if len(numlist) == 1:
            break
        
        leastCommon = getCO2Frequent(i, numlist)
        # filter out most common digits having numbers
        numlist = [ num for num in numlist if int(num[i]) == leastCommon ]

    return BinaryToDecimal(numlist[0])


# Solution for Part 2
def solvePuzzle2(puzzleInput) -> int:
    numbers = readInput(puzzleInput)

    ox_rating = determineOxygenGeneratorRating(numbers)
    co2_rating = determineCO2ScrubberRating(numbers)

    return ox_rating * co2_rating

start_time = pfc()
print(solvePuzzle2("input3.txt"))
print(pfc() - start_time)