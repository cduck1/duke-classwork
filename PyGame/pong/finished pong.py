import pygame 
# -- Global Constants 
# -- Colours 
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
BLUE = (50, 50, 255) 
YELLOW = (255, 255, 0) 
# -- Initialise PyGame 
pygame.init() 
# -- Blank Screen 
size = (640, 480) 
screen = pygame.display.set_mode(size) 
# -- Title of new window/screen 
pygame.display.set_caption("Pong") 
# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 
# -- Game Loop 
def gameloop():
    # -- Exit game flag set to false 
    done = False 
    # -- Variables 
    # ---- top_left_screen = (0, 0) 
    # ---- top_right_screen = (640, 0) 
    # ---- bottom_left_screen = (0, 480) 
    # ---- bottom_right_screen = (640, 480)
    ai_padd_width = 15
    ai_padd_length = 60
    ai_x_padd = 625
    ai_y_padd = 200
    padd_width = 15 
    padd_length = 60 
    x_padd = 0 
    y_padd = 20 
    x_val = 150 
    y_val = 200 
    ball_width = 20 
    x_offset = -1
    y_offset = 1
    lives = 3
    ai_lives = 3
    score = 0
    
    while not done:
        # -- User input and controls 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y_padd = y_padd - 5
            if keys[pygame.K_DOWN]:
                y_padd = y_padd + 5
            
        # -- Game logic goes after this comment
        # -- The paddle can't go off the top or bottom
        if y_padd <= 0:
            y_padd = 0
            
        if y_padd >= 420:
            y_padd = 420

        # -- Getting the score to increase by 1 when the ball goes off the left edge
        if x_val <= 0:
            lives = lives - 1
            x_val = 150
            y_val = 200
            
        # -- getting the right edge reset the ball and -1 from ai_lives
        if x_val >= 640:
            ai_lives = ai_lives - 1
            x_val = 150
            y_val = 200
            
        # -- getting the top edge to bounce
        if y_val <= 0:
            y_val = 0
            y_offset = -y_offset
            
        # -- getting the bottom edge to bounce
        if y_val >= 460:
            y_val =  460
            y_offset = -y_offset
               
        # -- Check the criteria for hitting the paddle and getting the ball speed to increase with a score variable
        if x_val < 15 and y_val > y_padd and y_val < y_padd + 60:
            x_offset = x_offset * -1
            x_offset += 1
            y_offset += 1
            
        x_val = x_val + x_offset 
        y_val = y_val + y_offset

        # -- getting the ball to bounce off the ai_paddle
        if x_val > 605 and y_val > ai_y_padd and y_val < ai_y_padd + 60:
            x_offset = x_offset * -1
        
        # -- getting the ai to track the ball
        ai_y_padd = y_val - 30
            
        # -- Screen background is BLACK 
        screen.fill(BLACK)
        
        # -- Draw here
        pygame.draw.rect(screen, BLUE, (x_val, y_val, ball_width, ball_width)) 
        pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_width, padd_length))
        pygame.draw.rect(screen, YELLOW, (ai_x_padd, ai_y_padd, ai_padd_width, ai_padd_length))

        # -- display ai_lives
        font = pygame.font.Font(None, 30)
        text = font.render("Lives: " + str(ai_lives), 1, WHITE)
        screen.blit(text, (550, 10))
                            
        # -- display lives
        font = pygame.font.Font(None, 30)
        text = font.render("Lives: " + str(lives), 1, WHITE)
        screen.blit(text, (10, 10))
        
        # -- getting the game to end when lives = 0
        if lives == 0:
            done = True
            you_win()

        # -- getting the game to end when ai_lives = 0
        if ai_lives == 0:
            done = True
            ai_win()
    
        # -- flip display to reveal new position of objects 
        pygame.display.flip() 
    
        # - The clock ticks over 
        clock.tick(60)
        
# -- getting the game to end when lives = 0
def you_win():
    screen.fill(BLACK)
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render("YOU WIN!", 1, WHITE)
    screen.blit(text, (300, 10))
    pygame.display.flip()
    clock.tick(60)

# -- getting the game to end when lives = 0
def ai_win():
    screen.fill(BLACK)
    font = pygame.font.Font("freesansbold.ttf", 50)
    text = font.render("YOU LOSE!", 1, WHITE)
    screen.blit(text, (300, 10))
    pygame.display.flip()
    clock.tick(60)
        
gameloop()        
pygame.quit()

