import pygame, sys
from button import Button

pygame.init()
pygame.font.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
guide = pygame.image.load("assets/Guide.png")

white = (255, 255, 255)
black = (0, 0, 0)

def get_font(size): 
    return pygame.font.Font("assets/arcadefont.ttf", size)

class Paddle1(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([10, 150])
        self.image.fill((white))
        self.rect = self.image.get_rect()

        self.points = 0

class Paddle2(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([10, 150])
        self.image.fill((white))
        self.rect = self.image.get_rect()

        self.points = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([15, 15])
        self.image.fill((white))
        self.rect = self.image.get_rect()

        self.speed = 10
        self.dx = 1
        self.dy = 1

paddle1 = Paddle1()
paddle1.rect.x = 25
paddle1.rect.y = 250

paddle2 = Paddle2()
paddle2.rect.x = 1255
paddle2.rect.y = 250

paddle_speed = 15

ping = Ball()
ping.rect.x = 640
ping.rect.y = 350

p1_win_condition = False

all_sprites = pygame.sprite.Group()
all_sprites.add(paddle1, paddle2, ping)

 # Title font
font = pygame.font.Font("assets/arcadefont.ttf", 32)

def p1_win_screen():

    while True:
        pygame.init()
        
        p1_win_mouse_pos = pygame.mouse.get_pos()
        paddle1.points = 0
        paddle2.points = 0

        SCREEN.fill(black)

        p1_congrats = font.render('PLAYER 1 WINS!', False, white)
        p1_congrats_rect = p1_congrats.get_rect()
        p1_congrats_rect.center = (1280 // 2, 50)

        SCREEN.blit(p1_congrats, p1_congrats_rect)

        P1_WIN_BACK = Button(image=None, pos=(640, 450), 
                        text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        
        for button in [P1_WIN_BACK]:
            button.changeColor(p1_win_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if P1_WIN_BACK.checkForInput(p1_win_mouse_pos):
                        main_menu()
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def p2_win_screen():

    while True:
        pygame.init()
        
        p2_win_mouse_pos = pygame.mouse.get_pos()
        paddle1.points = 0
        paddle2.points = 0

        SCREEN.fill(black)

        p2_congrats = font.render('PLAYER 2 WINS!', False, white)
        p2_congrats_rect = p2_congrats.get_rect()
        p2_congrats_rect.center = (1280 // 2, 50)

        SCREEN.blit(p2_congrats, p2_congrats_rect)

        P2_WIN_BACK = Button(image=None, pos=(640, 450), 
                        text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        
        for button in [P2_WIN_BACK]:
            button.changeColor(p2_win_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if P2_WIN_BACK.checkForInput(p2_win_mouse_pos):
                        main_menu()
                key = pygame.key.get_pressed()
                if key[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def redraw():

    pygame.init()

    global get_font
    SCREEN.fill(black)

    text = font.render('PING', False, white)
    textRect = text.get_rect()
    textRect.center = (1280 // 2, 40)

    SCREEN.blit(text, textRect)

    # Player 1 Score
    p1_score = font.render(str(paddle1.points), False, white)
    p1Rect = p1_score.get_rect()
    p1Rect.center = (50, 50)

    SCREEN.blit(p1_score, p1Rect)

    # Player 2 Score
    p2_score = font.render(str(paddle2.points), False, white)
    p2Rect = p2_score.get_rect()
    p2Rect.center = (1230, 50)
    SCREEN.blit(p2_score, p2Rect)

    all_sprites.draw(SCREEN)

    pygame.display.update()
    while True:

        ping.speed = 10

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

            #pygame.time.wait(1000)
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            paddle1.rect.y += -paddle_speed
        
        if key[pygame.K_ESCAPE]:
            main_menu()

        if key[pygame.K_s]:
            paddle1.rect.y += paddle_speed

        if key[pygame.K_UP]:
            paddle2.rect.y += -paddle_speed

        if key[pygame.K_DOWN]:
            paddle2.rect.y += paddle_speed

        ping.rect.x += ping.speed * ping.dx
        ping.rect.y += ping.speed * ping.dy

        if ping.rect.y >= 700:
            ping.dy = -1

        if ping.rect.y <= 0:
            ping.dy = 1

        if ping.rect.x > 1270:
            ping.rect.x, ping.rect.y = 1280 / 2, 350
            ping.dx = -1
            paddle1.points += 1

        if ping.rect.x <= 0:
            ping.rect.x, ping.rect.y = 1280 / 2, 350
            ping.dx = 1
            paddle2.points += 1

        if paddle1.rect.colliderect(ping.rect):
            ping.dx = 1

        if paddle2.rect.colliderect(ping.rect):
            ping.dx = -1

        if paddle1.points >= 1:
            ping.speed = 0
            p1_win_screen()
        if paddle2.points >= 1: 
            ping.speed = 0
            p2_win_screen()
            
        PLAY_BACK = Button(image=None, pos=(1160, 60), 
        text_input="BACK", font=get_font(30), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        
        redraw()


pygame.display.update()
    
def options():
    while True:
        SCREEN.blit(guide, (0,0))
        guide_mouse_pos = pygame.mouse.get_pos()



        GUIDE_BACK = Button(image=None, pos=(1160, 600), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")

        GUIDE_BACK.changeColor(guide_mouse_pos)
        GUIDE_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GUIDE_BACK.checkForInput(guide_mouse_pos):
                    main_menu()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            main_menu()

        pygame.display.update()

def main_menu():

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("PING", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="GUIDE", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    redraw()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            main_menu()

        pygame.display.update()

main_menu()