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
   pygame.display.set_caption('Pong')   
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
      self.ball = Ball('white', 5, [250, 200], [4,4], self.surface)
      self.paddle1 = Paddle('white', 11, 42, [90 ,180], [0, 5], self.surface)
      self.paddle2 = Paddle('white', 11, 42, [410 ,180], [0, 5], self.surface)

      self.left_score = 0
      self.right_score = 0


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
      pressed_key = pygame.key.get_pressed()
      if pressed_key[pygame.K_q]:
         self.paddle1.move('up')
      if pressed_key[pygame.K_a]:
         self.paddle1.move('down')
      if pressed_key[pygame.K_p]:
         self.paddle2.move('up')
      if pressed_key[pygame.K_l]:
         self.paddle2.move('down')


   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.ball.draw()
      self.paddle1.draw()
      self.paddle2.draw()
      self.draw_left_score()
      self.draw_right_score()
      pygame.display.update() # make the updated surface appear on the display

   def draw_left_score(self):
       # draw the left score
       # self is the Game 
      font_size = 50
      fg_color = pygame.Color('white')
      string = str(self.left_score)
      font = pygame.font.SysFont("Arial", font_size)
      text_box = font.render(string, True, fg_color)
      location = (0, 0)
      self.surface.blit(text_box, location)

   def draw_right_score(self):
       # draw the right score
       # self is the Game
      font_size = 50
      fg_color = pygame.Color('white')
      string = str(self.right_score)
      font = pygame.font.SysFont("Arial", font_size)
      text_box = font.render(string, True, fg_color)
      if self.right_score >=10:
         location = (450, 0)
      else: 
         location = (475, 0) # accomodate double digit scores from right side.
      self.surface.blit(text_box, location)

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      
      # move the ball
      left_score, right_score = self.ball.move()
      self.left_score = self.left_score + left_score
      self.right_score = self.right_score + right_score

      if self.left_score == 11 or self.right_score == 11:
          self.continue_game = False
      # update the paddle rectangles
      self.paddle1.update()
      self.paddle2.update()
      # check if paddle collides with ball
      self.collide_paddle()


   def collide_paddle(self):
      # if the ball center is a point in paddle1.rect, then a boolean of true will occur
      # if true, then we will reverse the 'x' velocity of the ball
      # - self is the Game
       if self.paddle1.rect.collidepoint(self.ball.center) == True:
          # if the ball is moving left and collides with the paddle, reverse it to move right
          if self.ball.velocity[0] < 0: 
            # avoid bouncing from behind paddle since ball velocity is positive
            self.ball.velocity[0] = -self.ball.velocity[0]
       if self.paddle2.rect.collidepoint(self.ball.center) == True:
         # if the ball is moving right and collides with the paddle, reverse it to move left
         if self.ball.velocity[0] > 0:
            # avoid bouncing from behind paddle since ball velocity is negative
            self.ball.velocity[0] = -self.ball.velocity[0]
            


class Ball:
   # An object in this class represents a Dot that moves 
   
   def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):
      # Initialize a Ball.
      # - self is the Ball to initialize
      # - color is the pygame.Color of the Ball
      # - center is a list containing the x and y int
      #   coords of the center of the Ball
      # - radius is the int pixel radius of the Ball
      # - velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object

      self.color = pygame.Color(ball_color)
      self.radius = ball_radius
      self.center = ball_center
      self.velocity = ball_velocity
      self.surface = surface
      
      
   def move(self):
      # Change the location of the Ball by adding the corresponding 
      # speed values to the x and y coordinate of its center
      # - self is the Ball
      size = self.surface.get_size() # get size is a method inside pygame.Surface class, returns (width, height)
      for i in range(0,2):
         self.center[i] = (self.center[i] + self.velocity[i])  # center is bound to object type list
         # left, right, bottom, top
         if self.center[i] < self.radius or self.center[i] + self.radius >= size[i]: # right edge of window
             self.velocity[i] = -self.velocity[i]
    
      left_score = 0
      right_score = 0
      # every movement the scores are reset to 0, only become 1 if they hit a wall
      
      # if ball goes over right edge, score becomes one
      if self.center[0] + self.radius > size[0]:
          right_score = 1       
      # if ball goes over left edge, score becomes one
      if self.center[0] < self.radius:
          left_score = 1

      return left_score, right_score
         
         
   def draw(self):
      # Draw the Ball on the surface
      # - self is the Ball
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)

class Paddle:
    def __init__(self, paddle_color, paddle_width, paddle_height, paddle_center, paddle_velocity, surface):
      # Initialize a Paddle
      # - self is the Paddle to initialize
      # - paddle_color is the pygame.Color of the Paddle
      # - paddle_center is a list containing the x and y int
      #   coords of the center of the Paddle
      # - paddle_width is the int pixel width of the Paddle
      # - paddle_height is the int pixel height of the Paddle
      # - paddle_velocity is a list containing the x and y components
      # - surface is the window's pygame.Surface object
        self.paddle_color = pygame.Color(paddle_color)
        self.paddle_height = paddle_height
        self.paddle_width = paddle_width
        self.paddle_dimensions = (paddle_width, paddle_height)
        self.paddle_center = paddle_center
        self.paddle_velocity = paddle_velocity
        self.surface = surface
        
    
    def update(self):
        # update the rect of the paddle as the paddles move
        # self is the Paddle
        self.rect = pygame.Rect(self.paddle_center, self.paddle_dimensions)
    
    def move(self, direction):
        # change the location of the paddles by adding corresponding speed values to y coordinate of 
        # its center
        # self is the Paddle
        # direction is type str
        size = (500, 400) # window size
        if direction == 'up':
           # stop the paddle from going over the top edge
           if self.paddle_center[1] >= 0:
              self.paddle_center[1] -= self.paddle_velocity[1] 
        elif direction == 'down':
           # stop the paddle from going over the bottom edge
           if self.paddle_center[1] + self.paddle_height <= size[1]:
            self.paddle_center[1] += self.paddle_velocity[1]

    def draw(self):
        # Draw the paddle on the surface
        # self is the Paddle
        pygame.draw.rect(self.surface, self.paddle_color, (self.paddle_center, self.paddle_dimensions))
main()