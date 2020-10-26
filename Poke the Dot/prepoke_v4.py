# Pre-Poke The Dots Version Four
# we are learning how to do the following things:
#
# Re-approach what we have written so far, with the goal of using a class to define the
# attributes and behaviors of a Dot to be used in Poke the Dots. - DONE
#
# Some of the source code contained in this program is not original. It was borrowed from
# a tutorial found on pygame's website. Specifically, we used portions of this tutorial
# to respond to QUIT events and close the PyGame grapical window, to create a
# game window, and to understand how to use the flip() function to render graphics.
# https://www.pygame.org/docs/tut/PygameIntro.html
import pygame


def main():
    # initialize pygame -- this is required for rendering fonts
    pygame.init()
    
    # create the window and set its size to 500 width and 400 height
    size = (500, 400)
    screen = pygame.display.set_mode(size)
    
    # set the title of the window
    pygame.display.set_caption("Poke The Dots Prepration v3")
    
    # game objects and variables that are general to games
    bg_color = pygame.Color('black')
    game_clock = pygame.time.Clock()
    FPS = 30
    continue_game = True
    
    # game objects that are specific to poke the dots
    big_dot_color = pygame.Color('blue')
    big_dot_pos = [150, 150]
    big_dot_velocity = [ 1, 2]
    big_dot_radius = 30    
    big_dot = Dot(big_dot_color, big_dot_radius, big_dot_pos, big_dot_velocity, screen)    
    
    small_dot_color = pygame.Color('red')
    small_dot_pos = [300, 150]
    small_dot_velocity = [ 2, 1 ]
    small_dot_radius = 20    
    small_dot = Dot(small_dot_color, small_dot_radius, small_dot_pos, small_dot_velocity, screen)
    
    frame_counter = 0
    max_frames = 100
    
    # ===Main Gameplay Loop
    # Each iteration over the loop will draw the dot at a static location.
    # We will then move the dot a small amount, redraw the dot, and repeat
    # many times a second to give the appearance of motion.
    #
    # This will repeat until the user clikcs the window's 'close' button
    #
    # handle user input
    # draw game objects
    # check for game over conditions
    # if the game over conditions are not yet met:
    #   then update the game state
    #   (including checking for game over conditions)
    close_clicked = False
    while not close_clicked:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                close_clicked = True

        # draw game objects
        #
        # clear our screen before we draw game objects        
        screen.fill(bg_color)

        # draw our dot to screen
        small_dot.draw()
        big_dot.draw()
            
        # render all drawn objects to the screen
        pygame.display.flip()
        
        # look at game over conditions
        # if those conditions are not met:
        #   update the game state
        #   check if game over conditions are now met
        if continue_game:
            
            # update game objects (in this game, move our circle to a new location)
            #circle_pos[0] = circle_pos[0] + circle_velocity[0]
            #circle_pos[1] = circle_pos[1] + circle_velocity[1]
            small_dot.move()
            big_dot.move()

            frame_counter = frame_counter + 1
                
            # check if game over conditions are met
            if frame_counter > max_frames:
                continue_game = False
            
        game_clock.tick(FPS)

class Dot:
    # represents a single 'dot' in Poke the Dots
    def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, screen):
        self.color = dot_color
        self.radius = dot_radius
        self.center = dot_center
        self.velocity = dot_velocity
        self.screen = screen
    
    def move(self):
        # Change the location of the Dot by adding the corresponding
        # speed values ot hte dot's x and y coordinates of its center.
        for index in range(0,2):
            self.center[index] = self.center[index] + self.velocity[index]         
            
    def draw(self):
        # Draw the dot onto the game's window
        pygame.draw.circle(self.screen, self.color, self.center, self.radius)        
              
main()