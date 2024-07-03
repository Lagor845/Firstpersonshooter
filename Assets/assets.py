import pygame
import pygame as pg

class Colors:
    def __init__(self) -> None:
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)

class Text:
    def __init__(self,text,font_size,text_color,centered = True) -> None:
        self.text = text
        self.font_size = font_size
        self.text_color = text_color
        self.centered = centered
    
    def update(self,screen,x,y,width = 0,height = 0):
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        self.text_structure = font.render(self.text, True, self.text_color,"red")
        self.rect = self.text_structure.get_rect()
        if self.centered == True:
            self.rect.center = (x,y)
        else:
            self.rect.topleft = [x,y]
            self.rect.width = width
            self.rect.height = height
        screen.blit(self.text_structure,self.rect)
        
class Sounds:
    def __init__(self,game) -> None:
        self.game = game
        self.select = pygame.mixer.Sound("Assets/Sounds/FX/Shotgun.mp3")
        self.battle_music_started = False
        self.menu_music_started = False
        
    def select_sound(self):
        self.select.play()
    
    def start_menu_music(self):
        pygame.mixer_music.load("Assets/Sounds/Music/Title_page.mp3")
        pygame.mixer_music.play(loops=1)
        self.menu_music_started = True
        
    def stop_menu_music(self):
        pygame.mixer_music.stop()
        self.menu_music_started = False
    
    def start_in_game_music(self):
        pygame.mixer_music.load("Assets/Sounds/Music/Theonlythingtheyfear.mp3")
        pygame.mixer_music.play(loops=1)
        self.battle_music_started = True
    
    def stop_in_game_music(self):
        pygame.mixer_music.stop()
        self.battle_music_started = False
        
class Slider:
    def __init__(self,game,centerx,centery,input_rect_width,input_rect_height,out_width,out_height,low_value = 0,high_value = 100,current_value = 100) -> None:
        self.game = game
        
        self.low_value = low_value
        self.high_value = high_value
        self.current_value = current_value
        
        self.input_rect = pg.Rect(0,0,0,0)
        self.input_rect.centerx = centerx
        self.input_rect.centery = centery
        self.input_rect.width = input_rect_width
        self.input_rect.height = input_rect_height
        print(f"centerx: {centerx}, rectcenterx: {self.input_rect.centerx}")
        
        self.out_rect = pg.Rect(0,0,0,0)
        self.out_rect.centerx = centerx
        self.out_rect.centery = centery
        self.out_rect.width = out_width
        self.out_rect.height = out_height
        
        
    def calculate_value(self):
        value = (self.out_rect.right - self.input_rect.centerx) / (self.out_rect.right - self.out_rect.left)
        print(value)
        
    
    def draw(self):
        pg.draw.rect(self.game.screen,"gray",self.out_rect)
        pg.draw.rect(self.game.screen,"red",self.input_rect)
    
    def mouse_input(self):
        if self.input_rect.collidepoint(pg.mouse.get_pos()):
            self.input_rect.centerx = pg.mouse.get_pos()[0]
            if self.input_rect.centerx >= self.out_rect.right:
                self.input_rect.centerx = self.out_rect.right
            if self.input_rect.centerx <= self.out_rect.left:
                self.input_rect.centerx = self.out_rect.left
            self.calculate_value()