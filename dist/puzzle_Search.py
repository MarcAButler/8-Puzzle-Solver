from queue import Queue, PriorityQueue
from time import time


################################################################
#                       BREADTH FIRST SEARCH                   #
################################################################
def breadth_first_search(puzzle_encoding):
    test_queue = Queue()
    test_queue.put(puzzle_encoding)
    # The queue should probably always have 8 characters in the string
    current_node = ""
    visited_set = {puzzle_encoding}

    goal = "12345678-"
    parent_node = None

    # Dictonary that contains all the nodes represented by the key-value pair of state and parent such as "12345678-" (node) and "1234567-8" (parent)
    nodePaths = { }
    rootNodePassed = False

    while not findPath(goal, current_node):

        # load the next element in the queue to return and remove it from the queue
        current_node_parent = test_queue.get()
       

        if type(current_node_parent) == tuple:

            current_node = current_node_parent[1]
            parent_node = current_node_parent[2]
        else:

            current_node = current_node_parent


        if current_node not in nodePaths:
            if rootNodePassed is False:
                nodePaths[current_node] = None
                rootNodePassed = True
            else:
                nodePaths[current_node] = parent_node

        parent_node = current_node

        possiblePaths_Parent = directionsToMove(current_node)


        for i in range(len(possiblePaths_Parent)):
            # Test if the possible path has been visited yet by comparing it to the set
            if possiblePaths_Parent[i] not in visited_set:
                test_queue.put(possiblePaths_Parent[i])
                visited_set.add(possiblePaths_Parent[i])


    # Since the dictonary has been generated we simply need to retrace our steps back to the root node--printing all the nodes inbetween!
    steps_to_take = [goal]
    curr_node = goal

    while nodePaths[curr_node] is not None:

        steps_to_take.append(nodePaths[curr_node])
        # Get he parent stored for that node
        curr_node = nodePaths[curr_node]

    # Reverses the steps_to_take list
    steps_to_take.reverse()

    print("Number of the steps to solution: ", len(steps_to_take))
    #print("Solution: ", steps_to_take)
   

    print("NODE PATHS: ", len(nodePaths))
    return steps_to_take


################################################################
#                       BEST FIRST SEARCH                      #
################################################################
def best_first_search(puzzle_encoding, heuristic_function):
    priorityQueue = PriorityQueue()
    priorityQueue.put(puzzle_encoding)

    # The queue should probably always have 8 characters in the string
    current_node = ""
    visited_set = {puzzle_encoding}

    goal = "12345678-"
    parent_node = None

    # Dictonary that contains all the nodes represented by the key-value pair of state and parent such as "12345678-" (node) and "1234567-8" (parent)
    nodePaths = { }
    rootNodePassed = False

    while not findPath(goal, current_node):

        # load the next element in the queue to return and remove it from the queue
        current_node_parent = priorityQueue.get()
       

        if type(current_node_parent) == tuple:
            #edge_weight = current_node_parent[0]
            current_node = current_node_parent[1]
            parent_node = current_node_parent[2]
        else:
            current_node = current_node_parent


        if current_node not in nodePaths:
            if rootNodePassed is False:
                nodePaths[current_node] = None
                rootNodePassed = True
            else:
                nodePaths[current_node] = parent_node

        parent_node = current_node
        
        possiblePaths_Parent = directionsToMove(current_node, heuristic_function)


        for i in range(len(possiblePaths_Parent)):
            # Test if the possible path has been visited yet by comparing it to the set
            if possiblePaths_Parent[i] not in visited_set:
                # Determine the weight of the edge of a particular node with a heuristicfunction
                priorityQueue.put(possiblePaths_Parent[i])
                visited_set.add(possiblePaths_Parent[i])


    # Since the dictonary has been generated we simply need to retrace our steps back to the root node--printing all the nodes inbetween!
    steps_to_take = [goal]
    curr_node = goal

    while nodePaths[curr_node] is not None:

        steps_to_take.append(nodePaths[curr_node])
        # Get he parent stored for that node
        curr_node = nodePaths[curr_node]

    # Reverses the steps_to_take list
    steps_to_take.reverse()

    print("Number of the steps to solution: ", len(steps_to_take))
    #print("Solution: ", steps_to_take)
   

    print("NODE PATHS: ", len(nodePaths))
    return steps_to_take


