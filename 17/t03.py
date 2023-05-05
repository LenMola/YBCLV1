# 仓鼠盲盒
# 导入模块
import pygame,random
from pygame.locals import *
# 初始化
pygame.init()

# 创建窗口
canvas = pygame.display.set_mode(flags = FULLSCREEN)
pygame.display.set_caption('仓鼠盲盒')

# 展示文本
def showText(text, position):
    TextFont = pygame.font.Font('./fonts/锐字温帅小可爱.ttf', 256)
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
# 背景

# 奖品路径列表



# 加载倒计时音效

# 播放倒计时音效

# 倒计时3




# 重复：倒计时2






# 重复：倒计时1






# 随机抽取奖品路径


# 加载随机奖品图片


# 绘制奖品



while True:
    handleEvent()
    pygame.display.update()


