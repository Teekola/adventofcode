from time import perf_counter as pfc

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
    # Use as a stack
    expected = []

    # Iterate through indexes from 0 to end
    for i in range(len(line)):
        if line[i] in [')', ']', '}', '>']:
            # If the expected closing bracket is current bracket, remove expected from the expected list, otherwise we have illegal bracket
            if expected[-1] == line[i]:
                expected.pop()
            else: return line[i]
        else:
            # Add the current opening bracket's closer as expected bracket
            expected.append(flipBracket(line[i]))

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



# Part 2

def findCompletionString(line) -> str:
    # Create a stack of expected closing brackets
    expected = []

    for i in range(len(line)):
        if line[i] in [')', ']', '}', '>']:
            # If the expected closing bracket is current bracket, remove expected from the expected list
            if expected[-1] == line[i]:
                expected.pop()
        else:
            # Add the current opening bracket's closer as expected bracket
            expected.append(flipBracket(line[i]))
            
    # Return the expected ones in reverse order as a string
    return "".join(expected)[::-1]

def scoreCompletionString(completionString) -> int:
    score = 0
    for char in completionString:
        score *= 5
        score += [')', ']', '}', '>'].index(char) + 1
    return score

"""
Find the completion string for each incomplete line and add them to a list
score the completion strings in the list
sort the scores
return the middle score
"""
def solvePuzzle2(puzzleInput) -> int:
    lines = readInput(puzzleInput)

    # Remove incomplete lines
    lines =  [line for line in lines if firstIllegalCharacter(line) == '']
    
    # Add completion strings of each line to a list
    completion_strings = []
    for line in lines:
        completion_strings.append(findCompletionString(line))

    # Score the completion strings in the list
    completion_scores = [scoreCompletionString(completionString) for completionString in completion_strings]

    # Sort the scores
    completion_scores.sort()

    return completion_scores[len(completion_scores) // 2]


if __name__ == "__main__":
    start_time = pfc()
    print(solvePuzzle("input10.txt"))
    print(pfc() - start_time)

    start_time = pfc()
    print(solvePuzzle2("input10.txt"))
    print(pfc() - start_time)