import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from network import *
from Menu_items.main_menu import *
from Menu_items.settings_menu import *

class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION,pg.HWSURFACE | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.started = False
        self.location = "In_game"
        self.main_menu = Main_Menu(self)
        self.settings_menu = Settings_menu(self)
        self.map_open = False
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = Raycasting(self)
        self.network_handler = Network_Handler(self)

    def update(self):
        if self.location == "In_game":
            self.player.update()
            self.raycasting.update()
        pg.display.update()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"FPS: {self.clock.get_fps()}")

    def draw_background(self):
        pg.draw.rect(self.screen,(0,50,0),(0,HALF_HEIGHT,WIDTH,HEIGHT))
        pg.draw.rect(self.screen,(0,0,20),pg.Rect(0,0,WIDTH,HALF_HEIGHT))

    def draw_map(self):
        self.map.draw()
        self.player.draw()
        self.raycasting.draw_map()

    def draw(self):
        self.screen.fill('black')
        if self.location == "Main_menu":
            self.main_menu.draw()
            
        elif self.location == "Settings":
            self.settings_menu.draw()
            
        elif self.location == "In_game" and self.map_open == True:
            self.draw_map()
            
        elif self.location == "In_game":
            self.draw_background()
            self.raycasting.draw()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    if self.location == "Main_menu":
                        self.quit()
                    elif self.location == "Settings":
                        self.location = "Main_menu"
                    elif self.location == "Other_Lobby":
                        self.location = "Lobby"
                    elif self.location == "Lobby":
                        self.location = "Main_menu"
                
                if event.key == pg.K_r:
                    self.player.x , self.player.y = PLAYER_POS
                    self.player.angle = 0

                if event.key == pg.K_m:
                    if self.location == "In_game" and self.map_open == False:
                        self.map_open = True
                    else:
                        self.map_open = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.location == "Main_menu":
                    self.main_menu.get_mouse_input()
                
                elif self.location == "Settings":
                    self.settings_menu.get_mouse_input()
    
    def quit(self):
        pg.quit()
        sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

def main():
    game = Game()
    game.run()

main()