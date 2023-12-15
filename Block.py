import pygame as pg 

class Present():
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
        for x in range(self.width):
            for y in range(self.height):
                self.occupied.append([self.posx+x,self.posy+y])
                print("present at space")
                print(str(self.posx)+"-"+str(self.posy))
                print("occupying:")
                print(str(self.occupied))

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.tick = 0
        

    
    def update(self):

        self.tick +=1
        if self.tick > 5:
            self.tick = 5

        if pg.Rect.colliderect(self.rect, self.app.mousebox) and self.app.mousedown:
            self.app.active_present = self
        

        if self.app.active_present == self:
            self.active_rgb = (0,255,0)
        else:
            self.active_rgb = self.rgb

        if self.app.active_present == self:
            #FIND LEGAL MOVES!!
            #right??
            
            self.right_move = True
            broadcast_pos = [self.posx+1,self.posy]
            for block in self.app.current_presents:

                if block != self:
                    for occ in self.occupied:
                        for bocc in block.occupied:
                            if occ[0]+1 == bocc[0] and bocc[1] == occ[1]:
                                self.right_move = False
                            elif occ[0]+1 > 4:
                                self.right_move = False
            

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


            

        if (pg.K_d in self.app.currentK or pg.K_a in self.app.currentK or pg.K_s in self.app.currentK or pg.K_w in self.app.currentK) and self.tick >= 5 and self.app.active_present == self:

            self.tick = 0
        
            #MOVE RIGHT!
            if pg.K_d in self.app.currentK and self.right_move:
                #IF TRY TO MOVE RIGHT!
                self.posx += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])


                print("new occupants:")
                print(str(self.occupied))


            if pg.K_a in self.app.currentK and self.left_move:
                #IF TRY TO MOVE LEFT!
                self.posx -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))




            if pg.K_s in self.app.currentK and self.down_move:
                #IF TRY TO MOVE DOWN!
                self.posy += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))





            if pg.K_w in self.app.currentK and self.up_move:
                #IF TRY TO MOVE DOWN!
                self.posy -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))


        


    def draw(self):
        self.app.screen.blit(self.image,self.rect)

        if self.app.active_present == self:
            temp = pg.Surface((self.rect.width,self.rect.height))
            temp.fill((255,255,255))
            temp.set_alpha(80)

            self.app.screen.blit(temp,self.rect)









class Golden_Present():
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

        self.rgb = rgb
        self.active_rgb = self.rgb
    
        self.legals = []

        self.image = image
        self.image = pg.image.load(("Assets/"+self.image+".png"))
        self.image = pg.transform.scale(self.image,(self.rect.width,self.rect.height))

        self.occupied =[]
        for x in range(self.width):
            for y in range(self.height):
                self.occupied.append([self.posx+x,self.posy+y])
                print("present at space")
                print(str(self.posx)+"-"+str(self.posy))
                print("occupying:")
                print(str(self.occupied))

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.right_win = False

        self.tick = 0
        

    
    def update(self):

        self.right_win = False

        self.tick +=1
        if self.tick > 5:
            self.tick = 5

        if pg.Rect.colliderect(self.rect, self.app.mousebox) and self.app.mousedown:
            self.app.active_present = self
        

        if self.app.active_present == self:
            self.active_rgb = (150,0,150)
        else:
            self.active_rgb = self.rgb

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
            
            elif [self.posx,self.posy] == self.app.wintile:
                self.app.win = True
                
            

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


            

        if (pg.K_d in self.app.currentK or pg.K_a in self.app.currentK or pg.K_s in self.app.currentK or pg.K_w in self.app.currentK) and self.tick >= 5 and self.app.active_present == self:

            self.tick = 0
        
            #MOVE RIGHT!
            if pg.K_d in self.app.currentK and self.right_move:
                #IF TRY TO MOVE RIGHT!
                self.posx += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])


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


            elif pg.K_a in self.app.currentK and self.left_move:
                #IF TRY TO MOVE LEFT!
                self.posx -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))




            elif pg.K_s in self.app.currentK and self.down_move:
                #IF TRY TO MOVE DOWN!
                self.posy += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))





            elif pg.K_w in self.app.currentK and self.up_move:
                #IF TRY TO MOVE DOWN!
                self.posy -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

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

            else:
                temprect = pg.Rect(self.rect.right,self.rect.centery,10,10)
                pg.draw.rect(self.app.screen,(255,0,0),temprect)

            if self.left_move:
                temprect = pg.Rect(self.rect.left-10,self.rect.centery,10,10)
                pg.draw.rect(self.app.screen,(0,255,0),temprect)
            else:
                temprect = pg.Rect(self.rect.left-10,self.rect.centery,10,10)
                pg.draw.rect(self.app.screen,(255,0,0),temprect)

            if self.up_move:
                temprect = pg.Rect(self.rect.centerx,self.rect.y-10,10,10)
                pg.draw.rect(self.app.screen,(0,255,0),temprect)
            else:
                temprect = pg.Rect(self.rect.centerx,self.rect.y-10,10,10)
                pg.draw.rect(self.app.screen,(255,0,0),temprect)

            if self.down_move:
                temprect = pg.Rect(self.rect.centerx,self.rect.bottom,10,10)
                pg.draw.rect(self.app.screen,(0,255,0),temprect)
            else:
                temprect = pg.Rect(self.rect.centerx,self.rect.bottom,10,10)
                pg.draw.rect(self.app.screen,(255,0,0),temprect)
            


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












