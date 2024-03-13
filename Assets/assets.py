import pygame

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