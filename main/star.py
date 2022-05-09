import pygame
from support import import_folder
import random


class Star(pygame.sprite.Sprite):       # self.rect / self.image 필요
    def __init__(self,pos):
        super().__init__()
        self.frame_index = 0
        self.anim_speed = (random.randrange(2,8)) * 0.010
        self.star = import_folder('.\\graphics\\npc\\star')
        self.image = self.star[int(self.frame_index)]
        self.rect = self.image.get_rect(topleft = pos)

    def animate(self):
        self.frame_index += self.anim_speed
        if self.frame_index > len(self.star):
            self.frame_index = 0
            
        self.image = self.star[int(self.frame_index)]


    def update(self,x_move):
        self.animate()
        self.rect.x += x_move