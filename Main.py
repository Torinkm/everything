import pygame as pg
import numpy as np
import os
import random as rng
from buttons import Button, Slider

from cutscenes import *
from Block import *
from Collectibles import *

class Main:
    SCREEN_HEIGHT = 1080
    SCREEN_WIDTH = 1920
    def __init__(self):
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT),pg.RESIZABLE|pg.SCALED,vsync=1)
        self.jukebox = os.listdir("Music")
        pg.init()
        pg.mixer.music.load(f"Music\{rng.choice(self.jukebox)}")
        pg.mixer.music.play(1)
        pg.mixer.music.set_volume(0)
        self.running = True #Switch to false when game quit
        self.state = "main menu" #game state, changes for states like paused and game over
        self.mousedown = False
        self.changing_state_to = ""

        self.backgroundCol = [202, 228, 241]

        self.currentK = [] #list of all keys currently down
        self.keys = [pg.K_a, pg.K_b, pg.K_c, pg.K_d, pg.K_e, pg.K_f, pg.K_g, pg.K_h, pg.K_i, pg.K_j, pg.K_k, pg.K_l, pg.K_m,
                    pg.K_n, pg.K_o, pg.K_p, pg.K_q, pg.K_r, pg.K_s, pg.K_t, pg.K_u, pg.K_v, pg.K_w, pg.K_x, pg.K_y, pg.K_z]

        self.levels = ["level 1","level 2", "level 3","level 4"]

        self.all_cutscenes = [Cutscene(self,["1.1","1.2"],"level 1"),
                                Cutscene(self,["1.2","1.1"],"level 4")]

        self.current_cutscene = self.all_cutscenes[0]

        self.level_to_level = True
        
        self.win = False

        self.collectible_count = 0


        self.mousebox = pg.Rect(0,0,5,5)

        def updall(arr):
            for i in arr:
                i.update()

        def drawall(arr):
            for i in arr:
                i.draw()


        self.current_presents = [] #List of all the presents currently on screen.
        self.tiles = [] #list of all tiles

        

        alt = False
        for x in range(5):
            for y in range(5):
                usex = 420+((x+1)*216)
                usey = 0+((y)*216)

                if alt:
                    self.tiles.append(Tile(self,(usex,usey),(100,100,100)))
                    alt = False
                else:
                    self.tiles.append(Tile(self,(usex,usey),(140,140,140)))
                    alt = True





        self.start_img = pg.image.load('Assets/start_btn.png').convert_alpha()
        self.exit_img = pg.image.load('Assets/exit_btn.png').convert_alpha()
        self.options_img = pg.image.load('Assets/options_btn.png').convert_alpha()

        self.start_button = Button(self.SCREEN_WIDTH/2,200, self.start_img, 1 )
        self.options_button = Button(self.SCREEN_WIDTH/2, 400, self.options_img, 1)
        self.exit_button = Button(self.SCREEN_WIDTH/2,600, self.exit_img, 1)

        self.back_button = Button(200,100, self.exit_img, 1)

        self.sfx_Volume_Slider = Slider(500,300,label="SFX")
        self.music_Volume_Slider = Slider(500,500,label="Music")


        #MAIN LOOP!!!!
        while self.running:
            delta = self.clock.tick(120) #delta is the seconds between frames eg: 0.02s
            fps = round(self.clock.get_fps())
            if not pg.mixer.music.get_busy():
                pg.mixer.music.load(f"Music\{rng.choice(self.jukebox)}")
                pg.mixer.music.play(1)

            self.screen.fill(self.backgroundCol)

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    self.running = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    self.mousedown = True

                elif event.type == pg.MOUSEBUTTONUP:
                    self.mousedown = False

                if event.type == pg.KEYDOWN:
                    
                    for key in self.keys:
                        if event.key == key:
                            self.currentK.append(key)

                elif event.type == pg.KEYUP:
                    for key in self.keys:
                        if event.key == key:
                            self.currentK.remove(key)

            
            self.mousebox.x = pg.mouse.get_pos()[0]
            self.mousebox.y = pg.mouse.get_pos()[1]

            if self.state == "start":                
                updall(self.tiles)
                updall(self.current_presents)

                drawall(self.tiles)
                drawall(self.current_presents)
        

            elif self.state in self.levels:

                updall(self.tiles)
                updall(self.current_presents)

                print("after updating tiles state is "+str(self.state))

                if self.mousedown and pg.Rect.colliderect(self.mousebox,pg.Rect(100,920,100,100)):
                    temp = self.state
                    self.changing_state_to = temp
                    self.state = "changing state"
                    
                if self.state in self.levels:
                    bg_temp = self.levels.index(self.state)
                    bg_temp = str(bg_temp)
                    self.screen.blit(pg.image.load(("Assets/Background_"+bg_temp+".png")),(0,0))
    
                    drawall(self.tiles)
                    pg.draw.rect(self.screen,(0,0,255),(420+(216*(self.wintile[0]+1)),
                                                        216*self.wintile[1],
                                                        216,216))
                    drawall(self.current_presents)
    
                    self.screen.blit(pg.image.load(("Assets/Restart.png")),(100,920))
    
    
                    self.active_present.big_draw()
                    
                    
                    
                    
                if self.win:
                    
                    if self.level_to_level:
                        temp = self.levels.index(self.state)
                        temp +=1
                        
                        self.changing_state_to = self.levels[temp]
                        
                        self.state = "changing state"
                        
                    else:
                        self.state = "cutscene"


            
            elif self.state == "main menu":
                
                
                if self.start_button.update(self.mousebox):
                    self.state = "cutscene"

                    







                self.start_button.draw(self.screen)

                if self.options_button.update(self.mousebox):
                    self.state = "options menu"
                self.options_button.draw(self.screen)

                if self.exit_button.update(self.mousebox):
                    self.running = False
                self.exit_button.draw(self.screen)





            elif self.state == "cutscene":

                self.current_cutscene.update()
                self.current_cutscene.draw()
            
            elif self.state == "changing state":
                
                if self.changing_state_to == "level 2":

                    self.wintile = [5,0]

                    self.level_to_level = True

                    self.current_presents = []

                    self.current_presents.append(Golden_Present(self,(100,0,100),[0,1],1,1,"Anuc2"))

                    self.current_presents.append(Present(self,(255,0,0),[2,1],3,1,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[3,2],1,2,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[2,4],2,1,"Anuc"))

                    self.current_presents.append(Present_Rock(self,(255,0,0),[3,0],1,1,"Rock"))
                    self.current_presents.append(Present_Rock(self,(255,0,0),[4,2],1,1,"Rock"))
                    
                    

                    self.active_present = self.current_presents[0]




                if self.changing_state_to == "level 1":

                    self.wintile = [5,0]

                    self.level_to_level = True

                    self.current_presents = []

                    self.current_presents.append(Golden_Present(self,(100,0,100),[1,2],1,1,"Anuc2"))

                    self.current_presents.append(Present(self,(255,0,0),[4,0],1,2,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[4,3],1,2,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[3,2],2,1,"Anuc"))

                    
                    

                    self.active_present = self.current_presents[0]

                

                

                if self.changing_state_to == "level 3":

                    self.wintile = [5,3]

                    self.level_to_level = False

                    self.current_presents = []

                    self.current_presents.append(Golden_Present(self,(100,0,100),[2,0],1,1,"Anuc2"))

                    self.current_presents.append(Present(self,(255,0,0),[1,0],1,3,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[2,1],2,1,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[4,0],1,2,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[4,2],1,2,"Anuc"))

                    self.current_presents.append(Present_Rock(self,(255,0,0),[0,0],1,1,"Rock"))
                    self.current_presents.append(Present_Rock(self,(255,0,0),[3,2],1,1,"Rock"))
                    self.current_presents.append(Present_Rock(self,(255,0,0),[4,4],1,1,"Rock"))
                    self.current_presents.append(Present_Rock(self,(255,0,0),[0,3],1,1,"Rock"))

                    self.current_presents.append(Collectible(self,(255,0,0),[0,4],1,1,"Collectible"))
                    

                    self.active_present = self.current_presents[0]





                if self.changing_state_to == "level 4":

                    self.wintile = [5,3]

                    self.level_to_level = False

                    self.current_presents = []

                    self.current_presents.append(Golden_Present(self,(100,0,100),[2,0],1,1,"Anuc2"))

                    self.current_presents.append(Present(self,(255,0,0),[1,0],1,3,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[2,1],2,1,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[4,0],1,2,"Anuc"))
                    self.current_presents.append(Present(self,(255,0,0),[4,2],1,2,"Anuc"))

                    self.current_presents.append(Present_Rock(self,(255,0,0),[0,0],1,1,"Rock"))
                    self.current_presents.append(Present_Rock(self,(255,0,0),[3,2],1,1,"Rock"))
                    self.current_presents.append(Present_Rock(self,(255,0,0),[4,4],1,1,"Rock"))
                    self.current_presents.append(Present_Rock(self,(255,0,0),[0,3],1,1,"Rock"))

                    self.current_presents.append(Collectible(self,(255,0,0),[0,4],1,1,"Collectible"))
                    

                    self.active_present = self.current_presents[0]


                
                self.state = self.changing_state_to
            elif self.state == "options menu":
                if self.back_button.update(self.mousebox):
                    self.state = "main menu"
                self.back_button.draw(self.screen)
                self.sfx_Volume_Slider.update(self.mousebox)
                self.volume = (self.sfx_Volume_Slider.draw(self.screen))
                pg.mixer.music.set_volume(self.music_Volume_Slider.update(self.mousebox))
                self.music_Volume_Slider.draw(self.screen)

                


            pg.display.flip()




        



Main()
pg.quit()