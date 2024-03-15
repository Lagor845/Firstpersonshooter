import pygame as pg
from Assets.assets import *

class Lobby:
    def __init__(self,game) -> None:
        self.game = game
        self.screen_width = self.game.screen.get_width()
        self.screen_height = self.game.screen.get_height()
        self.colors = Colors()
        self.start_button = Text("Start",40,self.colors.white)
        self.back_button = Text("Back",40,self.colors.white)

    def draw(self):
        self.start_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.2)
        self.back_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.1)

    def get_mouse_input(self):
        if self.start_button.rect.collidepoint(pg.mouse.get_pos()):
            self.game.start_game()

        elif self.back_button.rect.collidepoint(pg.mouse.get_pos()):
            self.game.location = "Main_menu"