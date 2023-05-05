# 我的星座
# 导入模块
import pygame
from pygame.locals import *
pygame.init()
# 创建窗口
canvas = pygame.display.set_mode((1024,1024))
pygame.display.set_caption('我的星座')
# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

# 创建函数，准备形参：星座名，实现绘制指定星座动漫------------------------------------------------------------------------




# 调用函数，传入星座名





while True:
    pygame.display.update()
    handleEvent()