import pygame as pg 

class Present():
    def __init__(self,app,rgb,pos,width,height):

        self.app = app

        self.posx = pos[0]
        self.posy = pos[1]

        self.width = width
        self.height = height

        self.rect = pg.Rect(420+((self.posx+1)*216),
                            self.posy*216,
                            self.width*216,
                            self.height*216)

        self.rgb = rgb
        self.active_rgb = self.rgb
    
        self.legals = []
        
    
    def update(self):

        if pg.Rect.colliderect(self.rect, self.app.mousebox) and self.app.mousedown:
            self.app.active_present = self
        

        if self.app.active_present == self:
            self.active_rgb = (0,255,0)
        else:
            self.active_rgb = self.rgb


        #FIND LEGAL MOVES!!


        if pg.K_d in self.app.currentK:
            #IF TRY TO MOVE RIGHT!
            pass


    def draw(self):
        pg.draw.rect(self.app.screen,self.active_rgb,self.rect)



class Tile():
    def __init__(self,app,pos,rgb):

        self.app = app
        self.pos = pos
        self.rgb = rgb
        self.rect = pg.Rect(0,0,216,216)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        pass

    def draw(self):
        pg.draw.rect(self.app.screen,self.rgb,self.rect)