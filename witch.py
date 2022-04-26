import pygame
from support import import_folder


class Witch(pygame.sprite.Sprite):       # self.rect / self.image 필요
    def __init__(self,pos):
        super().__init__()
        self.frame_index = 0
        self.anim_speed = 0.075
        self.witch = import_folder('.\\graphics\\npc\\witch')
        self.image = self.witch[int(self.frame_index)]
        self.rect = self.image.get_rect(topleft = pos)
        self.face_right = False

    def animate(self):
        self.frame_index += self.anim_speed
        if self.frame_index > len(self.witch):
            self.frame_index = 0
            
        image_witch = self.witch[int(self.frame_index)]

        if self.face_right == True:
            self.image = image_witch
        else:
            self.image = pygame.transform.flip(image_witch,True,False)


    def update(self,x_move):
        self.animate()
        self.rect.x += x_move