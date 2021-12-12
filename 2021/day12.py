from time import perf_counter as pfc
from collections import Counter

"""
Create a data structure Graph containing the start

Create a data structure Node containing reference to all connected nodes

"""


def readInput(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split("-") for line in lines]

    graph = dict()
    for nodelist in lines:
        # If the nodes have not been added to the graph, create a connectionlist for them
        if graph.get(nodelist[0], "not_found") == "not_found":
            graph[nodelist[0]] = set()
        if graph.get(nodelist[1], "not_found") == "not_found":
            graph[nodelist[1]] = set()
        
        # Add the connections to the node in the graph
        graph[nodelist[0]].add(nodelist[1])
        graph[nodelist[1]].add(nodelist[0])        

    return graph


def findPaths(graph, solutions=list(), path=["start"]) -> list:
    # Base case: If we have added end, add the path to the solutions list
    if path[-1] == 'end':
        solutions.append(path.copy())
    
    # Recursive case: If the last element in the path is not end
    else:

        # Go through the list of connections (nodes) of the last added element
        for node in graph[path[-1]]:

            # If we have a big cave or the node is not in the path
            if node.upper() == node or node not in path:

                # Add the node to the path
                path.append(node)

                # Find paths again until we have reached end, and store solutions to solutions
                solutions = findPaths(graph, solutions)

                # Remove 'end' (last element) from the path
                path.pop()

    return solutions
    
def oneSmallCaveTwice(path):
    smallCavesOnly = [node for node in path if node.upper() != node]
    return len(smallCavesOnly) - len(set(smallCavesOnly)) <= 1

def findPaths2(graph, solutions=list(), path=["start"]):
    # Base case: If we have added end, add the path to the solutions list
    if path[-1] == 'end':
        solutions.append(path.copy())

    # Recursive case: If the last element in the path is not end  
    else:

        # Go through the list of connections (nodes) of the last added element
        for node in graph[path[-1]]:
            
            # If we have a big cave or the node is not in the path or we have not visited a small cave twice
            if (node != 'start') and (oneSmallCaveTwice(path)) and \
               ((node.upper() == node) or (node not in path) or (path.count(node) < 2)):
                
                # Add the node to the path
                path.append(node)

                solutions = findPaths2(graph, solutions)

                # Remove 'end' from the path
                path.pop()
    
    return solutions



# Part 1: How many paths through this cave system are there that visit small caves at most once?
def solvePuzzle(puzzleInput) -> int:
    graph = readInput(puzzleInput)

    all_paths = findPaths(graph)
    return len(all_paths)

# Part 2
def solvePuzzle2(puzzleInput) -> int:
    graph = readInput(puzzleInput)

    all_paths = findPaths2(graph)
    return len(all_paths)

if __name__ == "__main__":
    start_time = pfc()
    print(solvePuzzle("input12.txt"))
    print(pfc() - start_time)

    start_time = pfc()
    print(solvePuzzle2("input12.txt"))
    print(pfc() - start_time)