import pygame, sys
pygame.init()

screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Title')
clock = pygame.time.Clock()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()                         # super().__init__ : super() = pygame.sprite.Sprite 의 변수를 사용하겠다고 선언 casting
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

tile_ex = Tile((50,50),100)
tile_group = pygame.sprite.Group()
tile_group.add(tile_ex)






running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
 

    screen.fill('black')
    tile_group.draw(screen)
    pygame.display.update()
    clock.tick(60)

    