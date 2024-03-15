import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from network import *
from Hud import *
from Menu_items.main_menu import *
from Menu_items.settings_menu import *
from Menu_items.lobby import *
from Assets.assets import *

class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION,pg.FULLSCREEN,pg.HWSURFACE | pg.DOUBLEBUF)
        self.fullscreen = False
        self.started = False
        self.map_open = False
        self.pause_menu_open = False
        self.delta_time = 1
        self.game_timer = 5 * 60 # 5 is the number of minutes while 60 is turning it into seconds
        self.location = "Main_menu"
        self.clock = pg.time.Clock()
        self.import_classes()

    def import_classes(self):
        self.main_menu = Main_Menu(self)
        self.settings_menu = Settings_menu(self)
        self.lobby = Lobby(self)
        self.sound = Sounds(self)
        self.hud = Hud(self)
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = Raycasting(self)
        self.network_handler = Network_Handler(self)

    def update(self):
        if self.location == "In_game":
            if self.sound.battle_music_started == False:
                self.sound.start_in_game_music()
            self.player.update()
            self.raycasting.update()
        pg.display.update()
        self.delta_time = self.clock.tick(FPS)

    def draw_background(self):
        #pg.draw.rect(self.screen,(0,50,0),(0,HALF_HEIGHT,WIDTH,HEIGHT))
        pg.draw.rect(self.screen,(0,0,20),pg.Rect(0,0,WIDTH,HALF_HEIGHT))

    def draw_map(self):
        self.map.draw()
        self.player.draw()
        self.raycasting.draw_map()

    def draw(self):
        self.screen.fill('black')
        
        if self.location == "Main_menu":
            if self.sound.menu_music_started == False:
                self.sound.start_menu_music()
            self.main_menu.draw()
            pg.mouse.set_visible(1)
        
        elif self.location == "Lobby":
            self.lobby.draw()
            pg.mouse.set_visible(1)

        elif self.location == "Settings":
            self.settings_menu.draw()
            pg.mouse.set_visible(1)

        elif self.location == "In_game" and self.pause_menu_open == True:
            self.draw_background()
            self.raycasting.draw()
            self.hud.draw_pause_menu()
            pg.mouse.set_visible(1)
            self.network_handler.draw("map")

        elif self.location == "In_game" and self.map_open == True:
            pg.mouse.set_pos(self.screen.get_width()/2,self.screen.get_height()/2)
            self.draw_map()

        elif self.location == "In_game":
            pg.mouse.set_visible(0)
            pg.mouse.set_pos(self.screen.get_width()/2,self.screen.get_height()/2)
            self.draw_background()
            self.raycasting.draw()
            self.hud.draw()
            self.network_handler.draw("3d")

        if self.settings_menu.Show_fps == True:
            font = pygame.font.Font('freesansbold.ttf', 20)
            text_structure = font.render(f"{int(self.clock.get_fps())}", True, Colors().white)
            rect = text_structure.get_rect()
            rect.center = (self.screen.get_width()/30,self.screen.get_height()/20)
            self.screen.blit(text_structure,rect)

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
                    elif self.location == "In_game":
                        if self.pause_menu_open == True:
                            self.pause_menu_open = False
                        else:
                            self.pause_menu_open = True

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
                
                elif self.location == "Lobby":
                    self.lobby.get_mouse_input()
                
                elif self.location == "In_game" and self.pause_menu_open == True:
                    self.hud.get_mouse_input()
                self.sound.select_sound()
    
    def leave_game(self):
        self.sound.stop_in_game_music()
        self.location = "Main_menu"
        self.player = Player(self)

    def quit(self):
        pg.quit()
        sys.exit()

    def start_game(self):
        self.sound.stop_menu_music()
        self.location = "In_game"

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

def main():
    game = Game()
    game.run()

main()