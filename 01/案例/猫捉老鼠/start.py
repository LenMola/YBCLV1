import pygame,sys,time
from pygame.locals import *
pygame.init()
canvas = pygame.display.set_mode((1024,650))
pygame.display.set_caption('猫捉老鼠')
# 加载图片
bg = pygame.image.load('images/背景.png')
c = pygame.image.load('images/猫_副本.png')
m = pygame.image.load('images/老鼠_副本.png')
r = pygame.image.load('images/路障_副本.png')
clock = pygame.image.load('images/倒计时.png')
catWin = pygame.image.load('images/汤姆赢.jpeg')
mouseWin = pygame.image.load('images/杰瑞赢.jpeg')
# 初始化音乐组件
pygame.mixer.init()
# 加载背景音乐
pygame.mixer.music.load('images/猫和老鼠.mp3')
# 音量
pygame.mixer.music.set_volume(1)
# 重复播放
pygame.mixer.music.play(-1)
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type==KEYDOWN and event.key==K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            print(event.pos[0],event.pos[1])
        if event.type == KEYDOWN :
            if event.key == K_LEFT :
                GameVar.x1 = -4
                GameVar.y1 = 0
            if event.key == K_RIGHT :
                GameVar.x1 = 4
                GameVar.y1 = 0
            if event.key == K_UP :
                GameVar.x1 = 0
                GameVar.y1 = -4
            if event.key == K_DOWN :
                GameVar.x1 = 0
                GameVar.y1 = 4
            if event.key == K_a :
                GameVar.x2 = -4
                GameVar.y2 = 0
            if event.key == K_d :
                GameVar.x2 = 4
                GameVar.y2 = 0
            if event.key == K_w :
                GameVar.x2 = 0
                GameVar.y2 = -4
            if event.key == K_s :
                GameVar.x2 = 0
                GameVar.y2 = 4
# 创建猫类
class Cat():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.width = 100
        self.height = 69
        self.life = 1
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def step(self):
        self.x += GameVar.x1
        self.y += GameVar.y1
    def outOfBounds(self):
        if self.x<=0:
            self.x=0
        if self.x>=1024-self.width:
            self.x=1024-self.width
        if self.y<=0:
            self.y=0
        if self.y>=650+30-self.width:
            self.y=650+30-self.width
    def hit(self,c):
        return c.x>self.x-c.width and c.x<self.x+self.width and \
            c.y > self.y - c.height and c.y < self.y + self.height
# 创建老鼠类
class Mouse():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.width = 80
        self.height = 93
        self.life = 1
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def step(self):
        self.x += GameVar.x2
        self.y += GameVar.y2
    def outOfBounds(self):
        if self.x<=0:
            self.x=0
        if self.x>=1024-self.width:
            self.x=1024-self.width
        if self.y<=0:
            self.y=0
        if self.y>=650-self.width:
            self.y=650-self.width
    def hit(self,c):
        return c.x>self.x-c.width and c.x<self.x+self.width and \
            c.y > self.y - c.height and c.y < self.y + self.height
# 创建路障类
class Roadblock():
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.width = 60
        self.height = 88
        self.life = 1
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def outOfBounds(self):
        if self.x<=30:
            self.x=30
        if self.x>=1000-30-self.width:
            self.x=1000-30-self.width
    def hit(self,c):
        return c.x>self.x-c.width and c.x<self.x+self.width and \
            c.y > self.y - c.height and c.y < self.y + self.height
# 存储游戏信息变量类
class GameVar():
    # 游戏状态变量
    state = 'RUNNING'
    # 比赛时间
    t = 60
    lastTime = 0
    interval = 1
    # 猫和老鼠的坐标改变值
    x1 = 4
    y1 = 0
    x2 = 4
    y2 = 0
    # 猫和老鼠的对象
    cat = Cat(50,500,c)
    mouse = Mouse(50,90,m)
    # 路障列表
    rbs = [
          Roadblock(255,135,r),
          Roadblock(730,175,r),
          Roadblock(260,460,r),
          Roadblock(710,460,r),
          Roadblock(490,320,r),
          Roadblock(475,30,r),
          ]
# 倒计时方法
def gameTime():
    # 画表
    canvas.blit(clock,(20,20))
    # 显示时间
    fillText(str(GameVar.t),(53,43))
    if not isActionTime(GameVar.lastTime, GameVar.interval):
        return
    GameVar.lastTime = time.time()
    GameVar.t -= 1
#控制时间
def isActionTime(lastTime,interval):
    if lastTime==0:
        return True
    currentTime=time.time()
    return currentTime-lastTime>=interval
# 画组件的方法  
def conPaint():
    # 画背景
    canvas.blit(bg,(0,0))
    # 画汤姆
    GameVar.cat.paint()
    # 画杰瑞
    GameVar.mouse.paint()
    # 画路障
    for rb in GameVar.rbs:
        rb.paint()
# 碰撞检测方法
def checkHit():
    # 检测猫碰撞到老鼠    
    if GameVar.cat.hit(GameVar.mouse):
        GameVar.state = 'CATWIN'
    # 检测时间是否到了
    if GameVar.t <= 0:
        GameVar.state = 'MOUSEWIN'
    # 检测杰瑞/汤姆  与路障的碰撞
    for rb in GameVar.rbs:
        if GameVar.cat.hit(rb):
            GameVar.state = 'MOUSEWIN'
    for rb in GameVar.rbs:
        if GameVar.mouse.hit(rb):
            GameVar.state = 'CATWIN'
# 组件移动
def conStep():
    GameVar.mouse.step()
    GameVar.cat.step()
# 写文字方法
def fillText(text, position, view=canvas):
    # 设置字体样式和大小
    my_font = pygame.font.SysFont("Courier New", 38)
    # 渲染文字
    text = my_font.render(text, True, (255, 255, 255))
    view.blit(text, position)
# 显示胜利的文字
def showWin():
    # 设置字体样式和大小，粗细
    my_font = pygame.font.SysFont("Segoe Script", 50,10)
    # 渲染文字
    text = my_font.render('WIN!!!!', True, (199, 71, 16))
    canvas.blit(text, (693,36))
# 主控方法
def control():
    # 画组件
    conPaint()
    # 运行状态
    if GameVar.state == "RUNNING":
        gameTime()
        conStep()
        GameVar.mouse.outOfBounds()
        GameVar.cat.outOfBounds()
        checkHit()
    # 猫赢
    elif GameVar.state == 'CATWIN':
        canvas.blit(catWin,(0,0))
        showWin()
    # 老鼠赢
    elif GameVar.state == 'MOUSEWIN':
        canvas.blit(mouseWin,(0,0))
        showWin()
# 主循环      
while True:
    control()
    # 调用事件检测
    handleEvent()
    # 刷新屏幕
    pygame.display.update()
    pygame.time.delay(15)