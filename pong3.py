"""
Abid Bakhtiyar
890459241
CPSC 386-02
"""

# imports for pygames
import pygame
import sys
import random
from pygame.locals import *

# size of the screen
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600

# surface variable
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
fps = 60
MOVESPEED = 6


# class for all the paddles and the net
class paddles:
    paddle = pygame.Rect(WINDOWWIDTH - 40, 0, 100, 10)  # top right
    paddle2 = pygame.Rect(WINDOWWIDTH - 40, WINDOWHEIGHT - 40, 100, 10)  # bot right
    paddle3 = pygame.Rect(WINDOWWIDTH - 40, WINDOWHEIGHT / 2, 10, 100)  # middle
    paddle4 = pygame.Rect(0, 0, 100, 10)  # top left
    paddle5 = pygame.Rect(0, WINDOWHEIGHT / 2, 10, 100)  # middle
    paddle6 = pygame.Rect(0, WINDOWHEIGHT - 40, 100, 10)  # bot left
    net = pygame.Rect(WINDOWWIDTH / 2, 0, 5, WINDOWHEIGHT)
    netImage = pygame.image.load('net.gif')
    paddleImage = pygame.image.load('green.gif')
    fixedNet = pygame.transform.scale(netImage, (5, WINDOWHEIGHT))
    fixedImg = pygame.transform.scale(paddleImage, (100, 10))
    fixedImg2 = pygame.transform.scale(paddleImage, (10, 100))


# class for the ball
class ball:
    bll = pygame.Rect(WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 40, 40)
    velocity = 0
    angle = 0
    bllimage = pygame.image.load('ball.gif')
    fixedball = pygame.transform.scale(bllimage, (40, 40))


# class for the score
class score:
    playerScore = 0
    compScore = 0


# resets the ball after it goes out of bounds
def reset_ball():
    ball.bll.x = WINDOWWIDTH / 2
    ball.bll.y = WINDOWHEIGHT / 2
    ball.velocity = random.randint(-10, 10)
    ball.angle = random.randint(-10, 10)


