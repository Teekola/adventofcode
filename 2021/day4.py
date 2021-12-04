from time import perf_counter as pfc

def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.read()
        lines = lines.split("\n")

        # Get the draw order
        draw_order = lines[0].split(",")
        draw_order = [ int(num) for num in draw_order ]

        # Get a list of lists that contain the different boards
        boards_list = []
        board = []
        for i in range(2, len(lines)):
            if lines[i] != '':
                # Create a line list without spaces
                line = lines[i].strip().split()
                for char in line:
                    if char == '':
                        line.remove(char)

                # Chars to int
                line = [ int(x) for x in line ]

                board.append(line)
            else:
                boards_list.append(board)
                board = []
        # Add the last board
        boards_list.append(board)

    return draw_order, boards_list


# Check if the board has won
def checkWinCondition(board, marked_numbers) -> bool:
    # Check for horizontal wins
    for row in board:
        bingo = True
        for number in row:
            # If a number is not marked, there is no bingo on the row
            if number not in marked_numbers:
                bingo = False
                break
        
        # If there is a bingo on a horizontal row, the board has already won
        if bingo:
            return True
    
    # Check for vertical wins
    for i in range(5):
        bingo = True
        for j in range(5):
            if board[j][i] not in marked_numbers:
                bingo = False
                break
        if bingo:
            return True

    # If there was no bingo, return false
    return False

# Calculate the score for the board
def calculateBoardScore(board, marked_numbers, win_number) -> int:
    unmarked_numbers = set()

    # Remove the marked numbers from the list and add them to unmarked_numbers
    for row in board:
        unmarked_numbers = set(row).difference(marked_numbers).union(unmarked_numbers)
    
    # Return the sum of unmarked numbers and multiply with the winning number
    return sum(unmarked_numbers) * win_number


# Solution for Part 1
def solvePuzzle(puzzleInput) -> int:
    # Read input
    draw_order, boards = readInput(puzzleInput)

    # Create a marked number list for each board
    boards_marked = []
    for i in range(len(boards)):
        boards_marked.append(set())

    
    # Helpers for the loop
    numbers_drawn = 0
    board_has_won = False
    win_score = -1

    # Iterate through the numbers in draw_order
    for drawn_number in draw_order:

        # If the board has won, break out of the outer loop
        if board_has_won: break

        # Iterate through the boards
        for i in range(len(boards)):

            # Mark the drawn number to the board by adding it to the set of drawn numbers for the board
            board = boards[i]
            boards_marked[i].add(drawn_number)

            # Check if the board has won
            if numbers_drawn >= 5:
                board_has_won = checkWinCondition(board, boards_marked[i])
            
            # If the board has won, calculate the score and break out of the inner loop
            if board_has_won: 
                win_score = calculateBoardScore(board, boards_marked[i], drawn_number)
                break

        numbers_drawn += 1
            
    return win_score


start_time = pfc()
print(solvePuzzle("input4.txt"))
print(pfc() - start_time)




# Solution for Part 2: Took way too long to make, eventually made a slow solution that works
def solvePuzzle2(puzzleInput) -> int:
    # Read input
    draw_order, boards = readInput(puzzleInput)

    while len(boards) > 1:
        # Create a marked number list for each board
        boards_marked = []
        for i in range(len(boards)):
            boards_marked.append(set())

        
        # Helpers for the loop
        numbers_drawn = 0
        board_has_won = False
        win_score = -1

        # Iterate through the numbers in draw_order
        for drawn_number in draw_order:

            # If the board has won, break out of the outer loop
            if board_has_won: break

            # Iterate through the boards
            for i in range(len(boards)):

                # Mark the drawn number to the board by adding it to the set of drawn numbers for the board
                board = boards[i]
                boards_marked[i].add(drawn_number)

                # Check if the board has won
                if numbers_drawn >= 5:
                    board_has_won = checkWinCondition(board, boards_marked[i])
                
                # If the board has won, calculate the score and break out of the inner loop
                if board_has_won: 
                    boards.pop(i)
                    break

            numbers_drawn += 1

    # Get the win score for the last board
    numbers_drawn = 0
    marked = set()
    board_has_won = False
    win_score = -1
    for drawn_number in draw_order:
        marked.add(drawn_number)
        if numbers_drawn >= 5:
            board_has_won = checkWinCondition(boards[0], marked)

        if board_has_won: 
            win_score = calculateBoardScore(boards[0], marked, drawn_number)
            break
        numbers_drawn += 1

    return win_score

start_time = pfc()
print(solvePuzzle2("input4.txt"))
print(pfc() - start_time)