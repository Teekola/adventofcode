from time import perf_counter as pfc
import heapq
from collections import defaultdict


def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    
    # Create a matrix
    risk_map = [[int(i) for i in line] for line in lines]
    return risk_map

# Dijkstra's algorithm
def findLowestRiskPath(risk_map):
    # Create a cost dictionary with initial zeroes
    cost_dict = defaultdict(int)

    # Keep track of each points (cost, row, column) in a priorityQueue
    priorityQueue = [(0, 0, 0)]
    heapq.heapify(priorityQueue)

    # Store visited points that have smallest possible distance to reach them found
    visited = set()

    # Iterate through the priority queue while there are points left in it
    while len(priorityQueue) > 0:
        # Remove the point with highest cost from the priority queue and get its stored values (cost, row, column)
        cost, row, col = heapq.heappop(priorityQueue)

        # If we have already visited a point continue to next (the point can not be efficient if it has been visited already)
        if (row, col) in visited:
            continue

        # Mark the point as visited
        visited.add((row, col))

        # Update the cost to the cost_array
        cost_dict[(row, col)] = cost

        # If we have reached the end, break
        if row == len(risk_map) - 1 and col == len(risk_map[0]) - 1:
            break
        
        # Check points in all possible directions and add them to the priority queue
        for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row = row + drow
            next_col = col + dcol

            # If the point is not in the map area, skip and continue
            if not (0 <= next_row < len(risk_map) and 0 <= next_col < len(risk_map[0])):
                continue
            
            # Get the risk value (cost) of the point and add to the priority queue
            heapq.heappush(priorityQueue, (cost + risk_map[next_row][next_col], next_row, next_col))
    
    # Return the bottomright corner points cost value in the cost dict
    return cost_dict[len(risk_map)-1, len(risk_map[0])-1]

def solvePuzzle(puzzleInput) -> int:
    risk_map = readInput(puzzleInput)

    risk_value = findLowestRiskPath(risk_map)

    return risk_value



def getCostValue(risk_map, row, col):
    N = len(risk_map)
    M = len(risk_map[0])
    # Get the correct value
    x = (risk_map[row % N][col % M] + (row // N) + (col // M))
    # 9 becomes one
    cost = (x - 1) % 9 + 1
    return cost


def findLowestRiskPath2(risk_map):
    N = len(risk_map) * 5
    M = len(risk_map[0]) * 5
    # Create a cost dictionary with initial zeroes
    cost_dict = defaultdict(int)

    # Keep track of each points (cost, row, column) in a priorityQueue
    priorityQueue = [(0, 0, 0)]
    heapq.heapify(priorityQueue)

    # Store visited points that have smallest possible distance to reach them found
    visited = set()

    # Iterate through the priority queue while there are points left in it
    while len(priorityQueue) > 0:
        # Remove the point with highest cost from the priority queue and get its stored values (cost, row, column)
        cost, row, col = heapq.heappop(priorityQueue)

        # If we have already visited a point continue to next (the point can not be efficient if it has been visited already)
        if (row, col) in visited:
            continue

        # Mark the point as visited
        visited.add((row, col))

        # Update the cost to the cost_array
        cost_dict[(row, col)] = cost

        # If we have reached the end, break
        if row == N - 1 and col == M - 1:
            break
        
        # Check points in all possible directions and add them to the priority queue
        for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_row = row + drow
            next_col = col + dcol

            # If the point is not in the map area, skip and continue
            if not (0 <= next_row < N and 0 <= next_col < M):
                continue
            
            # Get the risk value (cost) of the point and add to the priority queue
            heapq.heappush(priorityQueue, (cost + getCostValue(risk_map, next_row, next_col), next_row, next_col))
    
    # Return the bottomright corner points cost value in the cost dict
    return cost_dict[N-1, M-1]

def solvePuzzle2(puzzleInput) -> int:
    risk_map = readInput(puzzleInput)

    risk_value = findLowestRiskPath2(risk_map)

    return risk_value

if __name__ == '__main__':
    start_time = pfc()
    print(solvePuzzle("input15.txt"))
    print(pfc() - start_time)

    start_time = pfc()
    print(solvePuzzle2("input15.txt"))
    print(pfc() - start_time)
    



# Failed try
"""
On every step, we can move to right or down
Backgtracking: For every position, if we have already reached it with lesser risk value, discard and try another

store visited points in a set()
store the minimum risk value taken to reach a point in a dict


start from topleft with riskvalue 0

if we have reached bottomright-corner, return risk-value
try to go right and down

if the point is in visited:
    if the total risk value to reach a point is greater than previous, discard
    elif it's the same continue
    elif it's smaller, update risk value to be the current and continue
else add the point to visited and update the risk value to reach it to be the current risk value, then continue from the point

def findLowestRiskPath(risk_map, visited=set(), points_risk_values=dict(), risk_value=0, point=(0, 0)) -> int:
    # Base case: we have reached the bottom right corner
    if (point[0] == len(risk_map[0])-1 and point[1] == len(risk_map)-1):
        print(point, risk_value)
        return risk_value, visited

    # Try right
    if point[0] + 1 < len(risk_map[0]):

        # Test the point on the right
        test_point = (point[0] + 1, point[1])
        
        # Get the risk value of the point from the risk_map and add it to the current risk value
        right_point_value = risk_map[test_point[1]][test_point[0]]
        risk_value += right_point_value

        # If the test point has been visited, 
        if test_point in visited:

            # check if we have reached the point with lesser or equal risk
            if points_risk_values.get(test_point) >= risk_value:

                # Update the risk value needed to reach the point
                points_risk_values[test_point] = risk_value

                # Continue searching the path from the point
                findLowestRiskPath(risk_map, visited, points_risk_values, risk_value, test_point)

            # If the risk to reach the point was higher
            else:
                # Go back from the point
                risk_value -= right_point_value

        # If the test point has not been visited
        else:
            # Add the point to visited points
            visited.add(test_point)

            # Add the risk value to reach the point
            points_risk_values[test_point] = risk_value

            # Continue searching from the new point
            findLowestRiskPath(risk_map, visited, points_risk_values, risk_value, test_point)

    # Try down
    if point[1] + 1 < len(risk_map):

        # Test the point down
        test_point = (point[0], point[1] + 1)

        # Get the risk value of the point from the risk_map and add it to the current risk value
        down_point_value = risk_map[test_point[1]][test_point[0]]
        risk_value += down_point_value

        # If the test point has been visited,
        if test_point in visited:

            # Check if we have reached the point with lesser or equal risk
            if points_risk_values.get(test_point) >= risk_value:

                # Update the risk value needed to reach the point
                points_risk_values[test_point] = risk_value

                # Continue searching the path from the point
                findLowestRiskPath(risk_map, visited, points_risk_values, risk_value, test_point)

            # If the risk to reach the point was higher
            else:
                # Go back from the point
                risk_value -= down_point_value
        
        # If the test point has not been visited,
        else:
            # Add the point to visited points
            visited.add(test_point)

            # Add the risk value to reach the point
            points_risk_values[test_point] = risk_value

            # Continue searching from the new point
            findLowestRiskPath(risk_map, visited, points_risk_values, risk_value, test_point)

"""