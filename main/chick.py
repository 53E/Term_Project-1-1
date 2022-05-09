import pygame
from support import import_folder


class Chick(pygame.sprite.Sprite):       # self.rect / self.image 필요
    def __init__(self,pos):
        super().__init__()
        self.frame_index = 0
        self.anim_speed = 0.075
        self.chick = import_folder('.\\graphics\\npc\\chick')
        self.image = self.chick[int(self.frame_index)]
        self.rect = self.image.get_rect(topleft = pos)

    def animate(self):
        self.frame_index += self.anim_speed
        if self.frame_index > len(self.chick):
            self.frame_index = 0
            
        self.image = self.chick[int(self.frame_index)]

    def update(self,x_move):
        self.animate()
        self.rect.x += x_move