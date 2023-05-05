# 猫咖
# 导入模块
import pygame
from pygame.locals import *
pygame.init()

canvas = pygame.display.set_mode((1180,790))
pygame.display.set_caption('猫咖')
# 加载背景图片
bg = pygame.image.load('images/草地.jpg')
# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
# 请在下方补充代码--------------------------------------------------------------------------------------------------------
# 创建列表存储猫咪/狗狗品种




# 使用pop()方法移出狗子品种




# 使用clear()清空列表




# -----------------------------------------------------------------------------------------------------------------------
# 绘制背景
canvas.blit(bg,(0,0))
# 绘制列表中的所有角色图片
y = 0
x = 0
for cat in cats:
    # 加载图片
    c = pygame.image.load('images/'+cat+'.jpg')
    # 绘制
    canvas.blit(c,(x,y))
    # 向右排列
    x += 280+20
    # 四个换行
    if x >= 1084:
        x = 0
        y += 250+20

# 主循环
while True:
    handleEvent()
    pygame.display.update()


