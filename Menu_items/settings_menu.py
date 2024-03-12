import pygame as pg
from assets import *

# pg.display.toggle_fullscreen()

class Settings_menu:
    def __init__(self,game) -> None:
        self.game = game
        self.screen_width = self.game.screen.get_width()
        self.screen_height = self.game.screen.get_height()
        self.colors = Colors()
        self.back_button = Text("Back",40,self.colors.white)

    def draw(self):
        self.back_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.3)

    def get_mouse_input(self):
        if self.back_button.rect.collidepoint(pg.mouse.get_pos()):
            self.game.location = "Main_menu"