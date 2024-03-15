import pygame as pg
import math
from settings import *

class Raycasting:
    def __init__(self,game) -> None:
        self.game = game

    def ray_cast(self):
        ox,oy = self.game.player.pos
        x_map,y_map = self.game.player.map_pos
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        
        # 3d lists
        self.color_list = []
        self.ray_list = []
        self.height_list = []
        
        #2d lists
        self.ox_list = []
        self.oy_list = []
        self.depth_list = []
        self.cos_a_list = []
        self.sin_a_list = []
        
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Horizontals
            y_hor,dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6,-1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy

                depth_hor += delta_depth

            # Verticals
            x_vert,dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6,-1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy

                depth_vert += delta_depth

            if depth_hor > depth_vert:
                depth = depth_vert
            else:
                depth = depth_hor

            self.ox_list.append(ox)
            self.oy_list.append(oy)
            self.depth_list.append(depth)
            self.cos_a_list.append(cos_a)
            self.sin_a_list.append(sin_a)
            # pg.draw.line(self.game.screen,'yellow',(100 * ox,100* oy),(100*ox+100 * depth * cos_a,100*oy+100 * depth * sin_a),2)
            
            depth *= math.cos(self.game.player.angle - ray_angle)

            if depth >= MAX_DEPTH:
                proj_height = 0
            else:
                proj_height = SCREEN_DIST / (depth + 0.0001)

            color = [255 / (1 + depth ** 6 * 0.00002)] * 3
            
            self.height_list.append(proj_height)
            self.color_list.append(color)
            self.ray_list.append(ray)
            # pg.draw.rect(self.game.screen,color,(ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
    
    def draw(self):
        for stuff in range(len(self.ray_list)):
            pg.draw.rect(self.game.screen,self.color_list[stuff],(self.ray_list[stuff] * SCALE, HALF_HEIGHT - self.height_list[stuff] // 2, SCALE, self.height_list[stuff]))
            
    def draw_map(self):
        for stuff in range(len(self.ox_list)):
            pg.draw.line(self.game.screen,'yellow',(self.game.map.distance * self.ox_list[stuff],self.game.map.distance* self.oy_list[stuff]),(self.game.map.distance*self.ox_list[stuff]+self.game.map.distance * self.depth_list[stuff] * self.cos_a_list[stuff],self.game.map.distance*self.oy_list[stuff]+self.game.map.distance * self.depth_list[stuff] * self.sin_a_list[stuff]),2)