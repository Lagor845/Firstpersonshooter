import pygame as pg
from Assets.assets import *
from settings import *

# pg.display.toggle_fullscreen()

class Settings_menu:
    def __init__(self,game) -> None:
        self.game = game
        self.screen_width = self.game.screen.get_width()
        self.screen_height = self.game.screen.get_height()
        self.colors = Colors()
        self.back_button = Text("Back",40,self.colors.white)
        self.fullscreen_button = Text("Fullscreen",40,self.colors.white)
        self.mouse_key_control_button = Text("Mouse",40,self.colors.white)
        self.fps_button = Text("Show FPS",40,self.colors.white)
        self.Show_fps = True

    def draw(self):
        self.back_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.3)
        self.fullscreen_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.5)
        self.mouse_key_control_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.8)
        self.fps_button.update(self.game.screen,self.screen_width/2,self.screen_height/2.2)

    def get_mouse_input(self):
        if self.back_button.rect.collidepoint(pg.mouse.get_pos()):
            self.game.location = "Main_menu"
            
        if self.fullscreen_button.rect.collidepoint(pg.mouse.get_pos()):
            if self.game.fullscreen == False:
                self.game.fullscreen = True
                self.fullscreen_button.text = "Windowed"
            else:
                self.game.fullscreen = False
                self.fullscreen_button.text = "Fullscreen"
            pygame.display.toggle_fullscreen()
            
        if self.mouse_key_control_button.rect.collidepoint(pg.mouse.get_pos()):
            if self.mouse_key_control_button.text == "Mouse":
                self.mouse_key_control_button.text = "Arrow keys"
            else:
                self.mouse_key_control_button.text = "Mouse"
        
        if self.fps_button.rect.collidepoint(pg.mouse.get_pos()):
            if self.Show_fps == True:
                self.fps_button.text = "Hide FPS"
                self.Show_fps = False
            else:
                self.fps_button.text = "Show FPS"
                self.Show_fps = True