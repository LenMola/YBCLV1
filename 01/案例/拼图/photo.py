# 国旗拼图
import pygame
from pygame.locals import *
import sys
import os,random
import easygui
pygame.init()
canvas = pygame.display.set_mode((1370,449))
pygame.display.set_caption("国旗拼图")
canvas.fill((255,255,255))
# 碎片图片
flag1 = pygame.image.load('flag/国旗拼图1.jpg')
flag2 = pygame.image.load('flag/国旗拼图2.jpg')
flag3 = pygame.image.load('flag/国旗拼图3.jpg')
flag4 = pygame.image.load('flag/国旗拼图4.jpg')
flag5 = pygame.image.load('flag/国旗拼图5.jpg')
flag6 = pygame.image.load('flag/国旗拼图6.jpg')
# 完整版
flag = pygame.image.load('flag/国旗拼图完整.jpg')
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print( event.pos[0],event.pos[1])
            x = event.pos[0]
            y = event.pos[1]
            # 判断所点击的位置是哪张碎片
            choose(x,y)
# 创建碎片类
class Piece():
    def __init__(self,x,y,img,num):
        self.x = x
        self.y = y
        self.img = img
        self.num = num
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def hit(self,x,y):
        return x > self.x and x < self.x + 228 and \
               y > self.y and y < self.y + 225
# 顺序图片
list = [flag1,flag2,flag3,flag4,flag5,flag6]


# 打乱图片
def cut():
    # 存储打乱的图片对象的列表
    global listnew
    listnew = []
    for i in range(3):
        # 产生随机数,表示图片下标
        n = random.randint(0,len(list)-1)
        # 向列表中添加第一排对应的随机图片,并且坐标右移动
        listnew.append(Piece(685+228*i,0,list[n],i))
        # 删除已选图片
        list.pop(n)
    for j in range(3,6):
        n = random.randint(0,len(list)-1)
        # 向列表中添加第二排对应的随机图片,并且坐标右移动
        listnew.append(Piece(685+228*(j-3),225,list[n],j))
        list.pop(n)
        for new in listnew:
            new.paint()
cut()
# 绘制打乱的图片
def paintcut():  
    for new in listnew:
        new.paint()
# 按顺序选择碎片并绘制
def choose(x,y):
    # 被选择的顺序碎片列表
    global listok
    if len(listok)>=6:
        return
    # 遍历碎片对象列表
    for new in listnew:
        # 点击检测
        if new.hit(x,y):
            # 将选中的图片添加进列表
            listok.append(new)
# 绘制选中的顺序图片
def paintok():  
    # 第一排:
    if len(listok)<=3:
        for i in range(len(listok)):
            canvas.blit(listok[i].img,(0+228*i,0))
            pygame.display.update()
    # 第二排
    else:
        for i in range(3,len(listok)):
            canvas.blit(listok[i].img,(0+228*(i-3),225))
            pygame.display.update()
listok = []
def over():
    global list
    if len(listok)==6:
        # 原始图片列表
        list = [flag1,flag2,flag3,flag4,flag5,flag6]
        # 最终所选碎片图片列表
        pic = []
        # 判断是否和正确顺序的图片列表一样
        for ok in listok:
            pic.append(ok.img)
        if pic==list:
            print('成功!')
            pygame.quit()
            os.system('python photowin.py')
        else:
            easygui.msgbox('失败啦!\n不要灰心!!\n再试一次吧!')
            # 清空屏幕,重绘白屏
            canvas.fill((255,255,255))
            cut()
            listok.clear()
            
while True:
    # paintcut()
    paintok()
    # 分界线
    pygame.draw.line(canvas,(255,0,0),(685,0),(685,898),5)
    pygame.display.update()
    over()
    handleEvent()
    pygame.time.delay(120)