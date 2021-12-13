from time import perf_counter as pfc

def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.read()
    
    lines = lines.split("\n\n")

    dots = lines[0].split("\n")
    instructions = lines[1].split("\n")

    dots = [(int(string.split(",")[0]), int(string.split(",")[1])) for string in dots]
    instructions = [(string.split("=")[0][-1], int(string.split("=")[1])) for string in instructions]

    return set(dots), instructions


"""
Taitetaan y=a kohdalta:
=> horisontaalinen taitos
=> jos x > a
        poista piste joukosta set.remove()
        laske etäisyys taittokohtaan a
        uusi x-koordinaatti on taittokohta - etäisyys a:sta
        lisää piste joukkoon set.add()
"""

def flipAlongX(dot: tuple, dots: set, axis_value: int) -> set:
    # Copy the set to prevent side effects
    dots_copy = dots.copy()

    # Remove the original dot
    dots_copy.remove(dot)

    # Get the new x-coordinate for the dot
    distance = dot[0] - axis_value
    new_x = axis_value - distance

    # Add the flipped dot to the set
    dot = (new_x, dot[1])
    dots_copy.add(dot)

    return dots_copy

def flipAlongY(dot: tuple, dots: set, axis_value: int) -> set:
    # Copy the set to prevent side effects
    dots_copy = dots.copy()

    # Remove the original dot
    dots_copy.remove(dot)

    # Get the new y-coordinate for the dot
    distance = dot[1] - axis_value
    new_y = axis_value - distance

    # Add the flipped dot to the set
    dot = (dot[0], new_y)
    dots_copy.add(dot)

    return dots_copy


# Part 1
def solvePuzzle(puzzleInput) -> int:
    dots, instructions = readInput(puzzleInput)
    instruction = instructions[0]
    
    axis = instruction[0]
    axis_value = instruction[1]

    if axis == 'x':
        # Iterate through all dots
        for dot in dots:
            # If x > axis value, flip the point
            if dot[0] > axis_value:
                dots = flipAlongX(dot, dots, axis_value)
    elif axis == 'y':
        # Iterate through all dots
        for dot in dots:
            # If y > axis value, flip the point
            if dot[1] > axis_value:
                dots = flipAlongY(dot, dots, axis_value)

    return len(dots)


def drawPaper(dots):
    # Get max and min values from random point and add the point back
    random = dots.pop()
    dots.add(random)
    max_x = random[0]
    min_x = random[0]
    for dot in dots:
        if dot[0] > max_x:
            max_x = dot[0]
        elif dot[0] < min_x:
            min_x = dot[0]

    max_y = random[1]
    min_y = random[1]
    for dot in dots:
        if dot[1] > max_y:
            max_y = dot[1]
        elif dot[1] < min_y:
            min_y = dot[1]
    
    # Generate a matrix to draw the dots
    matrix = []
    for _ in range(min_y, max_y+1):
        items = []
        for _ in range(min_x, max_x+1):
            items.append('.')
        matrix.append(items)

    # Add the dots to the matrix
    for dot in dots:
        matrix[dot[1]][dot[0]] = "#"
    
    # Print the matrix
    for row in matrix:
        print("".join(row))

# Part2
def solvePuzzle2(puzzleInput) -> int:
    dots, instructions = readInput(puzzleInput)

    for instruction in instructions:

        # Get the axis and the axis position
        axis = instruction[0]
        axis_value = instruction[1]

        if axis == 'x':
            # Iterate through all dots
            for dot in dots:
                # If x > a, flip the point
                if dot[0] > axis_value:
                    dots = flipAlongX(dot, dots, axis_value)
        elif axis == 'y':
            # Iterate through all dots
            for dot in dots:
                # If y > a, flip the point
                if dot[1] > axis_value:
                    dots = flipAlongY(dot, dots, axis_value)
    # Draw the paper
    drawPaper(dots)

        
if __name__ == "__main__":
    start_time = pfc()
    print(solvePuzzle("input13.txt"))
    print(pfc() - start_time)

    start_time = pfc()
    solvePuzzle2("input13.txt")
    print(pfc() - start_time)