# 水果动物园
# 导入模块
import pygame
from pygame.locals import *
pygame.init()

canvas = pygame.display.set_mode((1600,900))
pygame.display.set_caption('水果动物园')
# 加载背景图片
bg = pygame.image.load('images/背景.jpg')
# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

# 请在下方补充代码------------------------------------------------------------------------------------------------------
# 创建列表存储水果图片名称
fruits = ['山竹鼠.jpg','桃子猴.jpg','梨猫.jpg',
          '榴莲猬.jpg','橙柴.jpg','火龙果.jpg',
          '牛芒.jpg','瓜个象.jpg','菠萝熊.jpg',]











# 主循环
while True:
    handleEvent()
    pygame.display.update()


