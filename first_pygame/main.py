import pygame

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Caption and Icon
pygame.display.set_caption("Rick Rolling Time")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, playerX, playerY)

#Game Loop.  Anything you want shown consistanlty goes into the while loop for game
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB screen color
    screen.fill((0, 0, 0))
    pygame.display.update()