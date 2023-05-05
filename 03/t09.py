# 要多少有多少！

import pygame
from pygame.locals import *
pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((1068,668))
pygame.display.set_caption('奥比银行')
# 展示文字
def showText(text, position):
    TextFont = pygame.font.Font('./fonts/kaiti.TTF', 25)
    TextFont.set_bold(True)
    text2 = TextFont.render(text, True, (0, 0, 0))
    canvas.blit(text2, position)
# 事件处理，关闭程序
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
# 加载图片
bg = pygame.image.load('images/奥比银行.PNG')
canvas.blit(bg,(0,0))
# ----------------------------------------------------------------------------------------------------------------------
# 使用input()输入昵称信息并赋值给变量name

# 使用input()输入金币信息并赋值给变量gold


# 展示昵称与金币——注意变量名哦
showText(name,(500,150))
showText(gold,(500,200))




# 主循环
while True:
    pygame.display.update()
    handleEvent()



