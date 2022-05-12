import pygame
from queue import Queue
from puzzle_Search import breadth_first_search, best_first_search, a_star_search, manhattan_distance, number_of_tiles_out_of_place

# Uses the tiles class through inheritance to generate multiple all the tiles needed
class Board:

    # Uses the indexes of the strings to map to the tuple cooridnates (x, y) so titles can be drawn
    index_to_corrdinates = {
        0 : (0, 0),
        1 : (1, 0),
        2 : (2, 0),
        3 : (0, 1),
        4 : (1, 1),
        5 : (2, 1),
        6 : (0, 2),
        7 : (1, 2),
        8 : (2, 2),
    }


    def __init__(self, initial_puzzle_encoding):
        if len(initial_puzzle_encoding) != 9:
           raise Exception("MUST SUPPLY A STRING OF LENGTH 9")

        if type(initial_puzzle_encoding) != str:
           raise Exception("MUST SUPPLY A STRING")

        for i in range(len(initial_puzzle_encoding)):
            Tiles(initial_puzzle_encoding[i], self.index_to_corrdinates[i])


    def redraw(self, puzzle_encoding):
        if len(puzzle_encoding) != 9:
            raise Exception("MUST SUPPLY A STRING OF LENGTH 9")

        if type(puzzle_encoding) != str:
           raise Exception("MUST SUPPLY A STRING")

        for i in range(len(puzzle_encoding)):
            #print(puzzle_encoding[i])

            Tiles(puzzle_encoding[i], self.index_to_corrdinates[i])




class Tiles:
    # Initialize the font
    pygame.font.init()


   

    # RGB COLOR
    color_primary = (211,211,211)
    color_secondary = (93,93,93)
    color_empty = (34,34,34)

    tile_pos = 200
    tile_size = 190
    tile_border = 200

    


    
    # CONTRUCTOR SHOULD AUTOMATICALLY CREATE TILES THAT ARE SIZED
    def __init__(self, number, position):
        """
        TAKES: (NUMBER, POSITION): NUMBER = INT, POSITION = ( , ) - TUPLE FROM (0, 0) TO (2, 2)
        """
        self.number = number

        font = pygame.font.SysFont('Helvetica', 60)
        self.text = font.render(f'{number}', False, (0,0,0))
        x, y = position[0] * self.tile_size +  0, position[1] * self.tile_size +  0


        #[RECTANGLE]
        # https://www.pygame.org/docs/ref/rect.html
        
        self.rectangle = pygame.draw.rect(screen, self.color_secondary, pygame.Rect(position[0] * self.tile_pos +  0, position[1] * self.tile_pos +  0, self.tile_border, self.tile_border))
        # CHECK IF TILE IS '-' SO IT COLORS IT DIFFERENTLY
        if number == '-':
            self.rectangle = pygame.draw.rect(screen, self.color_empty, pygame.Rect(position[0] * self.tile_pos +  5, position[1] * self.tile_pos +  5, self.tile_size, self.tile_size))
        else:
            self.rectangle = pygame.draw.rect(screen, self.color_primary, pygame.Rect(position[0] * self.tile_pos +  5, position[1] * self.tile_pos +  5, self.tile_size, self.tile_size))
        
        screen.blit(self.text, (x + 95, y + 70))
        
    def move_tile(self, position):
        """TAKES A TUPLE POSITION TO MOVE THE TILE"""
      
        x, y = position[0] * self.tile_size +  0, position[1] * self.tile_size +  0

        self.rectangle = pygame.draw.rect(screen, self.color_primary, pygame.Rect(x, y, self.tile_size, self.tile_size))
        screen.blit(self.text, (x + 85, y + 65))
    




################################################################
#                 CHOOSE SPECIFIC ALGORITHMS                   #
################################################################



print("[CHOSE AN ALGORITHM BY TYPING THE FOLLOWING]")
print("bfs - breadth_first_search(puzzle_encoding)")
print("bstfs - best_first_search(puzzle_encoding, heuristic_function)")
print("a* - a_star_search(puzzle_encoding, heuristic_function)")
print("------------------------------------------------")


algorithm = ''
heuristic_function = ''
puzzle_encoding = ''


# algorithm_map = {
#                     'bfs' : breadth_first_search(puzzle_encoding)
#                 }

