# Pre-Poke the Dots Version Zero
# we are learning how to do the following things:
#
# learn how to open a graphical window -DONE
# learn how to keep graphical window open until close window is pressed - DONE
# set title window - DONE
# draw basic geometric shapes - DONE
# change the colour of geometric shapes - DONE
# respond to user input (close window) - DONE

import pygame
# create the window and set the size to 500 width and 400 height
size = (500, 400)
screen = pygame.display.set_mode(size)   


# set the title of the window
pygame.display.set_caption("Poke the Dot Preperation v0")


# set the main game loop, repeating until close_clicked is True
close_clicked = False
while not close_clicked:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            close_clicked = True
        
        # draw a green circle with radius 100 at position 150, 150 on screen
        circle_color = pygame.Color('pink')
        circle_position = (150, 150)
        circle_radius = 100
        pygame.draw.circle(screen, circle_color, circle_position, circle_radius)

        # draw a blue rectangle with height 50 and width 200 at position 0, 0 on screen
        rect_color = pygame.Color('blue')
        rect_left = 0
        rect_top = 0
        rect_width = 200
        rect_height = 50
        rect_parameters = pygame.Rect(rect_left, rect_top, rect_width, rect_height)
        pygame.draw.rect(screen, rect_color, rect_parameters)

        #render all drawn objects onto the screen
        pygame.display.flip()