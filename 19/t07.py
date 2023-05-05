# 我的动物世界
# 导入模块
import pygame
from pygame.locals import *
pygame.init()

canvas = pygame.display.set_mode((1080,600))
pygame.display.set_caption('我的世界')
# 加载背景图片
bg = pygame.image.load('images/bg1.png')
# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
# 创建列表存储动物角色
animals = ['驴','猪']
# 请在下方补充代码------------------------------------------------------------------------------------------------------

# 1.观察预留效果，将兔插入到驴和猪之前
animals.insert(1,'兔')
# 2.将鸡添加到最后
animals.append('鸡')
# 3.将哞菇插入到猪和鸡之间
animals.insert(3,'哞菇')



# -----------------------------------------------------------------------------------------------------------------------
# 绘制背景
canvas.blit(bg,(0,0))
# 绘制列表中的所有角色图片
y = 400
x = 0
for animal in animals:
    # 加载对应图片
    a = pygame.image.load('images/'+animal+'.png')
    # 绘制
    canvas.blit(a,(x,y))
    # 横向排列
    x += 200+20
    # 五个换列
    if x >= 1080:
        x = 0
        y += 220

# 主循环
while True:
    handleEvent()
    pygame.display.update()




