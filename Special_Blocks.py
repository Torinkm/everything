# -*- coding: utf-8 -*-
import pygame as pg

class Corner_Block():
    def __init__(self,app,gap,pos,image):
        self.app = app
        
        self.gap = gap

        self.posx = pos[0]
        self.posy = pos[1]

        self.width = 2
        self.height = 2

        self.rect = pg.Rect(420+((self.posx+1)*216),
                            self.posy*216,
                            self.width*216,
                            self.height*216)


    
        self.legals = []

        self.image = image
        self.image = pg.image.load(("Assets/"+self.image+".png"))
        self.image = pg.transform.scale(self.image,(self.rect.width,self.rect.height))

        self.occupied =[]
        for x in range(self.width):
            for y in range(self.height):
                self.occupied.append([self.posx+x,self.posy+y])
        
        for occ in self.occupied:
            if self.posx+occ[0] == gap[0] and self.posy+occ[1] == gap[0]
                
                
        

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.right_win = False

        self.tick = 0