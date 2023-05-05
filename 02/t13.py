# 我的程序我做主
import pygame
from pygame.locals import *

pygame.init()

# 创建pygame窗口
canvas = pygame.display.set_mode((1024, 521))

# 我是分割线-------------------------------------------------------------------------------------------------------------
# 以上是预留代码，请在下面书写代码
pygame.display.set_caption('请输入标题')


# 加载自己喜欢图片
# 示例：bg = pygame.image.load('./images/王者荣耀.png')



# 给变量bg重新赋值试试呢？



# ----------------------------------------------------------------------------------------------------------------------


# 事件处理，关闭程序
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()


# 绘制背景图片
canvas.blit(bg, (0, 0))

# 主循环
while True:
    pygame.display.update()
    handleEvent()
