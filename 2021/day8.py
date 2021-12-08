from time import perf_counter as pfc
from collections import Counter

def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.read()
        lines = lines.split("\n")

    outputlist = []
    for line in lines:
        output = line.split(" | ")[1]
        output = output.split(" ")
        outputlist.extend(output)
    return outputlist


def solvePuzzle(puzzleInput) -> int:
    outputs = readInput(puzzleInput)

    special_digits = 0
    for output in outputs:
        if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
            special_digits += 1
    
    return special_digits

start_time = pfc()
print(solvePuzzle("input8.txt"))
print(pfc() - start_time)

def determineConnections(input) -> list:
    foursandeights = []
    fouradded = False
    eightadded = False
    onesandsevens = []
    oneadded = False
    sevenadded = False
    threes = []
    threeadded = False

    for number in input:
        if len(foursandeights) < 3:
            if len(number) == 4 and not fouradded:
                foursandeights.append(number)
                fouradded = True
            elif len(number) == 7 and not eightadded:
                foursandeights.append(number)
                eightadded = True

        if len(onesandsevens) < 3:
            if len(number) == 2 and not oneadded:
                onesandsevens.append(number)
                oneadded = True
            elif len(number) == 3 and not sevenadded:
                onesandsevens.append(number)
                sevenadded = True

    # The index of 1 is the subtraction of set 7 from set 1
    set1 = set(onesandsevens[0])
    set2 = set(onesandsevens[1])
    one = list(set1.difference(set2))[0]
    threesix = set1.intersection(set2)

    # Remove set of one and three from numbers to get six
    sixes = set()
    for number in input:
        sixes.union(set(number).difference(set1).difference(set2))

    


    # Return from top to down left to right the wire identifiers in a list
    return one, threesix, sixes


def solvePuzzle2(puzzleInput) -> int:
    input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab".split(" ")

    four = determineConnections(input)


    return four


start_time = pfc()
print(solvePuzzle2("input8.txt"))
print(pfc() - start_time)