################################################################
#                       A* ALGORITHM                           #
################################################################
def a_star_search(puzzle_encoding, heuristic_function):
    priorityQueue = PriorityQueue()
    priorityQueue.put(puzzle_encoding)


    # The queue should probably always have 8 characters in the string
    current_node = ""
    visited_set = {puzzle_encoding}

    goal = "12345678-"
    parent_node = None

    # Dictonary that contains all the nodes represented by the key-value pair of state and parent such as "12345678-" (node) and "1234567-8" (parent)
    nodePaths = { }
    rootNodePassed = False

    while not findPath(goal, current_node):

        # load the next element in the queue to return and remove it from the queue
        current_node_parent = priorityQueue.get()
       

        if type(current_node_parent) == tuple:
            #edge_weight = current_node_parent[0]
            current_node = current_node_parent[1]
            parent_node = current_node_parent[2]
        else:
            current_node = current_node_parent


        if current_node not in nodePaths:
            if rootNodePassed is False:
                nodePaths[current_node] = None
                rootNodePassed = True
            else:
                nodePaths[current_node] = parent_node

        node_depth = distanceToNode(current_node, nodePaths)

        parent_node = current_node
        
        possiblePaths_Parent = directionsToMove(current_node, heuristic_function, node_depth)


        for i in range(len(possiblePaths_Parent)):
            # Test if the possible path has been visited yet by comparing it to the set
            if possiblePaths_Parent[i] not in visited_set:
                # Determine the weight of the edge of a particular node with a heuristicfunction
                
                priorityQueue.put(possiblePaths_Parent[i])
                visited_set.add(possiblePaths_Parent[i])


    # Since the dictonary has been generated we simply need to retrace our steps back to the root node--printing all the nodes inbetween!
    steps_to_take = [goal]
    curr_node = goal

    while nodePaths[curr_node] is not None:

        steps_to_take.append(nodePaths[curr_node])
        # Get he parent stored for that node
        curr_node = nodePaths[curr_node]

    # Reverses the steps_to_take list
    steps_to_take.reverse()

    print("Number of the steps to solution: ", len(steps_to_take))
    #print("Solution: ", steps_to_take)
   

    print("NODE PATHS: ", len(nodePaths))
    return steps_to_take


################################################################
#                       HELPER FUNCTIONS                       #
################################################################
# Checks if the "-" piece can move in a given direction - write a seperate function handling the conditions 
            #     if it can move in the given direction add it to the queue with test_queue.put(add)
def directionsToMove(queue, heuristic_function=None, node_depth=0):
    if(len(queue) != 9):
        print("[DEBUG] directionsToMove queue PARAMETER MUST HAVE 9 ELEMENTS")
        return

   
    # Finds what index the '-' is at
    open_space_index = queue.find('-')

    # Put the queue into a list so that the elements can be modified; python has immutable strings!
    # [NOTE] This must be joined to return it into a string!

    if (open_space_index == 0):
        # Index 1 & 3 can be moved 
        # Indexes will be stored in a dictonary so that they can be looped through later to be inserted into a returnable tuple
        indexesToSwap = {
            "index1" : 1,
            "index2" : 3
        }
        # [Case] Index 1 will be moved; Swap the place of index 1 and index 0 -- the index of the open space
        # [Case] Index 3 will be moved
        return getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth)

    elif (open_space_index == 1):
        # Index 0 & 2 & 4 can be moved
        indexesToSwap = {
            "index1" : 0,
            "index2" : 2,
            "index3" : 4,
        }
        return getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth)

    elif (open_space_index == 2):
        # Index 1 & 5 can be moved
        indexesToSwap = {
            "index1" : 1,
            "index2" : 5,
        }
        return getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth)

    elif (open_space_index == 3):
        # Index 0 & 4 & 6 can be moved
        indexesToSwap = {
            "index1" : 0,
            "index2" : 4,
            "index3" : 6,
        }
        return getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth)
        
    elif (open_space_index == 4):
        # Index 1 & 3 & 5 & 7 can be moved
        indexesToSwap = {
            "index1" : 1,
            "index2" : 3,
            "index3" : 5,
            "index4" : 7,
        }
        return getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth)

    elif (open_space_index == 5):
        # Index 2 & 4 & 8 can be moved
        indexesToSwap = {
            "index1" : 2,
            "index2" : 4,
            "index3" : 8,
        }
        return getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth)

    elif (open_space_index == 6):
        # Index 3 & 7 can be moved
        indexesToSwap = {
            "index1" : 3,
            "index2" : 7,
        }
        return getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth)

    elif (open_space_index == 7):
        # Index 4 & 6 & 8 can be moved
        indexesToSwap = {
            "index1" : 4,
            "index2" : 6,
            "index3" : 8,
        }
        return getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth)

    elif (open_space_index == 8):
        # Index 5 & 7 can be moved
        indexesToSwap = {
            "index1" : 5,
            "index2" : 7,
        }
        return getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth)

    else:
        print("[DEBUG] INDEX NOT REGONIZED")

