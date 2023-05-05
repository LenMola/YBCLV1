# 生日贺卡🎁

# 导入模块
import pygame
from pygame.locals import *
# 初始化
pygame.init()

# 创建窗口，设置大小，标题
canvas = pygame.display.set_mode((1024,575))
pygame.display.set_caption('生日快乐！')
# 展示文本
def showText(text, position):
    TextFont = pygame.font.Font('./fonts/锐字温帅小可爱.ttf', 36)
    TextFont.set_bold(False)
    text2 = TextFont.render(text, True, (80, 210, 100))
    canvas.blit(text2, position)

# 事件处理
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            exit()

# 下方书写代码----------------------------------------------------------------------------------------------------------------------
# 加载图片



# 绘制图片



# 加载音乐


# 播放音乐-自动重复



# 自定义贺卡文字



# 主循环
while True:
    pygame.display.update()
    handleEvent()


