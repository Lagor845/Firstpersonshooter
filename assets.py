import pygame

class Colors:
    def __init__(self) -> None:
        self.white = (255,255,255)
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)

class Text:
    def __init__(self,text,font_size,text_color) -> None:
        self.text = text
        self.font_size = font_size
        self.text_color = text_color
        
    
    def update(self,screen,x,y):
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        self.text_structure = font.render(self.text, True, self.text_color)
        self.rect = self.text_structure.get_rect()
        self.rect.center = (x,y)
        screen.blit(self.text_structure,self.rect)