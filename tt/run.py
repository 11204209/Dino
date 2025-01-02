# Example file showing a basic pygame "game loop"
import pygame
import random 
# pygame setup
pygame.init()

# 畫布大小
screen = pygame.display.set_mode((1280, 400))
BLACK = (0,0,0)

#載入圖片
img_track = pygame.image.load("track.png")
img_dino = pygame.image.load("dino.png")

img_DinoRun1 = pygame.transform.scale(pygame.image.load("dinorun1.png"),(150, 150))
img_DinoRun2 = pygame.transform.scale(pygame.image.load("dinorun2.png"),(150, 150))

img_DinoRun2 = [img_DinoRun1,img_DinoRun2]
img_cactus = pygame.image.load("cactus.png")
img_dino = pygame.transform.scale(img_dino,(150, 150))
img_cactus = pygame.transform.scale(img_cactus,(70,70))

img_dinoduck1 = pygame.transform.scale(pygame.image.load("DinoDuck1.png"),(150, 150))
img_dinoduck2 = pygame.transform.scale(pygame.image.load("DinoDuck2.png"),(150, 150))
img_bird= pygame.image.load("Bird1.png")
img_birdrun= pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")

img_dinoduck =[img_dinoduck1,img_dinoduck2]

img_missile = pygame.image.load("missile.png")
img_missile = pygame.transform.scale(img_missile,(100,50))
# 設定角色
dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 260
is_jumping = False
is_ducking =False
attack = False
jump =22
nowjump=jump
g=0.8
cactus_rect = img_cactus.get_rect()
cactus_rect.x = random.randrange(1280, 3000)
cactus_rect.y =330
initspeed =5

bird_rect =  img_bird.get_rect()
bird_rect.x = random.randrange(1280, 3000)
bird_rect.y =200
initspeed =5
speed=initspeed

missile_rect = img_missile.get_rect()
missile_rect.x = dino_rect.x+50
missile_rect.y = dino_rect.y+50

# 設定分數
score = 0
highscore =0#最高紀錄
font = pygame.font.Font(None,36)

# 設定等級
level =0
speedlist = [5,6,7,8,9]
#設定等級
level =0


clock = pygame.time.Clock()
running = True
gameover = False

frame = 0
lastime=0


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    score += 1
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_jumping = True
                if event.key == pygame.K_r:
                    score =0
                    cactus_rect.x = 1100
                    bird_rect.x = 900
                    gameover = False

                if event.key == pygame.K_v:
                    attack=True   
                    missile_rect.y=dino_rect.y+50
                    missile_rect.x=dino_rect.x+50

                if event.key==pygame.K_DOWN:
                    dino_rect.y=270
                    is_ducking = True

            if event.type == pygame.KEYUP:
                if is_ducking:
                    dino_rect.y=240
                    is_ducking = False
            if event.type == pygame.MOUSEBUTTONDOWN  :
                is_jumping = True
                if gameover:
                    score = 0
                    cactus_rect.x = 1100
                    bird_rect.x = 2000
                    gameover = False
    if not gameover:     
        
        
        if is_jumping:
            dino_rect.y -= nowjump
            nowjump -=g
            if dino_rect.y>260:
                dino_rect.y=260
                nowjump=jump
                is_jumping = False
        cactus_rect.x -= speed
        bird_rect.x -= speed
        if cactus_rect.x<0:
            cactus_rect.x=random.randrange(1280, 3000)
            
        if bird_rect.x < 0:
            bird_rect.x = random.randrange(1280, 3000)
        


        if dino_rect.colliderect(cactus_rect) or dino_rect.colliderect(bird_rect):
            if score>highscore:
                highscore=score
            gameover =True
            speed=initspeed
        
        if score>3000:
          speed = speedlist[3]
          level = 3
        elif score >2000:
          speed = speedlist[2]
          level =2
        elif score >1000:
          speed = speedlist[1]
          level = 1


        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255,255,255))
        screen.blit(img_track,(0,370))# 多加這行
        score_show = font.render(f"Score: {score}",True, BLACK)
        screen.blit(score_show,(10,10))

        highscore_show = font.render(f"Hi Score: {highscore}",True, BLACK)
        screen.blit(highscore_show,(10,30))

        level_show = font.render(f"Level: {level}",True, BLACK)
        screen.blit(level_show,(10,50))

        if attack:
            missile_rect.x +=5
            screen.blit(img_missile,(missile_rect.x,missile_rect.y))
            if missile_rect.colliderect(cactus_rect):
                cactus_rect.x = random.randint(1280, 3000)
                missile_rect.x=1280
                attack = False
            if missile_rect.colliderect(bird_rect):
                bird_rect.x = random.randint(1280, 3000)
                missile_rect.x=1280
                attack = False

        if gameover:
            gameover_show = font.render(f"GAME OVER",True,BLACK)
            screen.blit(gameover_show,(550,150))

         # 更新跑步動畫
        nowtime = pygame.time.get_ticks()
        if nowtime - lastime>300:
            frame = (frame+1)%2 
            lastime = nowtime

        if is_ducking:
           
            screen.blit(img_dinoduck[frame],dino_rect)
        else:
            
            screen.blit(img_DinoRun2[frame],dino_rect)
        # RENDER YOUR GAME HERE
        # screen.blit(img_dino,dino_rect)
        screen.blit(img_cactus,cactus_rect)
        screen.blit(img_birdrun[frame],bird_rect)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

pygame.quit()