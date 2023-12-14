import pygame as pg
from math import *

class NoAnimation:
    def __init__(self, x, y, height, img:pg.surface.Surface = pg.surface.Surface((0,0))):
        scale = height/img.get_height()
        self.image = pg.transform.scale_by(img,scale)
        self.pos = pg.Vector2(x,y)
        self.rect = pg.rect.Rect(self.image.get_rect())
        self.rect.center = self.pos
    def update(self):
        if self.pos.y>=1080+self.rect.h/2:
            self.pos.y-=1080+self.rect.h/2
        elif self.pos.y<0-self.rect.h/2:
            self.pos.y+=1080+self.rect.h/2
        if self.pos.x>=1920+self.rect.w/2:
            self.pos.x-=1920+self.rect.w/2
        elif self.pos.x<0-self.rect.w/2:
            self.pos.x+=1920+self.rect.w/2
        self.rect.center = self.pos
    def draw(self,screen:pg.surface.Surface):
        screen.blit(self.image,self.rect)

class VerticalSine(NoAnimation):
    def __init__(self, x, y, height, img:pg.surface.Surface = None ,amp = pi, speed = 0.02):
        super().__init__(x,y,height,img)
        self.basePos = self.pos.copy()
        self.amplitude = amp
        self.wavespeed = speed
        self.wavepos = 0
    def update(self):
        self.wavepos+=self.wavespeed
        if self.wavepos>tau:
            self.wavepos -= tau
        self.pos.y = self.basePos.y+cos(self.wavepos)*self.amplitude
        super().update()

class Scroll(NoAnimation):
    def __init__(self, x, y, height, img:pg.surface.Surface = None, vel:pg.Vector2 = pg.Vector2(0,-1)):
        super().__init__(x,y,height,img)
        self.velocity = vel
    def update(self):
        self.pos += self.velocity
        super().update()
        
        
        