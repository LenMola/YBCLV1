# 光明与黑暗
# 导入模块
import pygame
from pygame.locals import *
pygame.init()

canvas = pygame.display.set_mode((1084,830))
pygame.display.set_caption('光明与黑暗')
# 加载背景图片
bg = pygame.image.load('images/宇宙.jpg')
# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()
# 请在下方补充代码------------------------------------------------------------------------------------------------------------------
atms = ['奈克瑟斯','盖亚','贝利亚','赛文',
       '赛罗','贝利亚','迪迦','贝利亚']
# 使用remove()方法移出反派角色贝利亚






# -----------------------------------------------------------------------------------------------------------------------
# 绘制背景
canvas.blit(bg,(0,0))
# 绘制列表中的所有角色图片
y = 0
x = 0
for atm in atms:
    # 加载奥特曼
    a = pygame.image.load('images/'+atm+'.jpg')
    # 绘制
    canvas.blit(a,(x,y))
    # 向右排列
    x += 256+20
    # 四个换行
    if x >= 1084:
        x = 0
        y += 410+10

# 主循环
while True:
    handleEvent()
    pygame.display.update()

