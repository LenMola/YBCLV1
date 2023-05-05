# 植物大战僵尸

import pygame
from pygame.locals import *
pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((1500,675))
pygame.display.set_caption('植物大战僵尸')

# 加载图片
bg = pygame.image.load('./images/植物大战僵尸bg5.jpg')
# 植物
plant01 = pygame.image.load('./images/plants/plant01.png')
plant02 = pygame.image.load('./images/plants/plant02.png')
plant03 = pygame.image.load('./images/plants/plant03.png')
plant04 = pygame.image.load('./images/plants/plant04.png')
plant05 = pygame.image.load('./images/plants/plant05.png')
plant06 = pygame.image.load('./images/plants/plant06.png')
plant07 = pygame.image.load('./images/plants/plant07.png')
plant08 = pygame.image.load('./images/plants/plant08.png')
plant09 = pygame.image.load('./images/plants/plant09.png')
plant10 = pygame.image.load('./images/plants/plant10.png')
plant11 = pygame.image.load('./images/plants/plant11.png')
plant12 = pygame.image.load('./images/plants/plant12.png')
plant13 = pygame.image.load('./images/plants/plant13.png')
# 僵尸
zombie01 = pygame.image.load('./images/zombies/zombie01.png')
zombie02 = pygame.image.load('./images/zombies/zombie02.png')
zombie03 = pygame.image.load('./images/zombies/zombie03.png')
zombie04 = pygame.image.load('./images/zombies/zombie04.png')

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
        # if event.type ==MOUSEBUTTONDOWN:
        #     print(event.pos[0],event.pos[1])
# 绘制背景图片

# 放一只小僵尸玩玩~


# ----------------------------------------------------------------------------------------------------------------------
# 主循环
while True:
    pygame.display.update()
    handleEvent()



