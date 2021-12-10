from time import perf_counter as pfc

def readInput(fileName) -> list:
    with open(fileName, 'r') as file:
        rows = file.read()
    rows = rows.split("\n")
    # Transform each row into an integer list
    rows = [[int(i) for i in list(x)] for x in rows]
    return rows

# Part 1

def checkLowPoint(row, col, map) -> bool:
    col_amount = len(map[0])
    row_amount = len(map)

    # Check that the point (row, col) is not in first or last column
    if col >= 1 and col <= col_amount - 2:

        # Case middlerow
        if row >= 1 and row <= row_amount - 2:
            # min(left, right, up, down) > current
            if min(map[row][col - 1], map[row][col + 1], map[row - 1][col], map[row + 1][col]) > map[row][col]:
                return True

        # Case first row
        elif row == 0:
            # min(left, right, down) > current
            if min(map[0][col - 1], map[0][col + 1], map[1][col]) > map[0][col]:
                return True

        # Case last row
        elif row == row_amount - 1:
            # min(left, right, up) > current
            if min(map[row_amount - 1][col - 1], map[row_amount - 1][col + 1], map[row_amount - 2][col]) > map[row_amount - 1][col]:
                return True

    # Case first column
    elif col == 0:

        # Case middlerow
        if row >= 1 and row <= row_amount - 2:
            # min(right, up, down) > current
            if min(map[row][1], map[row - 1][0], map[row + 1][0]) > map[row][0]:
                return True

        # Case first row
        elif row == 0:
            # min(right, down) > current
            if min( map[0][1], map[1][0]) > map[0][0]:
                return True

        # Case last row
        elif row == row_amount - 1:
            # min(right, up) > current
            if min(map[row_amount - 1][1], map[row_amount - 2][0]) > map[row_amount - 1][0]:
                return True

    # Case last column
    elif col == col_amount - 1:

        # Case middlerow
        if row >= 1 and row <= row_amount - 2:
            # min(up, down, left) > current
            if min(map[row - 1][col_amount - 1], map[row + 1][col_amount - 1], map[row][col_amount - 2]) > map[row][col_amount - 1]:
                return True

        # Case first row
        elif row == 0:
            # min(down, left) > current
            if min(map[1][col_amount - 1], map[0][col_amount - 2]) > map[0][col_amount - 1]:
                return True

        # Case last row
        elif row == row_amount - 1:
            # min(left, up) > current
            if min(map[row_amount - 1][col_amount - 2], map[row_amount - 2][col_amount - 1]) > map[row_amount - 1][col_amount - 1]:
                return True
    
    return False




def solvePuzzle(puzzleInput) -> int:
    map = readInput(puzzleInput)

    # Iterate through the rows and columns
    risklevelSum = 0
    for row in range(len(map)):
        for col in range(len(map[0])):
            # If the current point (row, col) is lowPoint, increase the riskLevelSum
            if checkLowPoint(row, col, map):
                risklevelSum += map[row][col] + 1

    return risklevelSum

start_time = pfc()
print(solvePuzzle("input9.txt"))
print(pfc() - start_time)


def calculateBasinSize(row, col, map, checked) -> int:
    # Base case, out of bounds, has been checked or the value is 9 (add 0)
    if row < 0 or row >= len(map) or col < 0 or col >= len(map[0]) or (row, col) in checked or map[row][col] == 9:
        return 0
    else:
        # Add the point to checked
        checked.add((row, col))
        # Add all to the down, up, right and left
        return (1 + calculateBasinSize(row+1, col, map, checked) + calculateBasinSize(row-1, col, map, checked) + calculateBasinSize(row, col+1, map, checked) + calculateBasinSize(row, col-1, map, checked))


def solvePuzzle2(puzzleInput) -> int:
    map = readInput(puzzleInput)

    three_biggest = [-1, -1, -1]
    checked = set()
    # Iterate through the map
    for row in range(len(map)):
        for col in range(len(map[0])):
            # If the current point (row, col) is lowpoint, calculate it's basin size
            if checkLowPoint(row, col, map):
                basin_size = calculateBasinSize(row, col, map, checked)
                if basin_size > min(three_biggest):
                    # Remove the smallest element from the three_biggest and add new the basin_size to the list
                    three_biggest.remove(min(three_biggest))
                    three_biggest.append(basin_size)
                   

    # Multiply the three biggest basins
    return three_biggest[0] * three_biggest[1] * three_biggest[2]

start_time = pfc()
print(solvePuzzle2("input9.txt"))
print(pfc() - start_time)