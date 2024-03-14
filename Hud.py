import pygame as pg 
from Assets.assets import *
from settings import *

class Hud:
    def __init__(self,game) -> None:
        self.game = game
        self.colors = Colors()
        self.screen_width = self.game.screen.get_width()
        self.screen_height = self.game.screen.get_height()
        self.health_bar_width = self.screen_width / 4
        self.health_bar_height = self.screen_height/ 15
        self.health_bar_x = self.game.screen.get_width() / 15
        self.health_bar_y = self.game.screen.get_height() / 1.2
        self.pause_menu_area = "main"
        # Main area
        self.paused_text = Text("Paused",80,self.colors.white)
        self.resume_button = Text("Resume",40,self.colors.white)
        self.settings_button = Text("Settings",40,self.colors.white)
        self.quit_button = Text("Quit",40,self.colors.white)

        # Settings Menu
        self.back_button = Text("Back",40,self.colors.white)
        self.fullscreen_button = Text("Fullscreen",40,self.colors.white)
        self.mouse_key_control_button = Text("Mouse",40,self.colors.white)
        self.fps_button = Text("Show FPS",40,self.colors.white)
        
    def draw(self):
        current_bar_width = (self.game.player.health / 100) * self.health_bar_width
        pg.draw.rect(self.game.screen,self.colors.red,pg.Rect(self.health_bar_x,self.health_bar_y,self.health_bar_width,self.health_bar_height))
        pg.draw.rect(self.game.screen,self.colors.green,pg.Rect(self.health_bar_x,self.health_bar_y,current_bar_width,self.health_bar_height))
    
    def draw_pause_menu(self):
        if self.pause_menu_area == "main":
            self.paused_text.update(self.game.screen,self.screen_width/2,self.screen_height/10)
            self.resume_button.update(self.game.screen,self.screen_width/2,self.screen_height/3)
            self.settings_button.update(self.game.screen,self.screen_width/2,self.screen_height/2)
            self.quit_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.5)
        
        elif self.pause_menu_area == "Settings":
            self.back_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.3)
            self.fullscreen_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.5)
            self.mouse_key_control_button.update(self.game.screen,self.screen_width/2,self.screen_height/1.8)
            self.fps_button.update(self.game.screen,self.screen_width/2,self.screen_height/2.2)
    
    def get_mouse_input(self):
        global Show_fps
        if self.pause_menu_area != "Settings":
            if self.resume_button.rect.collidepoint(pg.mouse.get_pos()):
                self.game.pause_menu_open = False
            elif self.settings_button.rect.collidepoint(pg.mouse.get_pos()):
                self.pause_menu_area = "Settings"
            elif self.quit_button.rect.collidepoint(pg.mouse.get_pos()):
                self.game.leave_game()
        
        else:
            if self.back_button.rect.collidepoint(pg.mouse.get_pos()):
                self.pause_menu_area = "main"

            elif self.fullscreen_button.rect.collidepoint(pg.mouse.get_pos()):
                if self.game.fullscreen == False:
                    self.game.fullscreen = True
                    self.fullscreen_button.text = "Windowed"
                else:
                    self.game.fullscreen = False
                    self.fullscreen_button.text = "Fullscreen"
                pygame.display.toggle_fullscreen()
                
            elif self.mouse_key_control_button.rect.collidepoint(pg.mouse.get_pos()):
                if self.mouse_key_control_button.text == "Mouse":
                    self.mouse_key_control_button.text = "Arrow keys"
                else:
                    self.mouse_key_control_button.text = "Mouse"
            
            elif self.fps_button.rect.collidepoint(pg.mouse.get_pos()):
                if self.game.settings_menu.Show_fps == True:
                    self.fps_button.text = "Hide FPS"
                    self.game.settings_menu.Show_fps = False
                else:
                    self.fps_button.text = "Show FPS"
                    self.game.settings_menu.Show_fps = True