# Gets the possible states
def getPossibleStates(indexesToSwap, queue, open_space_index, heuristic_function, node_depth=0):
    queueable_paths = []
    for i in range(1, len(indexesToSwap) + 1):
        newQueue = list(queue)
    
        
        temp = newQueue[open_space_index]
        newQueue[open_space_index] = newQueue[indexesToSwap[f"index{i}"]]
        newQueue[indexesToSwap[f"index{i}"]] = temp


        weight_node_parent_pair = None
        # If a heuristic_function is not provided then do not use a heuristic_function
        if heuristic_function is not None:
            weight_node_parent_pair = (heuristic_function(newQueue) + node_depth,"".join(newQueue), queue)
        else:
            weight_node_parent_pair = (0 + node_depth,"".join(newQueue), queue)

       
        queueable_paths.append(weight_node_parent_pair)

    return queueable_paths

# Finds how deep in terms of levels the node is
# Takes a node and a dictonary that contains all the traversed nodes so far with a node-parent key-value pair
def distanceToNode(curr_node, nodePaths):
    depth = 0

    while nodePaths[curr_node] is not None:
        # Get he parent stored for that node
        curr_node = nodePaths[curr_node]
        depth += 1

    return depth

def findPath(path_to_find, current_path):
    if path_to_find == current_path:
        # The path was found
        return True
    else:
        return False

################################################################
#                    HEURISTIC FUNCTIONS                       #
################################################################
def manhattan_distance(puzzle_encoding):
    total_manhattan = 0


    for tile in puzzle_encoding:
        distance = distance_apart(puzzle_encoding.index(tile), tile)

        total_manhattan += distance

    return total_manhattan

def distance_apart(index, tile):

    # (INDEX) : (ROW_NUMBER, COLUMN NUMBER) - 0 INDEXED from (0, 0) to (2,2)
    correct_tile_positions = {
        "1" : (0, 0),
        "2" : (0, 1),
        "3" : (0, 2),
        "4" : (1, 0),
        "5" : (1, 1),
        "6" : (1, 2),
        "7" : (2, 0),
        "8" : (2, 1),
        "-" : (2, 2)
    }

    index_map = {
        0 : (0, 0),
        1 : (0, 1),
        2 : (0, 2),
        3 : (1, 0), 
        4 : (1, 1),
        5 : (1, 2),
        6 : (2, 0), 
        7 : (2, 1),
        8 : (2, 2),
    }
    
    distance_apart = abs(correct_tile_positions[tile][0] - index_map[index][0]) + abs(correct_tile_positions[tile][1] - index_map[index][1])
    return distance_apart





def number_of_tiles_out_of_place(puzzle_encoding):
    tiles_out_of_place = 0

    for tile in puzzle_encoding:
        result = out_of_place(puzzle_encoding.index(tile), tile)
        
        if result:
            tiles_out_of_place += 1

    return tiles_out_of_place

# Determines if a single tile is out of place
def out_of_place(index, tile):
    correct_indexes = {
        "1" : 0,
        "2" : 1,
        "3" : 2,
        "4" : 3,
        "5" : 4,
        "6" : 5,
        "7" : 6,
        "8" : 7,
        "-" : 8
    }

    if index == correct_indexes[tile]:
        return False
    else:
        return True


# THE HEURISTIC FUNCTIONS ARE LABELED UNDER THE NAMES:
# - number_of_tiles_out_of_place
# - manhattan_distance

# THE ALGORITHMS ARE LABELED AS:
# - breadth_first_search(string puzzle_encoding)
# - best_first_search(string puzzle_encoding, heuristic_function())
# - a_star_search(string puzzle_encoding, heuristic_function())


# # EXAMPLES:
# print("================================")
# print("=     BREADTH FIRST SEARCH     =")
# print("================================")
# t0_start = time()
# print(breadth_first_search("1564-7238"))
# t0_end = time()
# print("BREADTH SEARCH FINISHED IN:", t0_end - t0_start)
# print("")


# print("===========================================")
# print("=      BEST FIRST SEARCH - Manhattan      =")
# print("===========================================")
# t1_start = time()
# print(best_first_search("1564-7238", manhattan_distance))
# t1_end = time()
# print("BEST FIRST SEARCH FINISHED IN:", t1_end - t1_start)
# print("")


# print("====================================================")
# print("=      BEST FIRST SEARCH - Tiles out of place      =")
# print("====================================================")
# t2_start = time()
# print(best_first_search("1564-7238", number_of_tiles_out_of_place))
# t2_end = time()
# print("BEST FIRST SEARCH FINISHED IN:", t2_end - t2_start)
# print("")


# print("==========================================")
# print("=          A* SEARCH - Manhattan         =")
# print("==========================================")
# t3_start = time()
# print(a_star_search("1564-7238", manhattan_distance))
# t3_end = time()
# print("A* SEARCH FINISHED IN:", t3_end - t3_start)
# print("")


# print("===================================================")
# print("=          A* SEARCH - Tiles out of place         =")
# print("===================================================")
# t3_start = time()
# print(a_star_search("1564-7238", number_of_tiles_out_of_place))
# t3_end = time()
# print("A* SEARCH FINISHED IN:", t3_end - t3_start)
# print("")

