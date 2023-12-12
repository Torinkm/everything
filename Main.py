import pygame as pg
import numpy as np


class Main:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode([0,0])
        self.running = True #Switch to false when game quit
        self.state = "start" #game state, changes for states like paused and game over

        self.currentK = [] #list of all keys currently down
        self.keys = [pg.K_a, pg.K_b, pg.K_c, pg.K_d, pg.K_e, pg.K_f, pg.K_g, pg.K_h, pg.K_i, pg.K_j, pg.K_k, pg.K_l, pg.K_m,
                    pg.K_n, pg.K_o, pg.K_p, pg.K_q, pg.K_r, pg.K_s, pg.K_t, pg.K_u, pg.K_v, pg.K_w, pg.K_x, pg.K_y, pg.K_z]
 


        self.mousebox = pg.Rect(0,0,5,5)




        #MAIN LOOP!!!!
        while self.running:
            self.clock.tick(120)

            self.screen.fill([255,255,255])

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
                pass
            



            pg.display.flip()






Main()
pg.quit()