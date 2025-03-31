#Importing Nessasary Libraries
import pygame

#Initialising required modules
pygame.init()

#Set up window geometry
screen = pygame.display.set_mode((600, 500))

#Create a loop to keep the game running until the user closes the window
done = False

while not done:
    
    #Keep clearing the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Make the changes visible
    pygame.display.flip()

