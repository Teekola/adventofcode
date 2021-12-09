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

def determineConnections(line) -> list:
    identifiers = line.split(" | ")[0].split(" ")
    ones = list([digit for digit in identifiers if len(digit) == 2][0])
    sevens = list([digit for digit in identifiers if len(digit) == 3][0])
    fours = list([digit for digit in identifiers if len(digit) == 4][0])
    eights = list([digit for digit in identifiers if len(digit) == 7][0])

    # Top can be determined by finding ones and sevens and choosing the one letter that is in only one of them
    top = list(set(sevens).difference(set(ones)))[0]

    # Middle and topleft can be determined by finding fours and removing sevens
    middletopleft = set(fours).difference(set(sevens))

    # By removing fours and top from eight we get bottom and bottomleft
    bottombottomleft = set(eights).difference(set(fours).union({top}))
    
    # We get bottom from the sixlongs by removing middletopleft
    sixlongs = [digit for digit in identifiers if len(digit) == 6]

    if len(set(list(sixlongs[0])).difference(middletopleft.union(set(sevens)))) == 1:
        bottom = list(set(list(sixlongs[0])).difference(middletopleft.union(set(sevens))))[0]
    elif len(set(list(sixlongs[1])).difference(middletopleft.union(set(sevens)))) == 1:
        bottom = list(set(list(sixlongs[1])).difference(middletopleft.union(set(sevens))))[0]
    else:
        bottom = list(set(list(sixlongs[2])).difference(middletopleft.union(set(sevens))))[0]

 
    # Bottomleft from bottombottomleft
    bottomleft = list(bottombottomleft.difference(set(bottom)))[0]

    # Find two from the fivelongs by removing bottomleft
    fivelongs = [digit for digit in identifiers if len(digit) == 5]
    two = set(list(fivelongs[0])) if len(set(list(fivelongs[0])).difference(bottomleft)) != 5 else set(list(fivelongs[1])) if len(set(list(fivelongs[1])).difference(bottomleft)) != 5 else set(list(fivelongs[2]))

    # Topright from the intersection of one and two
    topright = list(two.intersection(set(ones)))[0]

    # Bottomright from the difference of one and topright
    bottomright = list(set(ones).difference(set(topright)))[0]

    # Middle from two by removing topright, bottomleft, top and bottom
    middle = list(two.difference({topright, bottomleft, top, bottom}))[0]
    
    # Topleft from middletopleft by removing middle
    topleft = list(middletopleft.difference({middle}))[0]

    return [top, topleft, topright, middle, bottomleft, bottomright, bottom]



def decodeNumber(line, connections) -> int:
    digits = line.split(" | ")[1].split(" ")

    decoded_str = ""
    patterns = {
        "012456": 0,
        "25": 1,
        "02346": 2,
        "02356": 3,
        "1235": 4,
        "01356": 5,
        "013456": 6,
        "025": 7,
        "0123456": 8,
        "012356": 9
    }

    # Iterate through the digits
    for digit in digits:
        # Add the indexes of the wires from the connections list to wires
        wires = ""
        for char in digit:
            wires += str(connections.index(char))
        # Sort the wires and retrieve the correct digit that matches the pattern from the dictionary. Add it to the decoded str
        wires = sorted(wires)
        wires = "".join(wires)
        decoded_str += str(patterns[wires])

    return int(decoded_str)

def readInput2(fileName) -> list:
    with open(fileName, 'r') as file:
        lines = file.read()
    lines = lines.split("\n")
    return lines

def solvePuzzle2(puzzleInput) -> int:
    lines = readInput2(puzzleInput)

    # Iterate through lines
    sumOfNumbers = 0
    for line in lines:
        
        # Determine connections
        connections = determineConnections(line)

        # Decode the number using the connections
        decoded = decodeNumber(line, connections)

        # Add the number to the total sum
        sumOfNumbers += decoded

    return sumOfNumbers


start_time = pfc()
print(solvePuzzle2("input8.txt"))
print(pfc() - start_time)