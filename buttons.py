import pygame
from pygame.locals import *
import sys



SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

start_img = pygame.image.load('Assets/start_btn.png').convert_alpha()
exit_img = pygame.image.load('Assets/exit_btn.png').convert_alpha()
options_img = pygame.image.load('Assets/options_btn.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action



start_button = Button(100,200, start_img, 1 )
exit_button = Button(450,200, exit_img, 1)
options_button = Button(250, 50, options_img, 1)


run = True
while run:

    screen.fill((202, 228, 241))

    if start_button.draw():
        print("START")
    if options_button.draw():
        print("OPTIONS")
    if exit_button.draw():
        print("EXIT")
        run = False

    

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
            run = False

    pygame.display.update()

pygame.quit()