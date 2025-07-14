import pygame, random, os, sys
from pygame.locals import *

pygame.init()

main_directory = os.path.dirname(__file__)
imagens_directory = os.path.join(main_directory, "imagens")

class MyGameText:
    def __init__(self):
        print("Inicializando biblioteca...")
        
    def create_text(self, msg, size, color, font=None):

        if font == None:
            font = "comicsansms"
            
        font = pygame.font.SysFont(font, size, True, False)
        mensagem = f"{msg}"
        text_formatted = font.render(mensagem, False, color)
        return text_formatted
    
mgt = MyGameText()

# Window Variables
height, width = 600, 600
isRunning = False
inicial = True
game_over = False

# Game Variables
fps = 60
fps2 = 20

points = 0
miss = 0

# Player Variables
x = random.randint(25, 576)
y = 50
hp = 3
container_size = 180

max_speed = 30
vel = 10

# Base Variables
baseX = 100
baseY = 525

cursorX = 100
cursorY = 100

icon = pygame.image.load(os.path.join(imagens_directory, 'RainbowBall.png'))

window = pygame.display.set_mode((height, width))
pygame.display.set_caption("Atlas")
pygame.display.set_icon(icon)

# imagens
sky = pygame.image.load(os.path.join(imagens_directory, 'Sky_Background.png'))
sky = pygame.transform.scale(sky, (320*3.2, 256*3))

ball = pygame.image.load(os.path.join(imagens_directory, 'Star.png')).convert_alpha()
ball = pygame.transform.scale(ball, (1024//20, 977//20))

base = pygame.image.load(os.path.join(imagens_directory, 'cloud.png')).convert_alpha()
base = pygame.transform.scale(base, (17*6, 10*3.5))

sun = pygame.image.load(os.path.join(imagens_directory, 'TheSun.png')).convert_alpha()
sun = pygame.transform.scale(sun, (2388//8, 1668//8))

logo = pygame.image.load(os.path.join(imagens_directory, 'Atlas_logo.png')).convert_alpha()
logo = pygame.transform.scale(logo, (236*2, 96*2))
logo_rect = logo.get_rect(center=(height//2, 150))

play_button = pygame.image.load(os.path.join(imagens_directory, 'Play_button.png')).convert_alpha()
play_button = pygame.transform.scale(play_button, (256//1.2, 112//1.2))
play_button_rect = play_button.get_rect(center=(height//2, 375))

exit_button = pygame.image.load(os.path.join(imagens_directory, 'Exit_button.png')).convert_alpha()
exit_button = pygame.transform.scale(exit_button, (256//1.2, 112//1.2))
exit_button_rect = exit_button.get_rect(center=(height//2, 500))

life_img = pygame.image.load(os.path.join(imagens_directory, "Atlas_HP.png")).convert_alpha()
life_img = pygame.transform.scale(life_img, (180,56))

clock = pygame.time.Clock()

hover = False

while inicial == True:
    clock.tick(fps2)
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
    XeY = pygame.mouse.get_pos()
    window.fill((255,255,255))
    os.system('cls')

    if hover == True:
        ball = pygame.transform.rotate(ball, 90)

    for event in pygame.event.get():
            if event.type == QUIT:
                isRunning = False
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    isRunning = False
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(XeY[0], XeY[1]):
                    inicial = False
                    isRunning = True
                
                if exit_button_rect.collidepoint(XeY[0], XeY[1]):
                    inicial = False
                    pygame.quit()
                    sys.exit()

            cursorX = XeY[0]
            cursorY = XeY[1]

            if play_button_rect.collidepoint(XeY[0], XeY[1]):
                hover = True
            elif exit_button_rect.collidepoint(XeY[0], XeY[1]):
                hover = True
            else: 
                hover = False

    window.blit(sky, (-100,0))
    window.blit(logo, logo_rect)
    window.blit(play_button, play_button_rect)
    window.blit(exit_button, exit_button_rect)
    window.blit(ball, (cursorX, cursorY))
    pygame.display.flip()

while isRunning == True:
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
    clock.tick(fps)
    window.fill((255,255,255))
    life_img_frame = life_img.subsurface(0,0,container_size,56).convert_alpha()
    os.system('cls')
    text_points = mgt.create_text(f"Points: {points}", 25, (0,0,0))
    text_speed = mgt.create_text(f"Speed: {round(vel)}", 25, (0,0,0))
    text_missed = mgt.create_text(f"Missed: {miss}", 25, (0,0,0))

    ball_rect = ball.get_rect(center=(x, y))
    base_rect = base.get_rect(center=(baseX, baseY))

    if hp == 0:
        isRunning = False
        game_over = True

    y += round(vel)

    if y >= width:
        x = random.randint(25, 576)
        y = 100
        miss += 1
        hp -= 1
        container_size -= 60

    if ball_rect.colliderect(base_rect):
        x = random.randint(25, 576)
        y = 100
        points += 1
        if vel >= max_speed:
            vel += 0
        else:
            vel += 0.1
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
                pygame.quit()
                sys.exit()

        if event.type == MOUSEMOTION:
            varX, varY = pygame.mouse.get_pos()
            baseX = varX

    window.blit(sky, (-100,0))
    window.blit(sun, (height-175,-65))
    window.blit(life_img_frame, (5,10))
    window.blit(text_points, (0,75))
    window.blit(text_speed, (0,100))
    window.blit(text_missed, (0,125))
    window.blit(ball, ball_rect)
    window.blit(base, base_rect)
    pygame.display.flip()
        
while game_over == True:
    text_game_over = mgt.create_text(f"FIM DE JOGO", 75, (255,0,0))
    max_points = mgt.create_text(f"Pontuação Maxima foi: {points}", 35, (255,0,0))
    pygame.event.set_grab(True)
    pygame.mouse.set_visible(False)
    clock.tick(fps)
    sky = sky.convert()
    sky.set_alpha(50)
    window.fill((0,0,0))
    window.blit(sky, (-100,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            isRunning = False
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                isRunning = False
                pygame.quit()
                sys.exit()

    window.blit(text_game_over, (30, 150))
    window.blit(max_points, (90, 250))
    pygame.display.flip()