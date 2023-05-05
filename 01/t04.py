# 无限的金币
import pygame
from pygame.locals import *
pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((1024,517))
pygame.display.set_caption('王者荣耀')

# 加载图片
bg = pygame.image.load('./images/王者荣耀1.png')

# 展示文字
def showText(text, position):
    TextFont = pygame.font.Font('./fonts/kaiti.TTF', 15)
    text2 = TextFont.render(text, True, (255, 255, 125))
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
# 删除下面代码前的#，解除注释，将字符串金币补充完
# showText(请输入内容,(633,13))
# showText(请输入内容,(747,13))
# showText(请输入内容,(853,13))







# ----------------------------------------------------------------------------------------------------------------------
# 主循环
while True:
    pygame.display.update()
    handleEvent()