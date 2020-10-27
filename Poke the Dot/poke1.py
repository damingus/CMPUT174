# Poke The Dots Part 1
# Implements a general game template for games with animation
# You must use this template for all your graphical lab assignments
# and you are only allowed to inlclude additional modules that are part of
# the Python Standard Library; no other modules are allowed

import pygame, random, math


# User-defined functions

def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((500, 400))
   # set the title of the display window
   pygame.display.set_caption('Poke The Dots')   
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
      self.score = 0
      self.small_dot = Dot('red', 30, [50, 50], [1, 2], self.surface)
      self.big_dot = Dot('blue', 40, [200, 100], [2, 1], self.surface)
      self.small_dot.randomize()
      self.big_dot.randomize()
      while self.small_dot.collide(self.big_dot):
         self.small_dot.randomize()
         self.big_dot.randomize()

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
   
   def handle_mouse_up(self):
      self.small_dot.randomize()
      self.big_dot.randomize()
   
   def handle_events(self):
      # Handle each user event by changing the game state appropriately.
      # - self is the Game whose events will be handled

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True
         if event.type == pygame.MOUSEBUTTONUP and self.continue_game:
            self.handle_mouse_up()

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.small_dot.draw()
      self.big_dot.draw()
      self.draw_score()
      if self.continue_game == False:
         self.draw_game_over()
      pygame.display.update() # make the updated surface appear on the display

   def draw_score(self):
      font_size = 72
      fg_color = pygame.Color("white")
      string = 'Score: ' + str(self.score)
      # step 1 create a font object
      font = pygame.font.SysFont("Arial", font_size)
      # step 2 create a tex_box
      text_box = font.render(string, True, fg_color)
      # step 3 compute location
      location = (0,0)
      # step 4 place textbok on surface
      self.surface.blit(text_box, location)

   def draw_game_over(self):
      font_size = 100
      fg_color = pygame.Color("red")
      bg_color = pygame.Color("blue")
      string = 'Game Over'

      # step 1 create a font object
      font = pygame.font.SysFont("Arial", font_size)
      # step 2 create a tex_box
      text_box = font.render(string, True, fg_color, bg_color)      
      h1 = self.surface.get_height()
      h2 = text_box.get_height()
      # step 3 compute location
      location = (0, h1 - h2)
      # step 4 place textbok on surface
      self.surface.blit(text_box, location)
  
   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      
      self.small_dot.move()
      self.big_dot.move()
      self.score = pygame.time.get_ticks()//1000
      # self.frame_counter = self.frame_counter + 1

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      if self.small_dot.collide(self.big_dot) == True:
         self.continue_game = False
      #if self.frame_counter > self.max_frames:
      #   self.continue_game = False


class Dot:
   # An object in this class represents a Dot that moves 
   
   def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
      # Initialize a Dot.
      # - self is the Dot to initialize
      # - color is the pygame.Color of the dot
      # - center is a list containing the x and y int
      #   coords of the center of the dot
      # - radius is the int pixel radius of the dot
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(dot_color)
      self.radius = dot_radius
      self.center = dot_center
      self.velocity = dot_velocity
      self.surface = surface
      
   def move(self):
      # Change the location of the Dot by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Dot
      
      # surface is an instance attribute and it is of type pygame.Surface 
      size = self.surface.get_size() # get_size is a method in pygame.Surface class
      
      for i in range(0,2):
         self.center[i] = (self.center[i] + self.velocity[i])
         # check left and top or right and bottom
         if self.center[i] < self.radius or self.center[i] + self.radius > size[i]:
            # we need to do something --- > bounce off the edges of the window
            self.velocity[i] = -self.velocity[i]
            
   def collide(self, other_dot):
      horizontal_distance = self.center[0] - other_dot.center[0]
      vertical_distance = self.center[1] - other_dot.center[1]
      distance = math.sqrt(horizontal_distance**2 + vertical_distance**2)

   # if distance <= (self.radius + other_dot.radius):
   #    return True
   # else:
   #    return False
      return distance < (self.radius + other_dot.radius)     
      
   def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)

   def randomize(self):
      # randomize the center of a Dot object
      # -self is the Dot
      size = self.surface.get_size()
      for index in range(0,2):
         self.center[index] = random.randint(self.radius,size[index] -self.radius)
      
main()
