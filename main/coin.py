import pygame
from support import import_folder

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()                         # super().__init__ : super() = pygame.sprite.Sprite 의 변수를 사용하겠다고 선언 casting
        self.frame_index = 0
        self.anim_speed = 0.175
        self.coin = import_folder('.\\graphics\\object\\coin')
        self.image = self.coin[int(self.frame_index)]
        self.rect = self.image.get_rect(topleft = pos)

    def animate(self):
        self.frame_index += self.anim_speed
        if self.frame_index > len(self.coin):
            self.frame_index = 0
            
        self.image = self.coin[int(self.frame_index)]
    
    def update(self,x_move):
        self.animate()  
        self.rect.x += x_move      # 타일의 x position을 변경함
