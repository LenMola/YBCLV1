# 给点阳光就温暖


import pygame
from pygame.locals import *
pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((641,499))
pygame.display.set_caption('植物大战僵尸')

# 加载图片
bg = pygame.image.load('images/阳光.jpg')

# 展示文字
def showText(text, position):
    TextFont = pygame.font.Font('./fonts/kaiti.TTF', 12)
    TextFont.set_bold(True)
    text2 = TextFont.render(text, True, (0, 0, 0))
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
# 你想要多少阳光呀？（不要开挂！！）
# 使用input()输入阳光数量并给变量sunshine赋值


# 补充代码，展示sunshine



# ----------------------------------------------------------------------------------------------------------------------
# 主循环
while True:
    pygame.display.update()
    handleEvent()







