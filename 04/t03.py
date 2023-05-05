# show标题

import pygame
from pygame.locals import *
pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((1024,660))
pygame.display.set_caption('植物大战僵尸')

# 加载图片
bg = pygame.image.load('./images/植物大战僵尸bg2.jpg')

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
# 绘制背景图片
canvas.blit(bg,(0,0))
# 我是分割线-------------------------------------------------------------------------------------------------------------
# 以上是预留代码，请在下面书写代码
# 使用showText()给我们的游戏设置标题吧！(400,600)









# ----------------------------------------------------------------------------------------------------------------------
# 主循环
while True:
    pygame.display.update()
    handleEvent()



