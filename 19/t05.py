# 缺一不可
# 导入模块
import pygame
from pygame.locals import *
pygame.init()

canvas = pygame.display.set_mode((1024,1000))
pygame.display.set_caption('王者荣耀')
# 加载背景图片
bg = pygame.image.load('images/bg3.jpg')
# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
# 创建列表存储英雄角色
heroes = ['梦奇']

# 请在下方补充代码------------------------------------------------------------------------------------------------------
# 使用append()进行英雄补位，完善阵容





# 继续添加对方阵容






# -----------------------------------------------------------------------------------------------------------------------
# 绘制背景
canvas.blit(bg,(0,0))
# 绘制列表中的所有角色图片
y = 0
x = 0
for hero in heroes:
    # 加载对应图片
    h = pygame.image.load('images/'+hero+'.jpg')
    # 绘制
    canvas.blit(h,(x,y))
    # 向下排列
    y += 200
    # 五个换列
    if y >= 1000:
        y = 0
        x += 435+154

# 主循环
while True:
    handleEvent()
    pygame.display.update()


