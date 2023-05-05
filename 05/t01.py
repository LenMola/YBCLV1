# 王者农药

import pygame
from pygame.locals import *

pygame.init()

# 创建pygame窗口 窗口全屏，按ESC键退出
canvas = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('王者农药')


# 我是分割线-------------------------------------------------------------------------------------------------------------
# 以上是预留代码，请在下面书写代码
# 加载自己喜欢图片
# 示例：bg = pygame.image.load('./images/王者荣耀.png')



# 绘制自己喜欢的图片：




# ----------------------------------------------------------------------------------------------------------------------
# 事件处理，关闭程序
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()



# 主循环
while True:
    pygame.display.update()
    handleEvent()



