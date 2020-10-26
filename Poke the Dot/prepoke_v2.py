# Pre-Poke The Dots Version 2
# we are learning how to do the following things:
#
# learn how to animate an object on the screen
#
# Some of the source code contained in this program is not original. It was borrowed from
# a tutorial found on pygame's website. Specifically, we used portions of this tutorial
# to respond to QUIT events and close the PyGame grapical window, to create a
# game window, and to understand how to use the flip() function to render graphics.
# https://www.pygame.org/docs/tut/PygameIntro.html
import pygame, time


def main():
    # initialize pygame -- this is required for rendering fonts
    pygame.init()
    
    # create the window and set its size to 500 width and 400 height
    size = (500, 400)
    screen = pygame.display.set_mode(size)
    
    # set the title of the window
    pygame.display.set_caption("Poke The Dots Prepration v1")\

    # initialize game objects
    bg_colour = pygame.Color('black')
    
    game_clock = pygame.time.Clock()
    FPS = 30
    circle_color = pygame.Color('green')
    circle_pos = [150, 150]
    circle_velocity = [ 5, -5 ]
    circle_radius = 30

    

    # ==Main Animation Loop
    # Each iteration over the loop will draw the dot at a static location
    # we will then move the dot a small amount, redraw the dot, and repeat many 
    # times a second to give the appearance of motion
    # will repeat until the windows close button is pressed
    
    # enter our main gameplay loop, repeating until the user clicks
    # the window's 'close' button
    close_clicked = False
    while not close_clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                close_clicked = True
        screen.fill(bg_colour) # clear our screen before we draw game objects
        
        # draw our dot to screen and move its location for next time, to create
        # illusion of motion 
        pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)
        for index in range(0,2):
            circle_pos[index] = (circle_pos[index] + circle_velocity[index])
        
        # render all drawn objects to the screen
        pygame.display.flip()
        game_clock.tick(FPS)
main()