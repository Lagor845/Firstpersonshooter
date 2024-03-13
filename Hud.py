import pygame as pg 
from Assets.assets import Colors

class Hud:
    def __init__(self,game) -> None:
        self.game = game
        self.colors = Colors()
        self.health_bar_width = self.game.screen.get_width() / 4
        self.health_bar_height = self.game.screen.get_height() / 15
        self.health_bar_x = self.game.screen.get_width() / 15
        self.health_bar_y = self.game.screen.get_height() / 1.2
        
    def draw(self):
        current_bar_width = (self.game.player.health / 100) * self.health_bar_width
        pg.draw.rect(self.game.screen,self.colors.red,pg.Rect(self.health_bar_x,self.health_bar_y,self.health_bar_width,self.health_bar_height))
        pg.draw.rect(self.game.screen,self.colors.green,pg.Rect(self.health_bar_x,self.health_bar_y,current_bar_width,self.health_bar_height))
    
    def draw_pause_menu(self):
        pass