import pygame as pg

custom_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

class Map:
    def __init__(self,game) -> None:
        self.game = game
        self.mini_map = custom_map
        self.custom_map = custom_map
        self.world_map = {}
        self.name = "Default"
        self.calculate_distance()
        self.get_map()
        
    def calculate_distance(self):
        if len(self.mini_map[0]) < len(self.mini_map):
            self.distance = self.game.screen.get_width() / len(self.mini_map[0])
        else:
            self.distance = self.game.screen.get_height() / len(self.mini_map)
    
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i,value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value
                    
    def draw(self):
        for pos in self.world_map:
            pg.draw.rect(self.game.screen,'darkgrey',(pos[0] * self.distance,pos[1] * self.distance,self.distance,self.distance),2)