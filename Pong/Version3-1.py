# Code Example 2
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
   width = 500
   height = 400
   pygame.display.set_mode((width, height))
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
 

   def __init__(self, surface):

      self.surface = surface
      self.bg_color = pygame.Color('black')
      

      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True

      self.ballRadius = 5
      self.leftScore = 0
      self.rightScore = 0
      self.maxScore = 11
      self.paddle = []
      
      self.width = self.surface.get_width()
      self.height = self.surface.get_height()

      self.ball = Dot('white', self.ballRadius, [int(self.width/2), int(self.height/2)], [4, 2], self.surface)
      self.paddle.append(paddle('white',10,40,[int(self.width/5),int(self.height/2)- 20],5,self.surface))
      self.paddle.append(paddle('white',10,40,[int(self.width - self.width/5),int(self.height/2)-20],5,self.surface))



   def play(self):

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game == True:
            self.update()
            self.decide_continue()
            self.getCollision()
         self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second
      
   def handle_events(self):

      events = pygame.event.get()
      for event in events:
         if event.type == pygame.QUIT:
            self.close_clicked = True

   def draw(self):
      
      self.surface.fill(self.bg_color) # clear the display surface first
      self.ball.draw()
      for i in range(len(self.paddle)):
         self.paddle[i].draw()
      self.surface.blit(text(str(self.leftScore)).surface,[0,0])
      self.surface.blit(text(str(self.rightScore)).surface,[self.width-60,0]) 
      pygame.display.flip()


   def update(self):

      for i in range(len(self.paddle)):
         self.paddle[i].move(i+1,self.height)
         self.paddle[i].update()


      leftHit,rightHit = self.ball.move(self.width,self.height)
      self.leftScore += leftHit
      self.rightScore += rightHit

   def decide_continue(self):
      if self.leftScore == self.maxScore or self.rightScore == self.maxScore:
         self.continue_game = False
         
   def getCollision(self):
      for i in range(len(self.paddle)):
         if self.paddle[i].rect.collidepoint(self.ball.center) == 1:
            if i == 0:
               if self.ball.velocity[0] < 0:
                  self.ball.velocity[0] *= -1
            elif i == 1:
               if self.ball.velocity[0] > 0:
                  self.ball.velocity[0] *= -1

class Dot:
   
   def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):

      self.color = pygame.Color(dot_color)
      self.radius = dot_radius
      self.center = dot_center
      self.velocity = dot_velocity
      self.surface = surface
      self.mask = pygame.mask.from_surface(self.surface)
      
   def move(self,width,height):

      leftHit = 0
      rightHit = 0
      mapDims = [width, height]
      for i in range(0,2):
        self.center[i] = (self.center[i] + self.velocity[i])

        if self.center[i] + self.radius >= mapDims[i]:
            self.velocity[i] *= -1
            if i == 0:
                leftHit = 1
        if self.center[i] - self.radius <= 0:
            self.velocity[i] *= -1
            if i == 0:
                rightHit = 1

      return leftHit, rightHit
   
   def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      
      pygame.draw.circle(self.surface, self.color, self.center, self.radius)

class paddle:
   def __init__(self,color, width, height, center, velocity, surface):
      self.color = pygame.Color(color)
      self.center = center
      self.velocity = velocity
      self.surface = surface
      self.dims = (width,height)
      self.mask = pygame.mask.from_surface(self.surface)
   
   def update(self):
      self.rect = pygame.Rect(self.center,self.dims)

   def draw(self):
      
      pygame.draw.rect(self.surface, self.color, (self.center, self.dims))

   def move(self,player,maxY):
      pressedKeys = pygame.key.get_pressed()
      if player == 1:
         up = pygame.K_q
         down = pygame.K_a
      elif player == 2:
         up = pygame.K_p
         down = pygame.K_l

      if not self.center[1]+self.dims[1] >= maxY:
         if pressedKeys[down]:
            self.center[1] += self.velocity
      if not self.center[1] <= 0:
         if pressedKeys[up]:
            self.center[1] -= self.velocity

class text:
   def __init__(self,score,color = (255,255,255),size = 60):
      self.color = color
      self.fontFam = 'Arial'
      self.fontSize = size
      self.font = pygame.font.SysFont(self.fontFam,self.fontSize)
      self.content = str(score)
      self.surface = self.font.render(self.content,1,self.color)


main()