# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
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
BRIGHT_GREEN = (29, 140, 12)
ORANGE = (255, 125 , 0)

# Make a player
player1 =  [200, 150, 25, 25]
vel1 = [0, 0]
player1_speed = 5
score1 = 0

player2 = [250, 150, 25, 25]
vel2 = [0, 0]
player2_speed = 5
score2 = 0

# make walls
wall1 = [300, 275, 200, 25]
wall2 = [400, 450, 200, 25]
wall3 = [100, 100, 25, 200]
wall4 = [0, 0, 400, 25]
wall5 = [450, 0, 400, 25]
wall6 = [

walls = [wall1, wall2, wall3, wall4, wall5]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]
coin4 = [500, 100, 25, 25]

coins = [coin1, coin2, coin3, coin4]

# Sound Effects

coin = pygame.mixer.Sound("sounds/coin.ogg")

# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

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

    for c in coins:
        if intersects.rect_rect(player1, c):
            hit_list.append(c)
        elif intersects.rect_rect(player2, c):
            hit_list2.append(c)
            
    hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
    hit_list2 = [c for c in coins if intersects.rect_rect(player2, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score1 += 1
        coin.play()

    for hit in hit_list2:
        coins.remove(hit)
        score2 += 1
        coin.play()
        
    if len(coins) == 0:
        win = True
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, PINK, player1)
    pygame.draw.rect(screen, PURPLE, player2)
    
    for w in walls:
        pygame.draw.rect(screen, ORANGE, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        if score1 > score2:
            font = pygame.font.Font(None, 50)
            score_text = font.render("P1 Wins!!!", 1, BRIGHT_BLUE)
            screen.blit(score_text, [350, 50])
        elif score1 < score2:
            font = pygame.font.Font(None, 50)
            score_text = font.render("P2 Wins!!!", 1, BRIGHT_BLUE)
            screen.blit(score_text, [350, 50])
        elif score1 == score2:
            font = pygame.font.Font(None, 50)
            score_text = font.render("Draw", 1, BRIGHT_BLUE)
            screen.blit(score_text, [350, 50])

       
    font = pygame.font.Font(None, 30)
    score_text = font.render("P1 Score: " + str(score1), 1, PINK)
    screen.blit(score_text, [100, 50])

    font = pygame.font.Font(None, 30)
    score_text = font.render("P2 Score: " + str(score2), 1, PURPLE)
    screen.blit(score_text, [600, 50])
    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
