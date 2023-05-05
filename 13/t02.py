# 植物大战僵尸
import time

import pygame
from pygame.locals import *

pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((2048, 885))
pygame.display.set_caption('植物大战僵尸')

# 加载图片
bg = pygame.image.load('./images/植物大战僵尸bg.jpg')
# 植物
plant = pygame.image.load('./images/plant.png')
# 豌豆
dou = pygame.image.load('./images/豆子.png')
# 僵尸
zombie = pygame.image.load('./images/僵尸1.png')
# 胜利
win = pygame.image.load('./images/植物大战僵尸胜利.png')

# 展示文字
def showText(text, position):
    TextFont = pygame.font.Font('./fonts/锐字温帅小可爱.TTF', 50)
    TextFont.set_bold(False)
    text2 = TextFont.render(text, True, (155, 255, 125))
    canvas.blit(text2, position)


# 事件处理，关闭程序
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            print(event.pos[0], event.pos[1])


# ----------------------------------------------------------------------------------------------------------------------
# 请在下方书写代码
# 声明变量表示豌豆的初始x坐标




# 主循环
while True:
    # 绘制背景图片


    # 绘制射手(650, 330)


    # 绘制豌豆(753,378)



    # 延迟


    pygame.display.update()
    handleEvent()