class Present():
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
        for x in range(self.width):
            for y in range(self.height):
                self.occupied.append([self.posx+x,self.posy+y])
                print("present at space")
                print(str(self.posx)+"-"+str(self.posy))
                print("occupying:")
                print(str(self.occupied))

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.tick = 0
        

    
    def update(self):

        self.tick +=1
        if self.tick > 5:
            self.tick = 5

        if pg.Rect.colliderect(self.rect, self.app.mousebox) and self.app.mousedown:
            self.app.active_present = self
        

        if self.app.active_present == self:
            self.active_rgb = (0,255,0)
        else:
            self.active_rgb = self.rgb

        if self.app.active_present == self:
            #FIND LEGAL MOVES!!
            #right??
            
            self.right_move = True
            broadcast_pos = [self.posx+1,self.posy]
            for block in self.app.current_presents:

                if block != self:
                    for occ in self.occupied:
                        for bocc in block.occupied:
                            if occ[0]+1 == bocc[0] and bocc[1] == occ[1]:
                                self.right_move = False
                            elif occ[0]+1 > 4:
                                self.right_move = False
            

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


            

        if (pg.K_d in self.app.currentK or pg.K_a in self.app.currentK or pg.K_s in self.app.currentK or pg.K_w in self.app.currentK) and self.tick >= 5 and self.app.active_present == self:

            self.tick = 0
        
            #MOVE RIGHT!
            if pg.K_d in self.app.currentK and self.right_move:
                #IF TRY TO MOVE RIGHT!
                self.posx += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])


                print("new occupants:")
                print(str(self.occupied))


            if pg.K_a in self.app.currentK and self.left_move:
                #IF TRY TO MOVE LEFT!
                self.posx -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))




            if pg.K_s in self.app.currentK and self.down_move:
                #IF TRY TO MOVE DOWN!
                self.posy += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))





            if pg.K_w in self.app.currentK and self.up_move:
                #IF TRY TO MOVE DOWN!
                self.posy -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

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









class Present_Vert():
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

        self.rgb = rgb
        self.active_rgb = self.rgb
    
        self.legals = []

        self.image = image
        self.image = pg.image.load(("Assets/"+self.image+".png"))
        self.image = pg.transform.scale(self.image,(self.rect.width,self.rect.height))

        self.occupied =[]
        for x in range(self.width):
            for y in range(self.height):
                self.occupied.append([self.posx+x,self.posy+y])
                print("present at space")
                print(str(self.posx)+"-"+str(self.posy))
                print("occupying:")
                print(str(self.occupied))

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.right_win = False

        self.tick = 0
        

    
    def update(self):

        self.right_win = False

        self.tick +=1
        if self.tick > 5:
            self.tick = 5

        if pg.Rect.colliderect(self.rect, self.app.mousebox) and self.app.mousedown:
            self.app.active_present = self
        

        if self.app.active_present == self:
            self.active_rgb = (150,0,150)
        else:
            self.active_rgb = self.rgb

        if self.app.active_present == self:
            #FIND LEGAL MOVES!!
            #right??


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


            

        if (pg.K_s in self.app.currentK or pg.K_w in self.app.currentK) and self.tick >= 5 and self.app.active_present == self:

            self.tick = 0
        




            if pg.K_s in self.app.currentK and self.down_move:
                #IF TRY TO MOVE DOWN!
                self.posy += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))





            if pg.K_w in self.app.currentK and self.up_move:
                #IF TRY TO MOVE DOWN!
                self.posy -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

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




