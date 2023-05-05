# 英雄贴标签

import pygame
from pygame.locals import *

pygame.init()

# 创建pygame窗口 窗口全屏，按ESC键退出
canvas = pygame.display.set_mode((640, 410))
pygame.display.set_caption('王者农药')
# 事件处理，关闭程序
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
# 展示文字
def showText(text, position):
    TextFont = pygame.font.Font('./fonts/kaiti.TTF', 36)
    TextFont.set_bold(True)
    text2 = TextFont.render(text, True, (155, 255, 125))
    canvas.blit(text2, position)

# 我是分割线-------------------------------------------------------------------------------------------------------------
# 以上是预留代码，请在下面书写代码
# 加载自己喜欢阵容
# 示例：bg = pygame.image.load('./images/王者荣耀阵容1.jpg')


# 绘制自己选择的阵容:canvas.blit(图片变量,(x坐标,y坐标))


# 使用showText('文字',(x坐标,y坐标))对每个英雄进行介绍
# 示例：showText('蔡文姬',(10,290))


# ----------------------------------------------------------------------------------------------------------------------


# 主循环
while True:
    pygame.display.update()
    handleEvent()






