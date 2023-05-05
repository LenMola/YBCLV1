# 导入运行依赖库
import pygame,sys,random,time
from pygame.locals import *
pygame.init()
# 创建窗口
canvas=pygame.display.set_mode((500,600))
pygame.display.set_caption('病毒大战')
# 加载图片
doctor = pygame.image.load('images/医生.png')
doctor1 = pygame.image.load('images/医生_辛苦.jpg')
doctor2 = pygame.image.load('images/胜利.jpg')
bg = pygame.image.load('images/背景_副本.jpg')
pill = pygame.image.load('images/药丸.png')
virus1 = pygame.image.load('images/病毒1号.png')
virus2 = pygame.image.load('images/病毒2号.png')
virus3 = pygame.image.load('images/病毒3号.png')
virus4 = pygame.image.load('images/病毒4号.png')
# 事件处理方法
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        # 将医生跟着鼠标左右移动
#         if event.type == MOUSEBUTTONDOWN:
#             print(event.pos[0],event.pos[1])
        if event.type == MOUSEMOTION:
            if GameVar.state == '运行':
                GameVar.doc.x = event.pos[0]-GameVar.doc.width/2
        # 键盘按下事件:按下空格调用医生的攻击方法,发射药丸
        if event.type == KEYDOWN and event.key == K_SPACE:
            if GameVar.state=='运行':
                GameVar.doc.attact()
                
# 创建医生类
class Doctor():
    def __init__(self):
        self.width = 100
        self.height = 98
        self.x = 200
        self.y = 500
        self.img = doctor  
        self.HP = 3
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def attact(self):
        GameVar.pills.append(Pill(self.x+self.width/2-18,self.y-36,36,36,1,pill))
# 药丸类
class Pill():
    def __init__(self,x,y,width,height,life,img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.life = life
        self.img = img
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def step(self):
        self.y -= 4
    #定义hit方法判断两个对象之间是否发生碰撞
    def hit(self,c):
        return c.x>self.x-c.width and c.x<self.x+self.width and \
               c.y>self.y-c.height and c.y<self.y+self.height
# 病毒类
class Virus():
    def __init__(self,x,y,width,height,type,life,score,img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.life = life
        self.score = score
        self.img = img
    #创建paint方法
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    #创建step方法
    def step(self):
        self.y += 2
# 游戏组件、信息、标志、对象类
class GameVar():
    # 游戏状态变量
    state = '运行'
    # 医生对象
    doc = Doctor()
    # 创建分数变量
    score = 0
    # 药丸列表
    pills = []
    # 病毒列表
    viruses = []
    # 产生病毒相关的时间变量
    lastTime = 0
    interval = 1
#添加时间间隔的方法
def isActionTime(lastTime, interval):
    if lastTime == 0:
        return True
    currentTime = time.time()
    return currentTime - lastTime >= interval
# 病毒生成方法
def conEnter():
    #随机生成坐标
    x1 = random.randint(0,500-48)
    x2 = random.randint(0,500-52)
    x3 = random.randint(0,500-66)
    x4 = random.randint(0,500-92)
    #根据随机整数的值生成不同的病毒
    n = random.randint(0,100)
    #判断是否到了产生病毒的时间
    if not isActionTime(GameVar.lastTime,GameVar.interval):
        return
    GameVar.lastTime = time.time()
    if n <= 50:
        GameVar.viruses.append(Virus(x1, -50, 48, 50, 1, 1, 1, virus1))
    elif n <= 75:
        GameVar.viruses.append(Virus(x2, -60, 52, 60, 2, 2, 2, virus2))
    elif n <= 90: 
        GameVar.viruses.append(Virus(x3, -70, 66, 70, 3, 3, 3, virus3))
    elif n <= 100: 
        GameVar.viruses.append(Virus(x4, -80, 92, 80, 4, 4, 4, virus4))
# 写文字方法，用于显示分数，劳累值
def fillText(text,position):
    #设置字体
    TextFont = pygame.font.Font('images/font3.ttf',22)
    #设置字体其他样式
    newText = TextFont.render(text,True,(0,0,0))
    canvas.blit(newText,position)
# 画组件方法
def conPaint():
    canvas.blit(bg,(0,0))
    GameVar.doc.paint()
    # 遍历画出所有药丸
    for p in GameVar.pills:
        p.paint()
    # 遍历画出所有病毒
    for v in GameVar.viruses:
        v.paint()
    # 显示分数和劳累值
    fillText('分    数:'+str(GameVar.score),(10,10))
    fillText('劳累值:'+str(GameVar.doc.HP),(400,10))
# 移动组件
def conStep():
    for p in GameVar.pills:
        p.step()
    for v in GameVar.viruses:
        v.step()
def checkHit():
    for v in GameVar.viruses:
        for p in GameVar.pills:
            if p.hit(v):
                v.life -= 1
                GameVar.pills.remove(p)
    # 如果病毒列表中有病毒超过了警戒线
    for v in GameVar.viruses:
        if v.y> 521:
            # 医生的体力值下降1
            GameVar.doc.HP-=1
            GameVar.viruses.remove(v)
    
# 删除生命值为0的病毒
def canDelete():
    for v in GameVar.viruses:
        if v.life <= 0:
            GameVar.score += v.score
            GameVar.viruses.remove(v)
# 主控方法
def control():
    if GameVar.state == '运行':
        conEnter()
        conPaint()
        conStep()
        checkHit()
        canDelete()
        if GameVar.doc.HP<=0:
            GameVar.state = '结束'
        if GameVar.score>=100:
            GameVar.state = '胜利'
    # 如果游戏状态进入结束：
    elif GameVar.state == '结束':
        conPaint()
        # 画出医生累的图片
        canvas.blit(doctor1,(0,0))
    # 如果游戏状态进入胜利：
    elif GameVar.state == '胜利':
        conPaint()
        # 画出医生累的图片
        canvas.blit(doctor2,(0,0))
    
while True:
    control()
    handleEvent()
    pygame.time.delay(10)
    pygame.display.update()
    