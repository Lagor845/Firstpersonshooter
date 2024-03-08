import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *

class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION,pg.HWSURFACE | pg.DOUBLEBUF)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.started = False
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = Raycasting(self)
    
    def update(self):
        self.player.update()
        self.raycasting.update()
        pg.display.update()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f"FPS: {self.clock.get_fps()}")
    
    def draw_background(self):
        pg.draw.rect(self.screen,(0,50,0),(0,HALF_HEIGHT,WIDTH,HEIGHT))
        pg.draw.rect(self.screen,(0,0,20),pg.Rect(0,0,WIDTH,HALF_HEIGHT))
    
    def draw(self):
        self.screen.fill('black')
        self.draw_background()
        """
        self.map.draw()
        self.player.draw()
        """
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                
                if event.key == pg.K_r:
                    self.player.x , self.player.y = PLAYER_POS
                    self.player.angle = 0
        
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

def main():
    game = Game()
    game.run()

main()