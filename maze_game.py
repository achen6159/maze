# Imports
import pygame
import intersects
import time

# Initialize game engine
pygame.init()

#Images
leopard = pygame.image.load('snow_leopard2.png')

# Window
WIDTH = 800

HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "The Beautiful Maze Game"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PINK = (237, 23, 176)
BRIGHT_BLUE = (39, 172, 244)
PURPLE = (164, 66, 244)
BRIGHT_GREEN = (80, 244, 66)
ORANGE = (255, 125 , 0)
FRONT_BLUE = (176, 196, 232)
GREY_BLUE = (29, 77, 155)


# make walls
wall1 = [100, 275, 700, 25]
wall2 = [500, 275, 25, 200]
wall3 = [100, 100, 25, 200]
wall4 = [0, 0, 400, 25]
wall5 = [460, 0, 400, 25]
wall6 = [775, 20, 25, 275]
wall7 = [775, 375, 25, 250]
wall8 = [0, 0, 25, 300]
wall9 = [0, 375, 25, 250]
wall10 = [25, 575, 350, 25]
wall11 = [450, 575, 340, 25]
wall12 = [100, 300, 25, 250]
wall13 = [250, 450, 250, 25]
wall14 = [250, 350, 25, 100]
wall15 = [600, 100, 25, 150]
wall16 = [600, 150, 175, 25]
wall17 = [450, 0, 25, 150]
wall18 = [450, 150, 50, 25]
wall19 = [375, 0, 25, 150]
wall20 = [350, 150, 50, 25]
wall21 = [475, 175, 25, 50]
wall22 = [350, 175, 25, 50]


walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9,\
         wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17,\
         wall18, wall19, wall20, wall21, wall22]


# Sound Effects

coin = pygame.mixer.Sound("sounds/coin.ogg")
bad_coin = pygame.mixer.Sound("sounds/bad_coin.ogg")

# Fonts
MY_FONT = pygame.font.Font(None, 50)

# stages
START = 0
PLAYING = 1
END = 2


def setup():
    global stage, player1, vel1, player1_speed, score1,\
           player2, vel2, player2_speed, score2, coins,\
           bad_coins, win

    win = False
    # Make a player
    player1 =  [200, 150, 25, 25]
    vel1 = [0, 0]
    player1_speed = 5
    score1 = 0

    player2 = [250, 150, 25, 25]
    vel2 = [0, 0]
    player2_speed = 5
    score2 = 0

    # Make coins
    coin1 = [300, 500, 25, 25]
    coin2 = [400, 200, 25, 25]
    coin3 = [150, 150, 25, 25]
    coin4 = [500, 100, 25, 25]
    coin5 = [200, 400, 25, 25]
    coin6 = [550, 400, 25, 25]
    coin7 = [400, 400, 25, 25]
    coin8 = [300, 75, 25, 25]
    coin9 = [600, 500, 25, 25]
    coin10 = [550, 100, 25, 25]
    coin11 = [50, 250, 25, 25]
    coin12 = [700, 60, 25, 25]
    coin13 = [650, 200, 25, 25]
    coin14 = [675, 450, 25, 25]
    coin15 = [150, 350, 25, 25]
    coin16 = [50, 450, 25, 25]

    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9,\
             coin11, coin12, coin13, coin14, coin15, coin16]

    bad_coin1 = [250, 500, 25, 25]
    bad_coin2 = [550, 200, 25, 25]
    bad_coin3 = [225, 50, 25, 25]
    bad_coin4 = [650, 375, 25, 25]
    bad_coin5 = [300, 550, 25, 25]
    bad_coins6 = [70, 100, 25, 25]
    bad_coins7 = [150, 250, 25, 25]
    bad_coins8 = [300, 300, 25, 25]
    bad_coins9 = [700, 500, 25, 25]
    bad_coins10 = [500, 480, 25, 25]

    bad_coins = [bad_coin1, bad_coin2, bad_coin3, bad_coin4, bad_coin5,\
                 bad_coins6, bad_coins7, bad_coins8, bad_coins9, bad_coins10,\
                 ]

    stage = START