class Present():
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
        for x in range(self.width):
            for y in range(self.height):
                self.occupied.append([self.posx+x,self.posy+y])
                print("present at space")
                print(str(self.posx)+"-"+str(self.posy))
                print("occupying:")
                print(str(self.occupied))

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.tick = 0
        

    
    def update(self):

        self.tick +=1
        if self.tick > 5:
            self.tick = 5

        if pg.Rect.colliderect(self.rect, self.app.mousebox) and self.app.mousedown:
            self.app.active_present = self
        

        if self.app.active_present == self:
            self.active_rgb = (0,255,0)
        else:
            self.active_rgb = self.rgb

        if self.app.active_present == self:
            #FIND LEGAL MOVES!!
            #right??
            
            self.right_move = True
            broadcast_pos = [self.posx+1,self.posy]
            for block in self.app.current_presents:

                if block != self:
                    for occ in self.occupied:
                        for bocc in block.occupied:
                            if occ[0]+1 == bocc[0] and bocc[1] == occ[1]:
                                self.right_move = False
                            elif occ[0]+1 > 4:
                                self.right_move = False
            

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


            

        if (pg.K_d in self.app.currentK or pg.K_a in self.app.currentK or pg.K_s in self.app.currentK or pg.K_w in self.app.currentK) and self.tick >= 5 and self.app.active_present == self:

            self.tick = 0
        
            #MOVE RIGHT!
            if pg.K_d in self.app.currentK and self.right_move:
                #IF TRY TO MOVE RIGHT!
                self.posx += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])


                print("new occupants:")
                print(str(self.occupied))


            if pg.K_a in self.app.currentK and self.left_move:
                #IF TRY TO MOVE LEFT!
                self.posx -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))




            if pg.K_s in self.app.currentK and self.down_move:
                #IF TRY TO MOVE DOWN!
                self.posy += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

                print("new occupants:")
                print(str(self.occupied))





            if pg.K_w in self.app.currentK and self.up_move:
                #IF TRY TO MOVE DOWN!
                self.posy -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

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

        








class Present_Hori():
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

        self.rgb = rgb
        self.active_rgb = self.rgb
    
        self.legals = []

        self.image = image
        self.image = pg.image.load(("Assets/"+self.image+".png"))
        self.image = pg.transform.scale(self.image,(self.rect.width,self.rect.height))

        self.occupied =[]
        for x in range(self.width):
            for y in range(self.height):
                self.occupied.append([self.posx+x,self.posy+y])
                print("present at space")
                print(str(self.posx)+"-"+str(self.posy))
                print("occupying:")
                print(str(self.occupied))

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.right_win = False

        self.tick = 0
        

    
    def update(self):

        self.right_win = False

        self.tick +=1
        if self.tick > 5:
            self.tick = 5

        if pg.Rect.colliderect(self.rect, self.app.mousebox) and self.app.mousedown:
            self.app.active_present = self
        

        if self.app.active_present == self:
            self.active_rgb = (150,0,150)
        else:
            self.active_rgb = self.rgb

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
            
            

            

        if (pg.K_d in self.app.currentK or pg.K_a in self.app.currentK ) and self.tick >= 5 and self.app.active_present == self:

            self.tick = 0
        
            #MOVE RIGHT!
            if pg.K_d in self.app.currentK and self.right_move:
                #IF TRY TO MOVE RIGHT!
                self.posx += 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])


                print("new occupants:")
                print(str(self.occupied))


                if self.right_win:
                    temp = self.app.levels.index(self.app.state)
                    temp += 1


            if pg.K_a in self.app.currentK and self.left_move:
                #IF TRY TO MOVE LEFT!
                self.posx -= 1

                self.rect = pg.Rect(420+((self.posx+1)*216),
                                self.posy*216,
                                self.width*216,
                                self.height*216)
                
                self.occupied = []
                for x in range(self.width):
                    for y in range(self.height):
                        self.occupied.append([self.posx+x,self.posy+y])

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




class Present_Rock():
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
        for x in range(self.width):
            for y in range(self.height):
                self.occupied.append([self.posx+x,self.posy+y])
                print("present at space")
                print(str(self.posx)+"-"+str(self.posy))
                print("occupying:")
                print(str(self.occupied))

        self.right_move = False
        self.left_move = False
        self.down_move = False
        self.up_move = False

        self.tick = 0
        

    
    def update(self):

        pass

        


    def draw(self):
        self.app.screen.blit(self.image,self.rect)
