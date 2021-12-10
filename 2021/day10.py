from time import perf_counter as pfc


"""
Calculate the error score
=> Calculate the sum of the syntax scores of corrupted lines
=> find the syntax score for each corrupted line
=> check if a line is corrupted and then calculate its score
=> check if a line is corrupted and get its score based on the first illegal character
"""

def readInput(fileName: str) -> list:

    with open(fileName, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]

    return lines


def flipBracket(char):
    open = ['(', '[', '{', '<']
    close = [')', ']', '}', '>']

    if char in open:
        return close[open.index(char)]
    else:
        return open[close.index(char)]

def getCharacterScore(char: chr) -> int:
    return 3 if char == ')' else 57 if char == ']' else 1197 if char == '}' else 25137


def firstIllegalCharacter(line) -> chr:
    for i in range(len(line)):
        if line[i] in [')', ']', '}', '>']:
            # Go through characters before line[i]
            for j in range(i, -1, -1):
                print(i, j)

    return ''



def solvePuzzle(puzzleInput) -> int:
    lines = readInput(puzzleInput)

    # Store error characters
    error_chars = []

    # Go through the lines and add first illegal char of each line to error_chars
    for line in lines:
        error_char = firstIllegalCharacter(line)
        if error_char != '':
            error_chars.append(error_char)

    # Calculate the total syntax error
    error_chars = [getCharacterScore(char) for char in error_chars]

    return sum(error_chars)


if __name__ == "__main__":
    start_time = pfc()
    print(solvePuzzle("input10.txt"))
    print(pfc() - start_time)