# 东风快递

import pygame,time
from pygame.locals import *

pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((1280, 700))
pygame.display.set_caption('东风快递')

# 加载背景
bg = pygame.image.load('./images/草地.jpg')
# 导弹车
car = pygame.image.load('./images/导弹车.png')
# 导弹
dan = pygame.image.load('./images/导弹.png')


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
# 绘制背景图片
canvas.blit(bg, (0, 0))
# 绘制导弹车
canvas.blit(car,(250,500))
# ----------------------------------------------------------------------------------------------------------------------
# 请在下方书写代码
# 声明变量表示导弹的初始坐标 x=325,y=388


# 主循环
while True:

    # 绘制导弹

    # 实现导弹右上方飞行（x增大y减小）

    pygame.display.update()
    handleEvent()