# Game loop
setup()
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        elif event.type == pygame.KEYDOWN:

            if stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
                    
            elif stage == PLAYING:
                pass
                    
            elif stage == END:
                if event.key == pygame.K_SPACE:
                    setup()

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        player1_up = pressed[pygame.K_UP]
        player1_down = pressed[pygame.K_DOWN]
        player1_left = pressed[pygame.K_LEFT]
        player1_right = pressed[pygame.K_RIGHT]

        player2_up = pressed[pygame.K_w]
        player2_down = pressed[pygame.K_s]
        player2_left = pressed[pygame.K_a]
        player2_right = pressed[pygame.K_d]
        
        if player1_left:
            vel1[0] = -player1_speed
        elif player1_right:
            vel1[0] = player1_speed
        else:
            vel1[0] = 0

        if player1_up:
            vel1[1] = -player1_speed
        elif player1_down:
            vel1[1] = player1_speed
        else:
            vel1[1] = 0

        if player2_left:
            vel2[0] = -player2_speed
        elif player2_right:
            vel2[0] = player2_speed
        else:
            vel2[0] = 0

        if player2_up:
            vel2[1] = -player2_speed
        elif player2_down:
            vel2[1] = player2_speed
        else:
            vel2[1] = 0    
        
    # Game logic (Check for collisions, update points, etc.)
    if stage == PLAYING:
        ''' move the player in horizontal direction '''
        player1[0] += vel1[0]
        player2[0] += vel2[0]

        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player1, w):        
                if vel1[0] > 0:
                    player1[0] = w[0] - player1[2]
                elif vel1[0] < 0:
                    player1[0] = w[0] + w[2]
            elif intersects.rect_rect(player2, w):        
                if vel2[0] > 0:
                    player2[0] = w[0] - player2[2]
                elif vel2[0] < 0:
                    player2[0] = w[0] + w[2]

        ''' move the player in vertical direction '''
        player1[1] += vel1[1]
        player2[1] += vel2[1]

        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player1, w):                    
                if vel1[1] > 0:
                    player1[1] = w[1] - player1[3]
                if vel1[1]< 0:
                    player1[1] = w[1] + w[3]
            elif intersects.rect_rect(player2, w):                    
                if vel2[1] > 0:
                    player2[1] = w[1] - player2[3]
                if vel2[1]< 0:
                    player2[1] = w[1] + w[3]


        ''' here is where you should resolve player collisions with screen edges '''
        if player1[1] < -(player1[3]):
            player1[1] = HEIGHT + 1
        if player1[1] > HEIGHT + 1:
            player1[1] = -(player1[3])

        if player1[0] < -(player1[2]):
            player1[0] = WIDTH + 1
        if player1[0] > WIDTH + 1:
            player1[0] = -(player1[2])
            
        if player2[1] < -(player2[3]):
            player2[1] = HEIGHT + 1
        if player2[1] > HEIGHT + 1:
            player2[1] = -(player2[3])

        if player2[0] < -(player2[2]):
            player2[0] = WIDTH + 1
        if player2[0] > WIDTH + 1:
            player2[0] = -(player2[2])


        ''' get the coins '''
        hit_list = []
        hit_list2 = []
        hit_list3 = []
        hit_list4 = []

        for c in coins:
            if intersects.rect_rect(player1, c):
                hit_list.append(c)
            elif intersects.rect_rect(player2, c):
                hit_list2.append(c)

        for b in bad_coins:
            if intersects.rect_rect(player1, b):
                hit_list3.append(b)
            elif intersects.rect_rect(player2, b):
                hit_list4.append(b)
                
        hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
        hit_list2 = [c for c in coins if intersects.rect_rect(player2, c)]
        hit_list3 = [b for b in bad_coins if intersects.rect_rect(player1, b)]
        hit_list4 = [b for b in bad_coins if intersects.rect_rect(player2, b)]

        for hit in hit_list:
            coins.remove(hit)
            score1 += 1
            coin.play()

        for hit in hit_list2:
            coins.remove(hit)
            score2 += 1
            coin.play()
            
        for hit in hit_list3:
            bad_coins.remove(hit)
            score1 -= 1
            bad_coin.play()
            
        for hit in hit_list4:
            bad_coins.remove(hit)
            score2 -= 1
            bad_coin.play()
            
        if len(coins) == 0:
            win = True
            stage = END
        
        
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(FRONT_BLUE)

    pygame.draw.rect(screen, PINK, player1)
    pygame.draw.rect(screen, PURPLE, player2)

    if stage == PLAYING:
        for w in walls:
            pygame.draw.rect(screen, FRONT_BLUE, w)

        for c in coins:
            pygame.draw.rect(screen, BRIGHT_GREEN, c)
            
        for b in bad_coins:
            pygame.draw.rect(screen, YELLOW, b)
                
    ''' begin/end game text '''
    if stage == START:
        screen.blit(leopard, (0, 0))
        text1 = MY_FONT.render("Welcome to the Beautiful Maze Game", True, GREY_BLUE)
        text2 = MY_FONT.render("(Press SPACE to play)", True, GREY_BLUE)
        screen.blit(text1, [100, 100])
        screen.blit(text2, [225, 200])
        
        
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [310, 150])
        screen.blit(text2, [210, 200])
        
           
    font = pygame.font.Font(None, 30)
    score_text = font.render("Player 1 Score: " + str(score1), 1, PINK)
    screen.blit(score_text, [50, 50])

    font = pygame.font.Font(None, 30)
    score_text = font.render("Player 2 Score: " + str(score2), 1, PURPLE)
    screen.blit(score_text, [600, 50])

    if win:
        if score1 > score2:
            font = pygame.font.Font(None, 50)
            score_text = font.render("Player 1 Wins!!!", 1, BRIGHT_BLUE)
            screen.blit(score_text, [275, 50])
        elif score1 < score2:
            font = pygame.font.Font(None, 50)
            score_text = font.render("Player 2 Wins!!!", 1, BRIGHT_BLUE)
            screen.blit(score_text, [275, 50])
        elif score1 == score2:
            font = pygame.font.Font(None, 50)
            score_text = font.render("Draw", 1, BRIGHT_BLUE)
            screen.blit(score_text, [350, 50])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

