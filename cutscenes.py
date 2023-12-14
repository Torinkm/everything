import pygame as pg 

class Cutscene():
    def __init__(self,app,slides,transition_to):
        self.app = app
        self.images = slides
        self.level = transition_to

        self.slides =[]
        for slide in self.images:
            self.slides.append(pg.image.load(("Assets/Cutscenes/"+slide+".png")))

        self.tick = 0
        self.current_slide = self.slides[0]

    def update(self):

        self.tick += 1
        if self.tick > 15:
            self.tick = 15

        if self.app.mousedown and self.tick == 15 and ((self.level in self.app.levels):
            self.tick = 0

            temp = self.slides.index(self.current_slide)
            temp += 1
            if temp > len(self.slides)-1:
                print("changing from cutscene to "+self.level)
                
                self.app.changing_state_to = self.level
                self.app.state = "changing state"
                

                temp2 = self.app.all_cutscenes.index(self)
                temp2+=1

                if temp2 > len(self.app.all_cutscenes)-1:
                    temp2 = len(self.app.all_cutscenes)-1

                self.app.current_cutscene = self.app.all_cutscenes[temp2]

            else:
                self.current_slide = self.slides[temp]
                
                
                
                
        elif self.app.mousedown and self.tick == 15 and self.level == "Gag" and self.current_slide == self.slides[-1]:
            self.tick = 0
            self.app.state = "Gag"
            
        


    def draw(self):
        self.app.screen.blit(self.current_slide,(0,0))
        
        

