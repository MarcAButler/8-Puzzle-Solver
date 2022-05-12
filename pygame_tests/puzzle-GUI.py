import pygame
from queue import Queue
from 


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
            print(initial_puzzle_encoding[i])

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
    






# Initialize the python library
pygame.init()


# Make the drawing window
screen = pygame.display.set_mode([600, 600])

running = True

# Change color of the background to white
screen.fill((255, 255, 255))


################################################################
#                 CHOOSE SPECIFIC ALGORITHMS                   #
################################################################






# CREATE THE BOARD
board = Board("52134678-")

board_state = None

puzzle_encodings = Queue()
puzzle_encodings.put("1564-7238")
puzzle_encodings.put("15647-238")
puzzle_encodings.put("15-476238")
puzzle_encodings.put("1-5476238")
puzzle_encodings.put("-15476238")
puzzle_encodings.put("415-76238")

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