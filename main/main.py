import pygame, sys, time
from setting import *
from level import *

pygame.init() # 초기화

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(screen,level_map_0,level_map_1,level_map_2,level_map_3,level_map_4,level_map_5,level_map_6)

pygame.display.set_caption('The Melancholy of StarGazer')


# 루프 실행
running = True
while running and level.running:

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 

    if level.chick_alive:
        screen.fill('black')
    elif level.chick_alive == False and level.is_level_5: 
        screen.fill((160,0,0))
    level.run()         # 레벨 처리
    pygame.display.update()

    clock.tick(60)

pygame.quit() 
sys.exit()