while algorithm not in ('bfs', 'bstfs', 'a*'):
    print("[CHOSE AN ALGORITHM BY TYPING THE FOLLOWING]")
    print("bfs   - breadth_first_search(puzzle_encoding)")
    print("bstfs - best_first_search(puzzle_encoding, heuristic_function)")
    print("a*    - a_star_search(puzzle_encoding, heuristic_function)")
    print("------------------------------------------------")
    algorithm = input("ALGORITHM: ")
    
    if (algorithm not in ('bfs', 'bstfs', 'a*')):
        print("[!] INCORRECT USAGE [!]")

if algorithm != 'bfs':
    while heuristic_function not in ('heuristic_function', 'manhattan', 'tiles_out_of_place'):
        print("[CHOOSE A HEURISTIC FUNCTION]")
        print("heuristic_function:")
        print("manhattan")
        print("tiles_out_of_place")
        print("------------------------------------------------")
        heuristic_function = input("HEURISTIC FUNCTION: ")
        
        if (heuristic_function not in ('heuristic_function', 'manhattan', 'tiles_out_of_place')):
            print("[!] INCORRECT USAGE [!]")
            print("YOU MUST ENTER ONE OF THE VALID FUNCTIONS")
            print("[CHOOSE A HEURISTIC FUNCTION]")

while len(puzzle_encoding) != 9:
    print("[ENTER A STRING ENCODING OF LENGTH 9]")
    print("EXAMPLE: '12345678-'")
    print("------------------------------------------------")
    puzzle_encoding = input("PUZZLE ENCODING: ")
    
    if puzzle_encoding != 9:
        print("[!] INCORRECT USAGE [!]")
        print("YOU MUST ENTER A STRING ENCODING OF LENGTH 9")


# PRINT THE USER INPUTS
print(f"[ALGORITHM]: {algorithm}")
print(f"[HEURISTIC FUNCTION]: {heuristic_function}")
print(f"[PUZZLE ENCODING]: {puzzle_encoding}")

solution_list = ''



if algorithm == "bfs":
   solution_list = breadth_first_search(puzzle_encoding)

elif algorithm == "bstfs":
    # Handle heuristic_function
    if heuristic_function == "manhattan":
        solution_list = best_first_search(puzzle_encoding, manhattan_distance)

    elif heuristic_function == "tiles_out_of_place":
        solution_list = best_first_search(puzzle_encoding, number_of_tiles_out_of_place)

elif algorithm == "a*":
     # Handle heuristic_function
    if heuristic_function == "manhattan":
        # [PASSES]
        solution_list = a_star_search(puzzle_encoding, manhattan_distance)

    elif heuristic_function == "tiles_out_of_place":
        solution_list = a_star_search(puzzle_encoding, number_of_tiles_out_of_place)

#solution_list = a_star_search("1564-7238", manhattan_distance)
puzzle_encodings = Queue()

for i in range(len(solution_list)):
    puzzle_encodings.put(solution_list[i])
    #$print(f"ELEMENT: {i}")


# Initialize the python library
pygame.init()


# Make the drawing window
screen = pygame.display.set_mode([600, 600])

# Set Title
pygame.display.set_caption("8-Puzzle-Solver")

# Create Image
# [ATTRIBUTION] "Icon made by Eucalyp from www.flaticon.com"
icon = pygame.image.load('algorithm.ico')
pygame.display.set_icon(icon)


running = True

# Change color of the background to white
screen.fill((255, 255, 255))



# CREATE THE BOARD
board = Board(solution_list[0])

board_state = None


# [TIMER]
# 1000 ms
time_to_wait = 1000
time_start = pygame.time.get_ticks()


while running:
    # Updates the game on every iteration of the while loop
    #pygame.display.update()


    # Check if the window was closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # [TESTING] IF THE USER PRESSES SOMETHING
        if event.type == pygame.KEYDOWN:
            # Change color of the background to white
            screen.fill((255, 255, 255))
            if event.key == pygame.K_LEFT:
                tile1.move_tile((2, 2))
                pygame.display.update()

            if event.key == pygame.K_RIGHT:
                tile1.move_tile((0, 0))
                pygame.display.update()




    #if puzzle_encodings.get():
    time_current = pygame.time.get_ticks()
    
    if puzzle_encodings.empty():
        board.redraw(board_state)

    if time_current - time_start >= time_to_wait and puzzle_encodings.empty() == False:
        time_start = time_current
        board_state = puzzle_encodings.get()
        board.redraw(board_state)

            


    # Renders the drawings
    pygame.display.flip()

# If the loop is broken the game will quit
pygame.quit()