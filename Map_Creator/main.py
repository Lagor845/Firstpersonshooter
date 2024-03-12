import pygame as pg

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
        font = pg.font.Font('freesansbold.ttf', self.font_size)
        self.text_structure = font.render(self.text, True, self.text_color)
        self.rect = self.text_structure.get_rect()
        self.rect.center = (x,y)
        screen.blit(self.text_structure,self.rect)

width = int(input("Width: "))
height = int(input("Height: "))

pg.init()

screen = pg.display.set_mode((0,0),pg.FULLSCREEN,pg.HWSURFACE | pg.DOUBLEBUF)
clock = pg.time.Clock()

if height <= width:
    actual_width = screen.get_height() / height / 1.05
else:
    actual_width = screen.get_width() / width

squares = []
for y in range(height):
    temp = []
    for x in range(width):
        temp.append(pg.Rect(x*actual_width,y*actual_width,actual_width,actual_width))
    squares.append(temp)

values = []
for y in range(height):
    temp = []
    for x in range(width):
        temp.append(0)
    values.append(temp)

# Buttons
save_button = Text("Save",40,Colors().white)

running = True
while running:
    screen.fill(Colors().black)
    save_button.update(screen,screen.get_width()/2,screen.get_height()/1.05)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pass

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            for y in range(len(squares)):
                for x in range(len(squares[0])):
                    if squares[y][x].collidepoint(pg.mouse.get_pos()):
                        if values[y][x] == 0:
                            values[y][x] = 1
                        else:
                            values[y][x] = 0
                
            if save_button.rect.collidepoint(pg.mouse.get_pos()):
                pass

    for y in range(len(squares)):
        for x in range(len(squares[0])):
            if values[y][x] == 1:
                pg.draw.rect(screen,Colors().green,squares[y][x])
    
    pg.display.update()