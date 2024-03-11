import pygame as pg
from assets import *

class Main_Menu:
    def __init__(self,game) -> None:
        self.game = game
        self.screen_width = self.game.screen.get_width()
        self.screen_height = self.game.screen.get_height()
        self.colors = Colors()
        self.start_button = Text("Start",40,self.colors.white)
        self.settings_button = Text("Settings",40,self.colors.white)
        self.quit_button = Text("Quit",40,self.colors.white)

    def draw(self):
        self.start_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.8)
        self.settings_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.5)
        self.quit_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.3)