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
# 创建列表存储猫咪/狗狗品种
cats = ['巴吉度','暹罗猫','喜玛拉雅猫','哈士奇',
        '美国卷耳猫','拉布拉多','异国猫','阿拉斯加',
        '西伯利亚猫','山东狮子猫','法国斗牛犬','挪威森林猫']
# 使用pop()方法移出狗子品种
cats.pop(0)
cats.pop(2)
cats.pop(3)
cats.pop(4)
cats.pop(6)

# 请在下方补充代码------------------------------------------------------------------------------------------------------
# 使用append()添加其他猫咪品种，填充背景
cats.append('金吉拉')
cats.append('褴褛猫')
cats.append('美国短尾猫')
cats.append('土耳其安哥拉猫')
cats.append('哈瓦纳棕毛猫')


# -----------------------------------------------------------------------------------------------------------------------
# 绘制背景
canvas.blit(bg,(0,0))
# 绘制列表中的所有角色图片
y = 0
x = 0
for cat in cats:
    # 加载对应图片
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


