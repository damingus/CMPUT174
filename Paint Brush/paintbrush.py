# Pre-Poke Framework
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to inlclude additional modules that are part of
# the Python Standard Library; no other modules are allowed

import pygame


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Painting')   
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
      self.paintbrush = Paintbrush('red', 10, 10, [size[0]/2, size[1]/2], [2, 2], self.surface)

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
    
    def move_brush(self):
      pressed_key = pygame.key.get_pressed()
      if pressed_key[pygame.K_UP]:
         self.paintbrush.move('up')
      if pressed_key[pygame.K_DOWN]:
         self.paintbrush.move('down')
      if pressed_key[pygame.K_RIGHT]:
         self.paintbrush.move("right")
      if pressed_key[pygame.K_LEFT]:
          self.paintbrush.move("left")
    
    def change_color(self):
      pressed_key = pygame.key.get_pressed()
      if pressed_key[pygame.K_b]:
          self.paintbrush.color_change('blue')
      if pressed_key[pygame.K_g]:
          self.paintbrush.color_change('green')
      if pressed_key[pygame.K_SPACE]:
          self.paintbrush.color_change('black')
      if pressed_key[pygame.K_r]:
          self.paintbrush.color_change('red')
      if pressed_key[pygame.K_y]:
          self.paintbrush.color_change('yellow')
    
    def update(self):
        self.move_brush()
        self.change_color()

    def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      self.paintbrush.draw()
      pygame.display.update() # make the updated surface appear on the display



class Paintbrush:
   # An object in this class represents a Dot that moves 
   
    def __init__(self, brush_color, brush_width, brush_height, brush_center, brush_velocity, surface):
      # Initialize a Dot.
      # - self is the Dot to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the dot
      # - radius is the int pixel radius of the dot
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(brush_color)
      self.height = brush_height
      self.width = brush_width
      self.center = brush_center
      self.velocity = brush_velocity
      self.surface = surface
      self.dimensions = (brush_width, brush_height)
      
    def move(self, direction):
      # Change the location of the Dot by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Dot
      size = (500, 400)
      if direction == 'up':
        # stop the paddle from going over the top edge
        if self.center[1] >= 0:
            self.center[1] -= self.velocity[1] 
      if direction == 'down':
        # stop the paddle from going over the bottom edge
        if self.center[1] + self.height <= size[1]:
            self.center[1] += self.velocity[1]
      if direction == "left":
          if self.center[0] >= 0:
              self.center[0] -= self.velocity[0]
      if direction == 'right':
          if self.center[0] + self.width <= size[0]:
              self.center[0] += self.velocity[0]
   
    def color_change(self, color):
        if color == 'blue':
            self.color = pygame.Color('blue')
        if color == 'red':
            self.color = pygame.Color('red')
        if color == 'green':
            self.color = pygame.Color('green')
        if color == 'yellow':
            self.color = pygame.Color('yellow')
        if color == 'black':
            self.color = pygame.Color('black')

    def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      
      pygame.draw.rect(self.surface, self.color, (self.center, self.dimensions))


main()