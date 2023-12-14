# -*- coding: utf-8 -*-

class Scene():
    def __init__(self,app,image,paths):
        self.app = app
        self.images = slides
        self.level = transition_to

        self.slides =[]
        for slide in self.images:
            self.slides.append(pg.image.load(("Assets/Cutscenes/"+slide+".png")))

        self.tick = 0
        self.current_slide = self.slides[0]

    def update(self):
        pass
    
    

class Scene():
    def __init__(self,app,shots,transition_to):
        self.app = app
        self.level = transition_to
        
        
        self.shots = shots

        self.tick = 0
        self.current_shot = self.shots[0]

    def update(self):
        pass