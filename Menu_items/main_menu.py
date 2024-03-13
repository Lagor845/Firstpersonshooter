import pygame as pg
from Assets.assets import *

class Main_Menu:
    def __init__(self,game) -> None:
        self.game = game
        self.screen_width = self.game.screen.get_width()
        self.screen_height = self.game.screen.get_height()
        self.colors = Colors()
        self.start_button = Text("Start",40,self.colors.white)
        self.settings_button = Text("Settings",40,self.colors.white)
        self.quit_button = Text("Quit",40,self.colors.white)
        self.image = pygame.image.load("Assets/Imgs/Title_page.jpg").convert()

    def draw(self):
        self.game.screen.blit(self.image,(0,0))
        self.start_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.5)
        self.settings_button.update(self.game.screen,self.screen_width/2,((self.screen_height/1.1 - self.screen_height/1.5) / 2) + self.screen_height/1.5)
        self.quit_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.1)

    def get_mouse_input(self):
        if self.start_button.rect.collidepoint(pg.mouse.get_pos()):
            self.game.location = "Lobby"
        elif self.settings_button.rect.collidepoint(pg.mouse.get_pos()):
            self.game.location = "Settings"
        elif self.quit_button.rect.collidepoint(pg.mouse.get_pos()):
            self.game.quit()