from distutils.spawn import spawn
from pickletools import pybytes
from re import S, T
import pygame
from tiles import Tile
from setting import tile_size , screen_width , screen_height
from player import Player , player_speed
from particles import Particle
from witch import Witch
from coin import Coin

class Level:
    def __init__(self,level_data,surface):
        # 레벨 셋업
        self.level_data = level_data
        self.display_surface = surface
        self.setup_level(level_data)   # level 불러오기
        self.world_shift = 0
        self.world_shift_y = 0
        self.current_x = 0

        # text
        self.font_title = pygame.font.Font('.\\font\\DungeonFont.ttf',35)
        self.font_info = pygame.font.Font('.\\font\\04B.ttf',25)
        self.font_name = pygame.font.Font('.\\font\\DungeonFont.ttf',20)
        self.text_x = 90

        # particle
        self.particle_sprite = pygame.sprite.Group()


    # level_data 셋업 (행과 열을 나눠 각 셀에 할당)
    def setup_level(self,layout):   
        self.tiles = pygame.sprite.Group()  # 타일 그룹 생성 
        self.player = pygame.sprite.GroupSingle()   # 플레이어 그룹 생성
        self.witch = pygame.sprite.GroupSingle()  # npc 그룹 생성
        self.coins = pygame.sprite.Group()       # coin 그룹 생성

        for row_index, row in enumerate(layout):  # 각 행에 숫자를 매김 return(숫자,행)
            for col_index, cell in enumerate(row):   # 각 행을 가져와서 그 행의 열에 숫자를 매김
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                elif cell == "P":
                    player_class = Player((x,y),self.display_surface,self.create_jump_particle,self.create_fall_jump_paricle)     # player 생성, 함수가져가기
                    self.player.add(player_class)
                elif cell == "W":
                    witch_class = Witch((x,y-15))
                    self.witch.add(witch_class)
                elif cell == "C":
                    coin = Coin((x,y),tile_size)
                    self.coins.add(coin)


    def create_jump_particle(self,pos):
        jump_particle_sprite = Particle(pos,'jump')
        self.particle_sprite.add(jump_particle_sprite)

    def create_fall_jump_paricle(self,pos):
        jump_particle_sprite = Particle(pos,'fall_jump')
        self.particle_sprite.add(jump_particle_sprite)
    


    # player 가 맵 끝으로 이동하면 player.speed =0 맵이 반대방향으로 이동! 그럼 플레이어의 카메라가 움직이는 효과
    def scroll_x(self):                  
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = player_speed
            player.speed = 0
        elif player_x > screen_width -(screen_width / 4) and direction_x > 0:
            self.world_shift = -player_speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = player_speed



    # x축 플레이어 콜리전 설정 
    def horizontal_movement_collision(self): 
        player = self.player.sprite                           # player 움직임 rect.x += ?
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles:
            if sprite.rect.colliderect(player.rect):    # colliderect 함수 - rect끼리의 충돌 체크
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
 
    # y축 플레이어 콜리전 설정
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()      # 중력은 계속 계속 더해짐

        for sprite in self.tiles:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0                # 땅에 가만히 있으면 중력이 계속 증가되는 것을 막기위해 dirction.y을 계속 0으로 반환
                    player.can_jump = True                # 땅에 닿으면 점프가능
                    player.on_ground = True
                    player.can_double_jump = False
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

        if player.on_ground and player.direction.y > 1 or player.direction.y < 0:
            player.on_ground = False

    def get_coin(self):
        player = self.player.sprite

        for coin in self.coins:
            if coin.rect.colliderect(player.rect):
                player.can_super_jump = True
                coin.kill()
        
    def witch_face(self):
        player = self.player.sprite
        witch = self.witch.sprite
        if player.rect.x > witch.rect.x:
            witch.face_right = True
        else:
            witch.face_right = False

    # Welecom TEXT
    def welcome(self,x):
        self.text_x += x
        player = self.player.sprite

        self.welcome_text = self.font_title.render('The Melancholy',True,(255,0,0))
        self.display_surface.blit(self.welcome_text,(self.text_x,100))
        self.welcome_text = self.font_title.render('of StarGazer',True,(255,0,0))
        self.display_surface.blit(self.welcome_text,(self.text_x + 20,150))
        self.welcome_text = self.font_info.render('SPACE - JUMP',True,('white'))
        self.display_surface.blit(self.welcome_text,(self.text_x ,250))
        self.welcome_text = self.font_info.render('S - SUPER JUMP',True,('white'))
        self.display_surface.blit(self.welcome_text,(self.text_x ,350))
        self.welcome_text = self.font_info.render('A - ATTACK',True,('white'))
        self.display_surface.blit(self.welcome_text,(self.text_x ,450))
        self.welcome_text = self.font_info.render('R - RESTART',True,('white'))
        self.display_surface.blit(self.welcome_text,(self.text_x ,550))
        self.welcome_text = self.font_info.render('TAB - CREDIT',True,('white'))
        self.display_surface.blit(self.welcome_text,(self.text_x ,650))
        self.welcome_text = self.font_info.render('ESC - QUIT',True,('white'))
        self.display_surface.blit(self.welcome_text,(self.text_x ,750))
        self.welcome_text = self.font_name.render("JIN WOO CHOI",True,('black'))
        self.display_surface.blit(self.welcome_text,(self.text_x + 100,800))


    # 게임 restart
    def restart(self):
        player = self.player.sprite
        if player.is_restart == True:
            self.setup_level(self.level_data)
            self.text_x = 90                            # text 움직여주기
            player.is_restart = False


    def run(self):

        #particle
        self.particle_sprite.update(self.world_shift)
        self.particle_sprite.draw(self.display_surface)
        
        # level
        self.tiles.update(self.world_shift)    # Group.draw(screen)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.restart()

        #text
        self.welcome(self.world_shift)
        
        #coin
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.get_coin()
        self.scroll_x()

        # witch
        self.witch_face()
        self.witch.update(self.world_shift)
        self.witch.draw(self.display_surface)
        
        
        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        