# draws the score on the game board
def draw_score(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = x, y
    surface.blit(textobj, textrect)


# terminates the game if the user selects it
def terminate():
    pygame.quit()
    sys.exit()


# lets the user decide if they want to play or quit
def choice():
    pressed = False
    while not pressed:
        for e in pygame.event.get():
            if e.type == QUIT:
                terminate()
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    terminate()
                if e.key == K_y:  # user must hit y to restart the game
                    play()
                return  # will return is anything is hit


# main function that runs the game
def play():
    pygame.init()  # initialize the game
    mainClock = pygame.time.Clock()
    pygame.display.set_caption("Pong w/o walls!")

    # all the sound files
    paddleSound = pygame.mixer.Sound('laser1.wav')
    gamelose = pygame.mixer.Sound('gameover.wav')
    matchwin = pygame.mixer.Sound('levelup.wav')
    pygame.mixer.music.load('peachcastle.wav')

    font = pygame.font.Font(None, 48)

    # directions for the user
    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    # creates a title screen for the user
    windowSurface.fill(WHITE)
    draw_score('   Welcome to Pong!   ', font, windowSurface, WINDOWWIDTH / 3, WINDOWHEIGHT / 3)
    draw_score('Press a key to start.', font, windowSurface, WINDOWWIDTH / 3 - 30, WINDOWHEIGHT / 3 + 50)
    pygame.display.update()
    choice()

    # starts nested loops that will both reset the game when the user wants to and will loop the animations and controls
    playAgain = True
    # resets
    while playAgain:
        score.compScore = 0
        score.playerScore = 0
        # sets the velocity and angle of the ball to be random when it starts
        ball.velocity = random.randint(-10, 10)
        ball.angle = random.randint(-10, 10)
        pygame.mixer.music.play(-1, 0.0)

        playGame = True
        # actual game animations
        while playGame:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                # controls
                if event.type == KEYDOWN:
                    if event.key == K_LEFT or event.key == K_a:
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT or event.key == K_d:
                        moveLeft = False
                        moveRight = True
                    if event.key == K_UP or event.key == K_w:
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == K_s:
                        moveUp = False
                        moveDown = True

                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_LEFT or event.key == K_a:
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == K_d:
                        moveRight = False
                    if event.key == K_UP or event.key == K_w:
                        moveUp = False
                    if event.key == K_DOWN or event.key == K_s:
                        moveDown = False

            windowSurface.fill(WHITE)
            # sets the random velocities to the ball
            ball.bll.x += ball.velocity
            ball.bll.y += ball.angle

            # controls for the user paddles
            if moveDown and paddles.paddle3.bottom < WINDOWHEIGHT:
                paddles.paddle3.top += MOVESPEED
            if moveUp and paddles.paddle3.top > 0:
                paddles.paddle3.top -= MOVESPEED
            if moveLeft and paddles.paddle.left > WINDOWWIDTH / 2:
                paddles.paddle.left -= MOVESPEED
                paddles.paddle2.left -= MOVESPEED
            if moveRight and paddles.paddle.right < WINDOWWIDTH:
                paddles.paddle.right += MOVESPEED
                paddles.paddle2.right += MOVESPEED

            # movement for the computer paddles
            paddles.paddle4.right += MOVESPEED
            if paddles.paddle4.x >= (WINDOWWIDTH / 2) - 100:
                paddles.paddle4.x = 0
            paddles.paddle5.top += MOVESPEED
            if paddles.paddle5.y >= WINDOWHEIGHT - 100:
                paddles.paddle5.y = 0
            paddles.paddle6.right += MOVESPEED
            if paddles.paddle6.x >= (WINDOWWIDTH / 2) - 100:
                paddles.paddle6.x = 0

            # Draws all the images on the surface
            windowSurface.blit(paddles.fixedImg, paddles.paddle)
            windowSurface.blit(paddles.fixedImg, paddles.paddle2)
            windowSurface.blit(paddles.fixedImg2, paddles.paddle3)
            windowSurface.blit(paddles.fixedImg, paddles.paddle4)
            windowSurface.blit(paddles.fixedImg2, paddles.paddle5)
            windowSurface.blit(paddles.fixedImg, paddles.paddle6)
            windowSurface.blit(paddles.fixedNet, paddles.net)
            windowSurface.blit(ball.fixedball, ball.bll)

            # draws all the scores
            draw_score(str(score.compScore), font, windowSurface, 100, WINDOWHEIGHT / 2)
            draw_score(str(score.playerScore), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)

            # list of paddles, easier to check for contact this way
            padds = [paddles.paddle, paddles.paddle2, paddles.paddle3, paddles.paddle4, paddles.paddle5,
                     paddles.paddle6]

            # for loop will iterate and see if any of the paddles as been hit
            for pad in padds:
                if ball.bll.colliderect(pad):
                    # reverses the ball in the opposite direction
                    ball.velocity = -ball.velocity
                    # creates a new random angle for the ball to travel
                    ball.angle = random.randint(-10, 10)

                    # plays the paddle sound effect
                    paddleSound.play()
                    break

            # checks if the ball is out of bounds
            if ball.bll.x > WINDOWWIDTH:
                score.compScore += 1
                draw_score(str(score.compScore), font, windowSurface, 100, WINDOWHEIGHT / 2)
                reset_ball()
            elif ball.bll.x < 0:
                score.playerScore += 1
                draw_score(str(score.playerScore), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)
                reset_ball()

            # need an and statement here because you need to check if the ball passed the top and if it's on computer
            # side or player side
            elif ball.bll.y > WINDOWHEIGHT and ball.bll.x > WINDOWWIDTH / 2:
                score.compScore += 1
                draw_score(str(score.compScore), font, windowSurface, 100, WINDOWHEIGHT / 2)
                reset_ball()
            elif ball.bll.y > WINDOWHEIGHT and ball.bll.x < WINDOWWIDTH / 2:
                score.playerScore += 1
                draw_score(str(score.playerScore), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)
                reset_ball()
            elif ball.bll.y < 0 and ball.bll.x > WINDOWWIDTH / 2:
                score.compScore += 1
                draw_score(str(score.compScore), font, windowSurface, 100, WINDOWHEIGHT / 2)
                reset_ball()
            elif ball.bll.y < 0 and ball.bll.x < WINDOWWIDTH / 2:
                score.playerScore += 1
                draw_score(str(score.playerScore), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)
                reset_ball()

            # if the ball passes through the exact middle, the ball will just reset
            elif ball.bll.y < 0 and ball.bll.x == WINDOWWIDTH / 2:
                reset_ball()
            elif ball.bll.y > WINDOWHEIGHT and ball.bll.x == WINDOWWIDTH / 2:
                reset_ball()
            # checks the score, to see if anyone scored about 11
            if score.compScore > 11 or score.playerScore > 11:
                # makes sure they won by at least 2
                if score.compScore - score.playerScore >= 2:
                    pygame.mixer.music.stop()  # stops background music
                    # resets the scores to be blank
                    score.playerScore = " "
                    score.compScore = " "
                    draw_score(str(score.compScore), font, windowSurface, 100, WINDOWHEIGHT / 2)
                    draw_score(str(score.playerScore), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)
                    # displays the player lose screen
                    draw_score("Computer WINS", font, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
                    gamelose.play()  # plays lose sound effect
                else:
                    pygame.mixer.music.stop()
                    score.playerScore = " "
                    score.compScore = " "
                    draw_score(str(score.compScore), font, windowSurface, 100, WINDOWHEIGHT / 2)
                    draw_score(str(score.playerScore), font, windowSurface, WINDOWWIDTH - 100, WINDOWHEIGHT / 2)
                    # displays the player win screen
                    draw_score("Player WINS", font, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
                    matchwin.play()  # plays the win sound effect
                # asks if the user wants to play again
                draw_score("Press Y to play again?", font, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 200)
                draw_score("Press Escape to escape", font, windowSurface, WINDOWWIDTH / 2, WINDOWHEIGHT / 2 - 300)
                pygame.display.update()
                choice()

            pygame.display.update()
            mainClock.tick(fps)


play()
