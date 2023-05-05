#coding:utf-8
import pygame
from pygame.locals import *
import time
import random
import sys
import os
#初始化pygame环境
pygame.init()

#创建一个长宽分别为1300/700窗口
os.environ[ 'SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 25)
canvas = pygame.display.set_mode((1000,600))
canvas.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("打砖块")

#加载图片
#画框
bg1=pygame.image.load("images/bg2.png")
#背景
bg2=pygame.image.load("images/bg1.png")
#挡板
board=pygame.image.load("images/board.png")
#右边云
c1=pygame.image.load("images/c2.png")
#左边云
c2=pygame.image.load("images/c1.png")
#血量
life=pygame.image.load("images/life.png")
#失败
lose=pygame.image.load("images/lose.png")
#胜利
win=pygame.image.load("images/win.png")
#弹球
b=pygame.image.load("images/ball.png")
#敌人1
e1=pygame.image.load("images/enemy1.png")
#敌人2
e2=pygame.image.load("images/enemy2.png")
#敌人3
e3=pygame.image.load("images/enemy3.png")

def handleEvent():  
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit() 
            sys.exit()
        #鼠标移动事件
        if event.type == pygame.MOUSEMOTION:
            if Game.states == 'RUNNING':
                Game.player.x = event.pos[0] - Game.player.width / 2

#玩家类
class Player():
    def __init__(self,x,y,img):
        self.width=217
        self.height=10
        self.x=x
        self.y=y
        self.img=img
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    #越界方法
    def outOfBounds(self):
        if self.x<=30:
            self.x=30
        if self.x>=1000-30-self.width:
            self.x=1000-30-self.width
    #碰撞方法
    def hit(self,c):
        return c.x > self.x - c.width and c.x < self.x + self.width and c.y > self.y - c.height and c.y < self.y + self.height        
#弹球类        
class Ball():
    def __init__(self,x,y,img):
        self.width=46
        self.height=46
        self.x=x
        self.y=y
        self.img=img
        self.life=3
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def step(self):
        self.x=self.x+Game.m
        self.y=self.y-Game.n
        if self.x<30:
            Game.m=random.randint(10,20)
        if self.x>970:
            Game.m=-random.randint(10,20)
        if self.y<15:
            Game.n=-random.randint(10,20)



#敌人类        
class Enemy():
    def __init__(self,x,y,img):
        self.width=132
        self.height=48
        self.x=x
        self.y=y
        self.img=img
        self.life=1
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    #碰撞方法
    def hit(self,c):
        return c.x > self.x - c.width and c.x < self.x + self.width and c.y > self.y - c.height and c.y < self.y + self.height

#云类
class Cloud():
    def __init__(self,x,y,img):
        self.width=132
        self.height=48
        self.x=x
        self.y=y
        self.img=img
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    #碰撞方法
    def hit(self,c):
        return c.x > self.x - c.width and c.x < self.x + self.width and c.y > self.y - c.height and c.y < self.y + self.height
   
#游戏类        
class Game():
    # 小球随机速度
    m=random.randint(10,20)
    n=random.randint(10,20)
    enemies=[Enemy(156,15,e1),Enemy(293,15,e2),Enemy(430,15,e3),Enemy(567,15,e2),Enemy(704,15,e1),# 第一排
             Enemy(156,15+48,e1),Enemy(293,15+48,e2),Enemy(430,15+48,e3),Enemy(567,15+48,e2),Enemy(704,15+48,e1),] # 第二排
    clouds=[Cloud(30,15,c1),Cloud(844,15,c2)]
    ball=Ball(500,450,b)
    player=Player(400,500,board)
    states='RUNNING'
    
#画组件方法  
def conPaint():
    canvas.blit(bg1,(0,0))
    Game.player.paint()
    canvas.blit(bg2,(0,0))    
    Game.ball.paint() 
    #画敌人
    for enemy in Game.enemies:
        enemy.paint()
    #画云彩
    for cloud in Game.clouds:
        cloud.paint()
    #画生命值
    if Game.ball.life==3:
        canvas.blit(life,(975,70))
        canvas.blit(life,(975,90))
        canvas.blit(life,(975,110))
    if Game.ball.life==2:
        canvas.blit(life,(975,70))
        canvas.blit(life,(975,90))
    if Game.ball.life==1:
        canvas.blit(life,(975,70))
        
#组件移动方法   
def conStep():
    Game.ball.step()

#检测碰撞       
def checkHit():
    for enemy in Game.enemies:
        if enemy.hit(Game.ball):
            enemy.life=0
            Game.m=-1*Game.m
            Game.n=-random.randint(10,20)
    for cloud in Game.clouds:
        if cloud.hit(Game.ball):
            Game.m=-1*Game.m
            Game.n=-random.randint(10,20)
    if Game.player.hit(Game.ball):
        Game.n=random.randint(10,20)
    if Game.ball.y>600:
        Game.ball.life=Game.ball.life-1
        Game.ball.x=500
        Game.ball.y=200
     
#删除敌人方法 
def conDelete():
    for enemy in Game.enemies:
        if enemy.life==0:
            Game.enemies.remove(enemy)
    
#游戏结束方法   
def gameOver():
    if len(Game.enemies)==0 or Game.ball.life<=0:
        Game.states='OVER'

#状态控制方法            
def control():
    if Game.states=='RUNNING':
        conPaint()
        conStep()
        Game.player.outOfBounds()
        checkHit()
        conDelete()
        gameOver()
        
    if Game.states=='OVER':  
        conPaint()  
        #胜利
        if len(Game.enemies)==0:
            canvas.blit(win,(250,150))
        #失败
        if Game.ball.life<=0:
            canvas.blit(lose,(250,150))

while True:
    #调用状态控制方法
    control()
    # 监听有没有按下退出按钮
    handleEvent()
    # 更新屏幕内容
    pygame.display.update()
    #延时1秒 
    pygame.time.delay(10)