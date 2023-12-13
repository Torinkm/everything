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
        
        if self.gap == [0,0]:
        
            self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy+1)*216),216,216)
            
        elif self.gap == [1,0]:
            self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy+1)*216),216,216)
            
        elif self.gap == [0,1]:
            self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy)*216),216,216)
            
        elif self.gap == [1,1]:
            self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy)*216),216,216)
                          
        

        self.rect = pg.Rect(420+((self.posx+1)*216),(self.posy*216),432,432)
                      
        
        
        
        


    
        self.legals = []

        self.image = image
        self.image = pg.image.load(("Assets/"+self.image+".png"))
        self.image = pg.transform.scale(self.image,(self.rect.width,self.rect.height))
        
        
        if self.gap == [1,0]:
            self.image = pg.transform.rotate(self.image,-90)
            

        self.occupied =[]
        for x in range(self.width):
            for y in range(self.height):
                self.occupied.append([self.posx+x,self.posy+y])
        
        for occ in self.occupied:
            if self.posx+self.gap[0] == occ[0] and self.posy+self.gap[1] == occ[1]:
                
                
                
                print("Gap found!:")
                print(str(occ))
                self.occupied.remove(occ)
                
                
                
        

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.right_win = False

        self.tick = 0
        
        
    def update(self):
        
        self.tick +=1
        if self.tick > 10:
            self.tick = 10

        if pg.Rect.colliderect(self.clickrect, self.app.mousebox) and self.app.mousedown:
            self.app.active_present = self
        



        if self.app.active_present == self:
            #FIND LEGAL MOVES!!
            #right??
            
            self.right_move = True
            self.broadcast_pos = [self.posx+1,self.posy]
            for block in self.app.current_presents:

                if block != self:
                    for occ in self.occupied:
                        for bocc in block.occupied:
                            if occ[0]+1 == bocc[0] and bocc[1] == occ[1]:
                                self.right_move = False
                            elif occ[0]+1 > 4:
                                self.right_move = False

            if (not self.right_move) and self.broadcast_pos == self.app.wintile:
                self.right_move = True
                self.right_win = True

            

            """
            if self.right_move:
                print("Can move right")
            else:
                print("Can't move right")
            """




            #FIND LEGAL MOVES!!
            #left??
            
            self.left_move = True
            broadcast_pos = [self.posx-1,self.posy]
            for block in self.app.current_presents:

                if block != self:
                    for occ in self.occupied:
                        for bocc in block.occupied:
                            if occ[0]-1 == bocc[0] and bocc[1] == occ[1]:
                                self.left_move = False
                            elif occ[0]-1 < 0:
                                self.left_move = False
            

            """
            if self.left_move:
                print("Can move left")
            else:
                print("Can't move left")
            """


            #FIND LEGAL MOVES!!
            #down??
            
            self.down_move = True
            broadcast_pos = [self.posx,self.posy+1]
            for block in self.app.current_presents:

                if block != self:
                    for occ in self.occupied:
                        for bocc in block.occupied:
                            if occ[0] == bocc[0] and bocc[1] == occ[1]+1:
                                self.down_move = False
                            elif occ[1]+1 > 4:
                                self.down_move = False


            #up??
            
            self.up_move = True
            broadcast_pos = [self.posx,self.posy+1]
            for block in self.app.current_presents:

                if block != self:
                    for occ in self.occupied:
                        for bocc in block.occupied:
                            if occ[0] == bocc[0] and bocc[1] == occ[1]-1:
                                self.up_move = False
                            elif occ[1]-1 < 0:
                                self.up_move = False


            

        if (pg.K_d in self.app.currentK or pg.K_a in self.app.currentK or pg.K_s in self.app.currentK or pg.K_w in self.app.currentK) and self.tick >= 10 and self.app.active_present == self:

            self.tick = 0
        
            #MOVE RIGHT!
            if pg.K_d in self.app.currentK and self.right_move:
                #IF TRY TO MOVE RIGHT!
                self.posx += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                
                
                
                if self.gap == [0,0]:
                
                    self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy+1)*216),216,216)
                    
                elif self.gap == [1,0]:
                    self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy+1)*216),216,216)
                    
                elif self.gap == [0,1]:
                    self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy)*216),216,216)
                    
                elif self.gap == [1,1]:
                    self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy)*216),216,216)
                    
                    
                    
                    
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])
                        
                for occ in self.occupied:
                    if self.posx+self.gap[0] == occ[0] and self.posy+self.gap[1] == occ[1]:
                        
                        
                        
                        print("Gap found!:")
                        print(str(occ))
                        self.occupied.remove(occ)


                print("new occupants:")
                print(str(self.occupied))


                if self.right_win:
                    self.right_win = False
                    
                    
                    if self.app.level_to_level:
                        temp = self.app.levels.index(self.app.state)
                        temp += 1
                        self.app.state = "changing state"
                        self.app.changing_state_to = self.app.levels[temp]
                    else:
                        self.app.state = "cutscene"


            if pg.K_a in self.app.currentK and self.left_move:
                #IF TRY TO MOVE LEFT!
                self.posx -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                
                
                if self.gap == [0,0]:
                
                    self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy+1)*216),216,216)
                    
                elif self.gap == [1,0]:
                    self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy+1)*216),216,216)
                    
                elif self.gap == [0,1]:
                    self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy)*216),216,216)
                    
                elif self.gap == [1,1]:
                    self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy)*216),216,216)
                    
                    
                    
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])
                        
                for occ in self.occupied:
                    if self.posx+self.gap[0] == occ[0] and self.posy+self.gap[1] == occ[1]:
                        
                        
                        
                        print("Gap found!:")
                        print(str(occ))
                        self.occupied.remove(occ)

                print("new occupants:")
                print(str(self.occupied))




            if pg.K_s in self.app.currentK and self.down_move:
                #IF TRY TO MOVE DOWN!
                self.posy += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                
                
                if self.gap == [0,0]:
                
                    self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy+1)*216),216,216)
                    
                elif self.gap == [1,0]:
                    self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy+1)*216),216,216)
                    
                elif self.gap == [0,1]:
                    self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy)*216),216,216)
                    
                elif self.gap == [1,1]:
                    self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy)*216),216,216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])
                        
                for occ in self.occupied:
                    if self.posx+self.gap[0] == occ[0] and self.posy+self.gap[1] == occ[1]:
                        
                        
                        
                        print("Gap found!:")
                        print(str(occ))
                        self.occupied.remove(occ)

                print("new occupants:")
                print(str(self.occupied))





            if pg.K_w in self.app.currentK and self.up_move:
                #IF TRY TO MOVE DOWN!
                self.posy -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                
                
                if self.gap == [0,0]:
                
                    self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy+1)*216),216,216)
                    
                elif self.gap == [1,0]:
                    self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy+1)*216),216,216)
                    
                elif self.gap == [0,1]:
                    self.clickrect = pg.Rect(420+((self.posx+2)*216),((self.posy)*216),216,216)
                    
                elif self.gap == [1,1]:
                    self.clickrect = pg.Rect(420+((self.posx+1)*216),((self.posy)*216),216,216)
                    
                    
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])
                        
                for occ in self.occupied:
                    if self.posx+self.gap[0] == occ[0] and self.posy+self.gap[1] == occ[1]:
                        
                        
                        
                        print("Gap found!:")
                        print(str(occ))
                        self.occupied.remove(occ)

                print("new occupants:")
                print(str(self.occupied))



            

        


    def draw(self):
        self.app.screen.blit(self.image,self.rect)

        if self.app.active_present == self:
            temp = pg.Surface((self.rect.width,self.rect.height))
            temp.fill((255,255,255))
            temp.set_alpha(80)

            self.app.screen.blit(temp,self.rect)
            
            
    def big_draw(self):
        
        if self.right_move:
            temprect = pg.Rect(self.rect.right,self.rect.centery,10,10)
            pg.draw.rect(self.app.screen,(0,255,0),temprect)