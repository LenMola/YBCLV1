# 我的农场

import pygame
from pygame.locals import *
pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((1334,750))
pygame.display.set_caption('我的农场')

# 加载图片
bg0 = pygame.image.load('./images/农场0.jpg')
bg1 = pygame.image.load('./images/路标_副本.png')
bg  = pygame.image.load('./images/农场.jpg')
plant01 = pygame.image.load('images/plant01.png')
plant02 = pygame.image.load('images/plant02.png')
plant03 = pygame.image.load('images/plant03.png')
plant04 = pygame.image.load('images/plant04.png')
# 展示文字
def showText(text, position):
    TextFont = pygame.font.Font('./fonts/上首萌虎体.ttf', 30)
    TextFont.set_bold(False)
    text2 = TextFont.render(text, True, (100, 50, 50))
    canvas.blit(text2, position)
# 事件处理，关闭程序
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN :
            print(event.pos[0],event.pos[1])
            # 点击按钮
            if 760 <= event.pos[0] <= 950 and 540 <= event.pos[1] <= 650:
                # 点击按钮后调用函数------------------------------------------------------------------------------------
                pass


canvas.blit(bg0,(0,0))
canvas.blit(bg1,(720,518))
# 我是分割线-------------------------------------------------------------------------------------------------------------
# 以上是预留代码，请在下面书写代码
# 创建函数绘制界面







# 创建函数绘制文字







# ----------------------------------------------------------------------------------------------------------------------
# 主循环
while True:
    pygame.display.update()
    handleEvent()



