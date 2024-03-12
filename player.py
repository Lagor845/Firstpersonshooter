from settings import *
import pygame as pg
import math

class Player:
    def __init__(self,game) -> None:
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.name = PLAYER_NAME
        self.health = PLAYER_MAX_HEALTH
        self.number = 1
        
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx,dy = 0,0
        keys = pg.key.get_pressed()
        if keys[pg.K_LSHIFT]:
            speed = PLAYER_SPEED * 1.5 * self.game.delta_time
        else:
            speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
            
        if keys[pg.K_s]:
            dx -= speed_cos
            dy -= speed_sin
            
        if keys[pg.K_a]:
            dx += speed_cos
            dy -= speed_sin
            
        if keys[pg.K_d]:
            dx -= speed_cos
            dy += speed_sin
        
        self.check_wall_collision(dx,dy)
        
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
        
        
    def check_wall(self,x,y):
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self,dx,dy):
        if self.check_wall(int(self.x + dx),int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x),int(self.y + dx)):
            self.y += dy
        
    def draw(self):
        pg.draw.circle(self.game.screen,'green', (self.x * self.game.map.distance, self.y * self.game.map.distance),10)
        
    def update(self):
        self.movement()
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)