# Pre-Poke Framework
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to inlclude additional modules that are part of
# the Python Standard Library; no other modules are allowed

import pygame, random, time


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Color Game')   
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
      size = self.surface.get_size()
      
      # === game specific objects
      self.left_tile = Tile('white', 70, 170, [size[0]/2 - 120, size[1]/2 - 85], self.surface)
      self.right_tile = Tile('white', 70, 170, [size[0]/2 + 60, size[1]/2 - 85], self.surface)
    
      self.match = 0
      self.mismatch = 0


    def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game:
            self.update()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

    def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled
      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.MOUSEBUTTONUP:
             if self.continue_game:
                if self.left_tile.color == pygame.Color('white'):
                    if self.left_tile.select(event.pos):
                        self.left_tile.color_change()
                        self.color_list.append(self.left_tile.color)
                if self.right_tile.color == pygame.Color('white'):
                    if self.right_tile.select(event.pos):
                        self.right_tile.color_change()
                        self.color_list.append(self.right_tile.color)

        
    def update(self):
        if self.match >= 5 or self.mismatch >= 5:
            self.continue_game = False        
        
        match, mismatch = self.match_or_mismatch()
        self.match += match
        self.mismatch += mismatch
        self.both_color_change()


    # this function determines whether the tile colors match or mismatch
    def match_or_mismatch(self):
        match = 0
        mismatch = 0
        if self.left_tile.color != pygame.Color('white') and self.right_tile.color != pygame.Color("white"):
            if self.left_tile.color == self.right_tile.color:
                match = 1
                
            else:
                mismatch = 1
        return match, mismatch

        
    # this function returns the tiles to their original color on the condition that 
    # both tile colors have already been changed
    def both_color_change(self):
      if self.left_tile.color != pygame.Color('white') and self.right_tile.color != pygame.Color('white'):
          time.sleep(1)
          self.left_tile.color = pygame.Color('white')
          self.right_tile.color = pygame.Color('white')

    def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      self.surface.fill(self.bg_color)
      self.left_tile.draw()
      self.right_tile.draw()
      self.draw_match_score()
      self.draw_mismatch_score()
      pygame.display.update() # make the updated surface appear on the display

    def draw_match_score(self):
        font_size = 50
        fg_color = pygame.Color('white')
        string = 'Match: ' + str(self.match)
        font = pygame.font.SysFont("", font_size)
        text_box = font.render(string, True, fg_color)
        location = (0,0)
        self.surface.blit(text_box, location)
    
    def draw_mismatch_score(self):
        font_size = 50
        fg_color = pygame.Color('white')
        string = 'Mismatch:' + str(self.mismatch)
        font = pygame.font.SysFont("", font_size)
        text_box = font.render(string, True, fg_color)
        location = (self.surface.get_width() - text_box.get_width(), 0)
        self.surface.blit(text_box, location)



class Tile:
   # An object in this class represents a Dot that moves 
   
    def __init__(self, color, width, height, center, surface):
      # Initialize a Dot.
      # - self is the Dot to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the dot
      # - radius is the int pixel radius of the dot
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object
      self.color = pygame.Color(color)
      self.width = width
      self.height = height
      self.center = center
      self.surface = surface
      self.dimensions = (self.width, self.height)
      self.rect = pygame.Rect(self.center, self.dimensions)
      self.color_list = ['red', 'yellow', 'green', 'blue']

    def color_change(self):
        if not self.color == 'white':
            random_color = random.choice(self.color_list)
            self.color = pygame.Color(random_color)
            

    def select(self, position):
        if self.rect.collidepoint(position):
            self.color_change()

    def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      
      pygame.draw.rect(self.surface, self.color, (self.center, self.dimensions))


main()