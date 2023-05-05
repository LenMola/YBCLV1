# 萌版星座
# 导入模块
import pygame
from pygame.locals import *
pygame.init()

canvas = pygame.display.set_mode((1200,900))
pygame.display.set_caption('十二星座')
# 加载背景图片
bg = pygame.image.load('images/星空.jpg')
# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

# 请在下方补充代码------------------------------------------------------------------------------------------------------





















# 主循环
while True:
    handleEvent()
    pygame.display.update()


