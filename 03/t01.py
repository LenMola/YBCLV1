# 练习：界面内容我来补

import pygame
from pygame.locals import *
pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((392,696))
pygame.display.set_caption('雷电')

# 展示文字
def showText(text, position):
    TextFont = pygame.font.Font('./fonts/kaiti.TTF', 20)
    text2 = TextFont.render(text, True, (255, 255, 125))
    canvas.blit(text2, position)


# 下面开始写代码---------------------------------------------------------------------------------------------------------
# 1.加载背景图片
# 示例：bg = pygame.image.load('图片路径')
# 路径为images/雷电.jpg





# ------------------------------------------------------------------------------------------------------------------------
# 事件处理，关闭程序
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
# 绘制背景图片
canvas.blit(bg,(0,0))
# ----------------------------------------------------------------------------------------------------------------------
# 以上是预留代码，请在下面书写代码
# 2.绘制文字
# 声明变量表示分数

# 使用showText（）将分数绘制到窗口
showText(请补充,(10,10))

# 声明变量表示金币

# 使用showText（）将金币绘制到窗口
showText(请补充,(270,10))


# ----------------------------------------------------------------------------------------------------------------------
# 主循环
while True:
    pygame.display.update()
    handleEvent()


