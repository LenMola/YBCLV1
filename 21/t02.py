# 太阳系
# 导入模块
import pygame
from pygame.locals import *
pygame.init()

canvas = pygame.display.set_mode((1240,960))
pygame.display.set_caption('太阳系')
# 加载背景图片
bg = pygame.image.load('images/星空.png')
# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
# 创建列表存储星球
planets = ['太阳','水星','金星','地球','月球',
           '火星','木星','土星','天王星','海王星',
           '冥王星']
# 请在下方补充代码------------------------------------------------------------------------------------------------------



















# 主循环
while True:
    handleEvent()
    pygame.display.update()


