# 拼图开始提示界面
import pygame
from pygame.locals import *
import sys
import math
import time
import datetime
import os,random
import easygui

pygame.init()
canvas = pygame.display.set_mode((685,449))
pygame.display.set_caption("开始!")
canvas.fill((255,255,255))
flag = pygame.image.load('flag/国旗拼图完整.jpg')

def handleEvent():
    global state
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pygame.quit()
            os.system('python photo.py')
            sys.exit()
            
canvas.blit(flag,(0,0)) 
pygame.display.update()
easygui.msgbox('一个小朋友好不容易画好的国旗绘画\n被人破坏啦!')
easygui.msgbox('呜呜呜┭┮﹏┭┮,好伤心!')
easygui.msgbox('可不可以帮帮她把图片拼起来?')
easygui.msgbox('点击画面进入拼图!')
while True:
    handleEvent()
    pygame.display.update()
    pygame.time.delay(120)