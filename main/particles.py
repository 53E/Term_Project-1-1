import pygame
from support import import_folder

class Particle(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        self.frame_index = 0
        self.animation_speed = 0.25
        if type == 'jump':
            self.frames = import_folder('.\\graphics\\character\\particles\\jump')
            self.animation_speed = 0.25
        if type == 'land':
            self.frames = import_folder('.\\graphics\\character\\particles\\land')
            self.animation_speed = 0.25
        if type == 'fall_jump':
            self.frames = import_folder('.\\graphics\\character\\particles\\fall_jump')
            self.animation_speed = 0.15
        if  type == 'super_jump':
            self.frames = import_folder('.\\graphics\\character\\particles\\super_jump')
            self.animation_speed = 0.02

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()                                # kill() 해당 sprite 그룹을 삭제
        else:
            self.image = self.frames[int(self.frame_index)]


    def update(self,x_shift):
        self.animate()
        self.rect.x += x_shift           # static particle 고정된 파티클이니 scroll 되면 같이 움직이기
