import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()



WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Pong w/o walls!")


BLACK = (0,0,0)
WHITE = (255, 255, 255)
fps = 60
'''
LEFT_KEYS = [K_LEFT, K_a]
RIGHT_KEYS = [K_RIGHT, K_d]
UP_KEYS = [K_UP, K_w]
DOWN_KEYS = [K_DOWN, K_s]
'''

moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 6
class paddles():
    paddle = pygame.Rect(WINDOWWIDTH - 40, 0, 100,10) # top right
    paddle2 = pygame.Rect(WINDOWWIDTH - 40, WINDOWHEIGHT - 40, 100, 10) # bot right
    paddle3 = pygame.Rect(WINDOWWIDTH - 40, WINDOWHEIGHT/2, 10, 100) # middle
    paddle4 = pygame.Rect(0, 0, 100, 10) # top left
    paddle5 = pygame.Rect(0, WINDOWHEIGHT / 2, 10, 100) # middle
    paddle6 = pygame.Rect(0, WINDOWHEIGHT - 40, 100, 10) # bot left
    net = pygame.Rect(WINDOWWIDTH / 2, 0, 5, WINDOWHEIGHT)
    netImage = pygame.image.load('net.gif')
    paddleImage = pygame.image.load('green.gif')
    fixedNet = pygame.transform.scale(netImage, (5, WINDOWHEIGHT))
    fixedImg = pygame.transform.scale(paddleImage, (100,10))
    fixedImg2 = pygame.transform.scale(paddleImage, (10, 100))

class ball():
    bll = pygame.Rect(WINDOWWIDTH / 2, WINDOWHEIGHT / 2, 40, 40)
    velocity = 0
    angle = 0
    bllimage = pygame.image.load('ball.gif')
    fixedball = pygame.transform.scale(bllimage, (40,40))


class score():
    playerScore = 0
    compScore = 0
ball.velocity = random.randint(-10, 10)
ball.angle = random.randint(-10, 10)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
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
    ball.bll.x += ball.velocity
    ball.bll.y += ball.angle

    if moveDown and paddles.paddle3.bottom < WINDOWHEIGHT:
        paddles.paddle3.top += MOVESPEED
    if moveUp and paddles.paddle3.top > 0:
        paddles.paddle3.top -= MOVESPEED
    if moveLeft and paddles.paddle.left > WINDOWWIDTH / 2:
        paddles.paddle.left -= MOVESPEED
        paddles.paddle2.left -=MOVESPEED
    if moveRight and paddles.paddle.right < WINDOWWIDTH:
        paddles.paddle.right += MOVESPEED
        paddles.paddle2.right += MOVESPEED

    # Draw the block onto the surface.
    windowSurface.blit(paddles.fixedImg, paddles.paddle)
    windowSurface.blit(paddles.fixedImg, paddles.paddle2)
    windowSurface.blit(paddles.fixedImg2, paddles.paddle3)
    windowSurface.blit(paddles.fixedImg, paddles.paddle4)
    windowSurface.blit(paddles.fixedImg2, paddles.paddle5)
    windowSurface.blit(paddles.fixedImg, paddles.paddle6)
    windowSurface.blit(paddles.fixedNet, paddles.net)
    windowSurface.blit(ball.fixedball, ball.bll)

    pygame.display.update()
    mainClock.tick(40)





