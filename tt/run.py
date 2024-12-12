# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
# 畫布大小
screen = pygame.display.set_mode((1280, 400))
BLACK = (0,0,0)


img_dino = pygame.image.load("dino.png")
img_DinoRun2 = |pygame.image.load("dinorun1.png"),pygame.image.load("dinorun2.png")|
img_cactus = pygame.image.load("cactus.png")
img_dino = pygame.transform.scale(img_dino,(150, 150))
img_cactus = pygame.transform.scale(img_cactus,(40, 40))
# 設定角色
dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 260
is_jumping = False
jump =30
nowjump=jump
g=1
cactus_rect = img_cactus.get_rect()
cactus_rect.x = 1100
cactus_rect.y =360
speed =5
# 設定分數
score = 0
highscore =0#最高紀錄
font = pygame.font.Font(None,36)

clock = pygame.time.Clock()
running = True
gameover = False
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
                    gameover = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_jumping = True
    if not gameover:
    
        if is_jumping:
            dino_rect.y -= nowjump
            nowjump -=g
            if dino_rect.y>260:
                dino_rect.y=260
                nowjump=jump
                is_jumping = False
        cactus_rect.x -= speed
        if cactus_rect.x<0:
            cactus_rect.x=1280


        if dino_rect.colliderect(cactus_rect):
            if score>highscore:
                highscore=score
            gameover =True


        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255,255,255))
        
        score_show = font.render(f"Score: {score}",True, BLACK)
        screen.blit(score_show,(10,10))

        highscore_show = font.render(f"Hi Score: {highscore}",True, BLACK)
        screen.blit(highscore_show,(10,30))

        if gameover:
            gameover_show = font.render(f"GAME OVER",True,BLACK)
            screen.blit(gameover_show,(550,150))
        # RENDER YOUR GAME HERE
        screen.blit(img_dino,dino_rect)
        screen.blit(img_cactus,cactus_rect)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

pygame.quit()