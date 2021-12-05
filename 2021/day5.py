from time import perf_counter as pfc
from collections import Counter

def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.read()
        lines = lines.split("\n")
        lines = [line.strip() for line in lines]
        
        # Create a list that contains lines as tuples of 2 tuples with the coordinates
        lines_coordinates = []
        for line in lines:
            start = line.split(" -> ")[0]
            start = tuple([int(start.split(",")[0]), int(start.split(",")[1])])
            end = line.split(" -> ")[1]
            end = tuple([int(end.split(",")[0]), int(end.split(",")[1])])
            lines_coordinates.append((start, end))

    return lines_coordinates

# Part 1
def solvePuzzle(puzzleInput) -> int:

    # Read input
    lines = readInput(puzzleInput)

    # Filter out such tuples where both coordinates change. Store proper lines to a new list
    proper_lines = []
    for line in lines:
        if line[0][0] == line[1][0]:
            proper_lines.append(line)
        elif line[0][1] == line[1][1]:
            proper_lines.append(line)

    # Add each coordinate to a list
    coordinates = []
    for line in proper_lines:
        
        start_x = line[0][0]
        end_x = line[1][0]
        start_y = line[0][1]
        end_y = line[1][1]

        if start_x == end_x:
            if start_y <= end_y:
                for y in range(start_y, end_y + 1):
                    coordinates.append((start_x, y))
            elif start_y > end_y:
                for y in range(end_y, start_y + 1):
                    coordinates.append((start_x, y))

        if start_y == end_y:
            if start_x <= end_x:
                for x in range(start_x, end_x + 1):
                    coordinates.append((x, start_y))
            elif start_x > end_x:
                for x in range(end_x, start_x + 1):
                    coordinates.append((x, start_y))

    # Count occurrences of elements to a dictionary using Counter
    amount_dict = Counter(coordinates)
    counter = 0

    # Count the number of coordinates with amount greater than 1
    for amount in amount_dict.values():
        if amount > 1:
            counter += 1

    # Naiive very slow solution
    """""
    overlapped_points = 0
    while len(coordinates) > 0:

        current = coordinates[0]
        current_amount = 0
        # Iterate through the list and count the number of times the specific coordinate is in the list
        for coordinate in coordinates:

            if coordinate == current:
                current_amount += 1

                # If the amount is greater than 1, there is overlapping, so increase the counter and break out of the loop
                if current_amount > 1:
                    overlapped_points += 1
                    break
        
        # Remove all of the instances of the current from the list
        coordinates = [coord for coord in coordinates if coord != current]
        print(coordinates)
    """
            

    return counter

start_time = pfc()
print(solvePuzzle('input5.txt'))
print(pfc() - start_time)



def solvePuzzle2(puzzleInput) -> int:
    # Read input
    lines = readInput(puzzleInput)

    

    # Add each coordinate to a list
    coordinates = []
    for line in lines:
        
        start_x = line[0][0]
        end_x = line[1][0]
        start_y = line[0][1]
        end_y = line[1][1]

        if start_x == end_x:
            if start_y <= end_y:
                for y in range(start_y, end_y + 1):
                    coordinates.append((start_x, y))
            elif start_y > end_y:
                for y in range(end_y, start_y + 1):
                    coordinates.append((start_x, y))

        if start_x < end_x and start_y < end_y:
            for i in range(0, end_x - start_x + 1):
                    coordinates.append((start_x + i, start_y + i))
                
        if start_x < end_x and start_y > end_y:
            for i in range(0, end_x - start_x + 1):
                    coordinates.append((start_x + i, start_y - i))
    
        if start_x > end_x and start_y < end_y:
            for i in range(0, end_y - start_y + 1):
                    coordinates.append((start_x - i, start_y + i))

        if start_x > end_x and start_y > end_y:
             for i in range(0, start_y - end_y + 1):
                    coordinates.append((start_x - i, start_y - i))
                
        if start_y == end_y:
            if start_x <= end_x:
                for x in range(start_x, end_x + 1):
                    coordinates.append((x, start_y))
            elif start_x > end_x:
                for x in range(end_x, start_x + 1):
                    coordinates.append((x, start_y))

    # Count occurrences of elements to a dictionary using Counter
    amount_dict = Counter(coordinates)
    counter = 0

    # Count the number of coordinates with amount greater than 1
    for amount in amount_dict.values():
        if amount > 1:
            counter += 1

    return counter


start_time = pfc()
print(solvePuzzle2('input5.txt'))
print(pfc() - start_time)