import pygame as pg
import sys

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x-width/2, y-height/2)
        self.clicked = False

    def update(self,mousebox):
        action = False
        if self.rect.colliderect(mousebox):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

    def draw(self,screen):    
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Slider():
    def __init__(self, x, y, len = 200 , label = ""):
        width = len
        height = 30
        self.rect = pg.rect.Rect(x,y,width,height)
        self.rect.topleft = (x-width/2, y-height/2)
        self.clicked = False

        self.minx = self.rect.left
        self.maxx = self.rect.right

        self.sliderPos = pg.Vector2(self.maxx-100,y)
        self.sliderRect = pg.rect.Rect(0,0,20,50)
        self.sliderRect.center = self.sliderPos

        self.font = pg.font.Font("Assets/PixeloidMono.ttf",64)
        self.label = self.font.render(label,True,[230,50,0])
        self.fontRect = self.label.get_rect()
        self.fontRect.centery = self.rect.centery
        self.fontRect.right = self.rect.left - 10


    @property
    def value(self) -> float:
        return (self.sliderPos.x-self.minx)/self.maxx

    def update(self,mousebox):
        if self.sliderRect.colliderect(mousebox) and not self.clicked:
            if pg.mouse.get_pressed()[0] == 1:
                self.clicked = True
                self.clickedOffset = self.sliderPos.x - mousebox.centerx

        if self.clicked:
            self.sliderPos.x = mousebox.centerx + self.clickedOffset
            self.sliderPos.x = pg.math.clamp(self.sliderPos.x, self.minx, self.maxx)
            self.sliderRect.center = self.sliderPos

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return self.value


    def draw(self,screen):    
        pg.draw.rect(screen, [30,30,30] , self.rect)
        pg.draw.rect(screen, [100,100,100], self.sliderRect)
        screen.blit(self.label,self.fontRect)
