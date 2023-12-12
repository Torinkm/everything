import pygame as pg

class Collectible():
    def __init__(self,app,rgb,pos,width,height,image):

        self.app = app

        
        

        self.posx = pos[0]
        self.posy = pos[1]

        self.width = width
        self.height = height

        self.rect = pg.Rect(420+((self.posx+1)*216),
                            self.posy*216,
                            self.width*216,
                            self.height*216)

        self.image = image
        self.image = pg.image.load(("Assets/"+self.image+".png"))
        self.image = pg.transform.scale(self.image,(self.rect.width,self.rect.height))




        self.rgb = rgb
        self.active_rgb = self.rgb
    

        self.occupied =[]


        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.tick = 0
        

    
    def update(self):

        if self.app.current_presents[0].posx == self.posx and self.app.current_presents[0].posy == self.posy:
            self.app.current_presents.remove(self)
            self.app.collectible_count += 1

        


    def draw(self):
        self.app.screen.blit(self.image,self.rect)
