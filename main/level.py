import pygame
from support import import_folder
from tiles import Tile
from setting import tile_size , screen_width , screen_height
from player import Player , player_speed
from particles import Particle
from witch import Witch
from coin import Coin
from chick import Chick
from star import Star
from emerald import Emerald

class Level:
    def __init__(self,surface,level_data_0,level_data_1,level_data_2,level_data_3,level_data_4,level_data_5):
        # 레벨 셋업
        self.level_data = level_data_0          # level_data 를 변경시켜주고 restart하면 맵 전환
        self.level_data_1 = level_data_1
        self.level_data_2 = level_data_2
        self.level_data_3 = level_data_3
        self.level_data_4 = level_data_4
        self.level_data_5 = level_data_5

        self.is_level_1 = False
        self.is_level_2 = False
        self.is_level_3 = False
        self.is_level_4 = False
        self.is_level_5 = False
        self.display_surface = surface
        self.setup_level(level_data_0)   # level 불러오기
        self.world_shift = 0
        self.world_shift_y = 0
        self.current_x = 0
        self.level_count = 1

        # player
        self.jump_count = 100
        self.super_jump = True


        # text
        self.is_welcome = True
        self.font_title = pygame.font.Font('.\\font\\DungeonFont.ttf',35)
        self.font_info = pygame.font.Font('.\\font\\04B.ttf',25)
        self.font_name = pygame.font.Font('.\\font\\DungeonFont.ttf',20)
        self.font_npc  = pygame.font.Font('.\\font\\Minecraft.ttf',17)
        self.font_npc_title = pygame.font.Font('.\\font\\DungeonFont.ttf',22)

        self.text_x = 90

        # sound
        self.bgm_8bit = pygame.mixer.Sound('.\\sound\\bgm\\bgm_8bit.wav')
        self.bgm_loby = pygame.mixer.Sound('.\\sound\\bgm\\loby.wav')
        self.horror_sound = pygame.mixer.Sound('.\\sound\\horror\\1.wav')
        self.horror_sound.set_volume(0.2)
        self.bgm()

        # particle
        self.particle_sprite = pygame.sprite.Group()
        
        #credit
        self.credit_image = pygame.image.load('.\\graphics\\credit\\credit.png')
          


    # level_data 셋업 (행과 열을 나눠 각 셀에 할당)
    def setup_level(self,layout):   
        self.tiles = pygame.sprite.Group()  # 타일 그룹 생성 
        self.player = pygame.sprite.GroupSingle()   # 플레이어 그룹 생성
        self.witch = pygame.sprite.GroupSingle()  # npc 그룹 생성
        self.chick = pygame.sprite.GroupSingle()
        self.star = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()       # coin 그룹 생성
        self.emeralds = pygame.sprite.Group()

        for row_index, row in enumerate(layout):  # 각 행에 숫자를 매김 return(숫자,행)
            for col_index, cell in enumerate(row):   # 각 행을 가져와서 그 행의 열에 숫자를 매김
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x,y),tile_size,tile_size)
                    self.tiles.add(tile)
                if cell =='x':  # 반칸
                    tile = Tile((x,y + (tile_size / 2)),tile_size,tile_size / 2)
                    self.tiles.add(tile)
                elif cell == "P":
                    player_class = Player((x,y),self.display_surface,self.create_jump_particle,self.create_fall_jump_paricle)     # player 생성, 함수가져가기
                    self.player.add(player_class)
                elif cell == "W":
                    witch_class = Witch((x,y-15))
                    self.witch.add(witch_class)
                elif cell == "C":
                    coin = Coin((x+(tile_size/3),y))
                    self.coins.add(coin)
                elif cell == 'E':
                    emerald = Emerald((x,y))
                    self.emeralds.add(emerald)
                elif cell == 'H':
                    chick_class = Chick((x,y+17))
                    self.chick.add(chick_class)
                elif cell == 'S':
                    star_class = Star((x,y))
                    self.star.add(star_class)


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
                    player.on_left = True
                    self.current_x = player.rect.left
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
 
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
        

    # 추락처리
    def fall(self):
        player = self.player.sprite
        if player.rect.y > screen_height + 100:
            player.is_restart = True
            self.restart()
            
    #interface
    def interface(self):
        player = self.player.sprite
        # jumpcount
        self.jump_text = self.font_info.render(str(player.jump_count),True,('white'))
        self.display_surface.blit(self.jump_text,(1425,30))
        self.jump_text = self.font_info.render('JUMP COUNT :',True,('white'))
        self.display_surface.blit(self.jump_text,(1250,30))
        # superjump
        self.can_superjump = 'True'
        if player.can_super_jump:
            self.can_superjump = "True"
        else:
            self.can_superjump = "False"

        self.superjump_text = self.font_info.render(self.can_superjump,True,('white'))
        self.display_surface.blit(self.superjump_text,(1425,80))
        self.superjump_text = self.font_info.render('SUPER JUMP :',True,('white'))
        self.display_surface.blit(self.superjump_text,(1250,80))
        self.superjump_text = self.font_info.render('RESTART : R',True,('white'))
        self.display_surface.blit(self.superjump_text,(1250,130))


    
    # level_text
    def level_text(self,x):
        player = self.player.sprite

        if self.is_welcome:
            self.text_x += x
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
            self.display_surface.blit(self.welcome_text,(self.text_x ,750))
            self.welcome_text = self.font_info.render('ESC - QUIT',True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x ,850))
            self.welcome_text = self.font_name.render("JIN WOO CHOI",True,('black'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 100,880))
            self.welcome_text = self.font_npc_title.render("Look at the stars ...",True,('red'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 2030 ,620))
            self.welcome_text = self.font_npc_title.render("isnt it beatiful ?",True,('red'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 2080 ,650))
            self.welcome_text = self.font_npc.render('When i look at the stars ...',True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 4090 ,680))
            self.welcome_text = self.font_npc.render("It's kind of scary",True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 4120 ,710))
            self.welcome_text = self.font_npc.render("You think so, Don't you ?",True,('red'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 4090 ,750))

        if self.is_level_1:
            self.text_x += x
            self.welcome_text = self.font_title.render('GOOD. . . LUCK. . . . .',True,(255,0,0))
            self.display_surface.blit(self.welcome_text,(self.text_x - 290,20))
            self.welcome_text = self.font_npc.render('You  have  limited  JUMP  COUNT',True,('yellow'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 500 ,720))
            self.welcome_text = self.font_npc.render('PRESS  S',True,('yellow'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 1000 ,720))
            self.welcome_text = self.font_npc.render('you can SUPER JUMP !!',True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 950 ,770))
            self.welcome_text = self.font_npc.render('you can DOUBLE JUMP !!',True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 1890 ,720))
            self.welcome_text = self.font_npc.render('DOUBLE JUMP on air',True,('yellow'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 1900 ,770))
            self.welcome_text = self.font_npc.render('not counted',True,('yellow'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 1940 ,790))
            self.welcome_text = self.font_npc.render('PRESS  R',True,('yellow'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 2550 ,600))
            self.welcome_text = self.font_npc.render('you can RESTART',True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 2520 ,640))
            self.welcome_text = self.font_npc.render('This is beautiful ?',True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 3560 ,730))
            self.welcome_text = self.font_npc.render("... You're joking, right ? ",True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x + 3540 ,760))
        
        if self.is_level_2:
            self.text_x += x
            self.welcome_text = self.font_npc.render("what are those shiny thing ?",True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x - 60 ,20))
            self.welcome_text = self.font_npc.render(". . . . . look kind of sad",True,('white'))
            self.display_surface.blit(self.welcome_text,(self.text_x - 30 ,50))

    # level clear
    def get_emerald(self):                
        player = self.player.sprite

        for emerald in self.emeralds:
            if emerald.rect.colliderect(player.rect):
                self.horror_sound.play()
                if self.level_count == 1:
                    player.is_restart = True
                    self.level_clear_0()
                    self.bgm_loby.stop()
                    self.level_count += 1
                    self.bgm()
                    emerald.kill()
                elif self.level_count == 2:
                    player.is_restart = True
                    self.level_clear_1()
                    self.level_count += 1
                    emerald.kill()
                elif self.level_count == 3:
                    player.is_restart = True
                    self.level_clear_2()
                    self.level_count += 1
                    emerald.kill()
                elif self.level_count == 4:
                    player.is_restart = True
                    self.level_clear_3()
                    self.level_count += 1
                    emerald.kill()
                elif self.level_count == 4:
                    player.is_restart = True
                    self.level_clear_4()
                    self.level_count += 1
                    emerald.kill()

    # 게임 restart
    def restart(self):
        player = self.player.sprite
        if player.is_restart == True:
            self.setup_level(self.level_data)
            self.text_x = 90                            # text 움직여주기
            player = self.player.sprite
            player.jump_count = self.jump_count
            player.can_super_jump = self.super_jump
            player.is_restart = False

    # level clear ---------------------------------------------------------------------------------------------------
    def level_clear_0(self):    
        player = self.player.sprite
        if player.is_restart == True:

            self.is_level_1 = True    #text 처리
            self.is_welcome = False
            self.text_x = 90

            self.level_data = self.level_data_1
            self.setup_level(self.level_data)
            player = self.player.sprite                # !!! setup_level 하면 플레이어가 초기화 즉 위에있는 player는 다른 객체 다시 만들어준다!!!#
            self.jump_count = 2
            pygame.display.set_caption('Level_1')
            player.jump_count = self.jump_count
            player.is_restart = False

    def level_clear_1(self):    
        player = self.player.sprite
        if player.is_restart == True:
            
            self.is_level_1 = False
            self.is_level_2 = True    #text 처리
            self.text_x = 90

            self.level_data = self.level_data_2
            self.setup_level(self.level_data)
            player = self.player.sprite                
            self.jump_count = 7
            self.super_jump = False
            player.can_super_jump = False
            pygame.display.set_caption('Level_2')
            player.jump_count = self.jump_count
            player.is_restart = False

    def level_clear_2(self):    
        player = self.player.sprite
        if player.is_restart == True:
            
            
            self.is_level_2 = False    #text 처리
            self.is_level_3 = True
            self.text_x = 90

            self.level_data = self.level_data_3
            self.setup_level(self.level_data)
            player = self.player.sprite                
            self.jump_count = 7
            self.super_jump = True
            player.can_super_jump = True
            pygame.display.set_caption('Level_3')
            player.jump_count = self.jump_count
            player.is_restart = False
    
    def level_clear_3(self):    
        player = self.player.sprite
        if player.is_restart == True:
            
            
            self.is_level_3 = False    #text 처리
            self.is_level_4 = True
            self.text_x = 90

            self.level_data = self.level_data_4
            self.setup_level(self.level_data)
            player = self.player.sprite                
            self.jump_count = 7
            self.super_jump = True
            player.can_super_jump = True
            pygame.display.set_caption('Level_4')
            player.jump_count = self.jump_count
            player.is_restart = False
    
    def level_clear_4(self):    
        player = self.player.sprite
        if player.is_restart == True:
            
            
            self.is_level_4 = False    #text 처리
            self.is_level_5 = True
            self.text_x = 90

            self.level_data = self.level_data_5
            self.setup_level(self.level_data)
            player = self.player.sprite                
            self.jump_count = 7
            self.super_jump = True
            player.can_super_jump = True
            pygame.display.set_caption('Level_5')
            player.jump_count = self.jump_count
            player.is_restart = False
    #----------------------------------------------------------------------------------------------------------------

    def bgm(self):
        if self.level_count == 1:
            self.bgm_loby.play(-1)
        else:
            self.bgm_8bit.play(-1)



    def credit(self):
        player = self.player.sprite

        if player.is_credit == True:
            self.display_surface.blit(self.credit_image,(0,0))
            player.can_move = False
        
        


    def run(self):

        #particle
        self.particle_sprite.update(self.world_shift)
        self.particle_sprite.draw(self.display_surface)
        
        # level
        self.tiles.update(self.world_shift)    # Group.draw(screen)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        self.restart()
        self.fall()

        #star
        self.star.update(self.world_shift)
        self.star.draw(self.display_surface)

        #text
        self.interface()
        self.level_text(self.world_shift)

        
        #coin
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.get_coin()
        self.scroll_x()

        #emerald
        self.emeralds.update(self.world_shift)
        self.emeralds.draw(self.display_surface)
        self.get_emerald()
        self.scroll_x()

        # witch
        self.witch_face()
        self.witch.update(self.world_shift)
        self.witch.draw(self.display_surface)

        #chick
        self.chick.update(self.world_shift)
        self.chick.draw(self.display_surface)
        
        
        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        #credit
        self.credit()
        
