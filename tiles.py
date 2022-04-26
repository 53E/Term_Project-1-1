import pygame
from support import import_folder

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()                         # super().__init__ : super() = pygame.sprite.Sprite 의 변수를 사용하겠다고 선언 casting
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_move):  
        self.rect.x += x_move      # 타일의 x position을 변경함


