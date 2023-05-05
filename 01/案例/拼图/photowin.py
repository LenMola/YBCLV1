# 国旗拼图成功
import pygame
from pygame.locals import *
import sys
import math
import time
import datetime
import os,random

pygame.init()
canvas = pygame.display.set_mode((685,449))
pygame.display.set_caption("成功!")
canvas.fill((255,255,255))
flag = pygame.image.load('flag/国旗拼图完整.jpg')
# 胜利音效
pygame.mixer.music.load('music/胜利.mp3')
pygame.mixer.music.play(1)
def handleEvent():
    global state
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            os.system('python index02.py')
            sys.exit()
while True:
    canvas.blit(flag,(0,0))
    handleEvent()
    pygame.display.update()
    pygame.time.delay(120)