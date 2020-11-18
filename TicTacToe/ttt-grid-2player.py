# TTT (Part 1)
# This program allows two players to play Tic Tac Toe.
# The X and O player's take turns selecting empty tiles
# to fill on a 3x3 board. If a player selects three tiles
# in a row, a column or a diagonal, that player wins.
# If all the tiles are filled without a win, the game is
# a draw.
#
# Part 1 implements a two player game in which both 
# players can select tiles until the whole board is
# filled. The players take turns, starting with the 
# X player. The turn changes when a valid selection 
# is made, i.e., an empty tile is selected. When an
# occupied tile is selected, the tile flashes briefly.

import pygame


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Tic Tac Toe')   
   # get the display surface
   w_surface = pygame.display.get_surface() 
   # create a game object
   game = Game(w_surface)
   # start the main game loop by calling the play method on the game object
   game.play() 
   # quit pygame and clean up the pygame window
   pygame.quit() 


# User-defined classes

class Game:
   # An object in this class represents a complete game.

   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
      
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      
      # === game specific objects
      # create board as an empty list
      self.board_size = 3
      self.board = []
      self.create_board()
      self.player_X = 'X'
      self.player_O = 'O'
      self.turn = self.player_X
      
   def create_board(self):
      width = self.surface.get_width()//3
      height = self.surface.get_height()//3
      # for each row index
      for row_index in range(0,self.board_size):
         # create row as an empty list
         row = []
         # for each column index
         for col_index in range(0,self.board_size):
            # create tile using row index and column index
            x = col_index * width 
            y = row_index * height
            tile = Tile(x,y,width,height,self.surface)
            # append tile to row
            row.append(tile)
         # append row to board
         self.board.append(row)      
      
   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game:
            self.update()
            self.decide_continue()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled
      
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(event)
            
   def handle_mouse_up(self, event):
      # Respond to the player releasing the mouse button by
      # taking appropriate actions.
      # - self is the Game where the mouse up occurred.
      # - event is the pygame.event.Event object to handle
      
      for row in self.board:
         for tile in row:
            if tile.select(event.pos, self.turn):
               self.change_turn()

            
   def change_turn(self):
      # Change the turn from one player to the other player.
      # - self is the Game where the mouse up occurred.

      if self.turn == self.player_X:
         self.turn = self.player_O
      else:
         self.turn = self.player_X

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      # draw the board
      for row in self.board:
         for tile in row:
            tile.draw()
      pygame.display.update() # make the updated surface appear on the display

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      pass
      

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      pass
       

class Tile:
   # an object of this class represents a Rectangular Tile
   
   def __init__(self, x, y, width, height,surface):
      
      # Initialize a tile to contain a ' '
      # - x is the int x coord of the upper left corner
      # - y is the int y coord of the upper left corner
      # - width is the int width of the tile
      # - height is the int height of the tile
      # - surface is pygame.Surface object on which a Tile object is drawn on
      
      self.rect = pygame.Rect(x,y,width,height)
      self.surface = surface
      self.content = ''
      self.flashing = False
   
   def draw(self):
      # Draw the Tile' content and a rectangle border, or flash it      
      # - self is the Tile object to draw
      
      color = pygame.Color('white')
      border_width = 3
      if not self.flashing:
         pygame.draw.rect(self.surface,color,self.rect,border_width)  
         self.draw_content()
      else:
         pygame.draw.rect(self.surface,color,self.rect)
         self.flashing = False
      
   def draw_content(self):
      # Draw the string content of the tile.
      # - self is the Tile
      
      text_string = self.content
      text_color = pygame.Color('white')        
      text_font = pygame.font.SysFont('', 100)
      text_image = text_font.render(text_string, True, text_color)
      text_x = self.rect.x + (self.rect.width - text_image.get_width()) // 2
      text_y = self.rect.y + (self.rect.height - text_image.get_height()) // 2
      text_pos = (text_x, text_y)
      self.surface.blit(text_image, text_pos)      
      
      
   def select(self, position, current_player):
      # A position was selected. If the position is in the Tile
      # and the Tile is empty, then update the Tile content
      # If the position is in this Tile but the Tile is not
      # empty, then mark this tile to flash.
      # - self is the Tile
      # - position is the selected location (tuple)
      # - current_player is the new str contents of the tile

      selected = False
      if self.rect.collidepoint(position):
         if self.content == '':
            self.content = current_player
            selected = True
         else:
            self.flashing = True
      return selected


main()