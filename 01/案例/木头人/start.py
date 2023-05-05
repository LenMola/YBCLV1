# 导入依赖的运行库:pygame游戏库,时间time,随机数random
import pygame,sys,time,random
from pygame.locals import *
pygame.init()
# 创建窗口
canvas = pygame.display.set_mode((480,650))
pygame.display.set_caption('木头人')
# 加载图片文件
clock = pygame.image.load('images/倒计时.png')
timeOver = pygame.image.load('images/时间到.png')
bg = pygame.image.load('images/教室.jpg')
bg1 = pygame.image.load('images/gameover.png')
bg2 = pygame.image.load('images/win.png')
t_b = pygame.image.load('images/教师背影.png')
t_f = pygame.image.load('images/教师正脸.png')
s = pygame.image.load('images/学生.png')
table = pygame.image.load('images/讲桌.png')
# 加载背景音乐
pygame.mixer.music.load('music/小孙同学 - 卡通 (伴奏).mp3')
# 设置音量
pygame.mixer.music.set_volume(1)
# 循环播放
pygame.mixer.music.play(-1)
# 事件检测
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        # 按下空格,停止学生移动
        if event.type == KEYDOWN and event.key == K_SPACE:
            GameVar.go = False
        # 松开空格,学生继续移动
        if event.type == KEYUP and event.key == K_SPACE:
            GameVar.go = True
        # 用于测试元素坐标
#         if event.type == MOUSEBUTTONDOWN:
#             print(event.pos[0],event.pos[1])
# 老师类
class Teacher():
    def __init__(self,x,y,width,height,img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = t_b
        self.face = False
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))

# 学生类
class Student():
    def __init__(self,x,y,width,height,img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def step(self):
        self.y -= 0.3

# 时间间隔
def isActionTime(lastTime,interval):
    if lastTime == 0:
        return True
    currentTime = time.time()
    return currentTime-lastTime>=interval
# 工具方法-写文字方法
def fillText(text, position, view=canvas):
    # 设置字体样式和大小
    my_font = pygame.font.SysFont("Curlz MT", 38)
    # 渲染文字
    text = my_font.render(text, True, (255, 255, 255))
    view.blit(text, position)
#计时方法
def gameTime():
    canvas.blit(clock,(20,20))
    fillText(str(GameVar.t),(53,43))
    if not isActionTime(GameVar.n,1):
        return
    GameVar.n = time.time()
    GameVar.t -= 1
# 封装游戏组件的类
class GameVar():
    # 时间
    t = 30
    n = 0
    # 状态
    state = 'RUNNING'
    begin = 0
    lastTime = 0
    interval = 1
    # 学生行动的标志
    go = True
    # 师生对象
    stu = Student(200,550,100,164,s)
    teacher = Teacher(180,30,66,99,t_b)
def componentPaint():
    canvas.blit(bg,(0,0))
    GameVar.teacher.paint()
    canvas.blit(table,(100,120))
    GameVar.stu.paint()
def componentStep():
    GameVar.stu.step()
# 老师随机动作的方法:有可能转身,有可能背对
def turn():
    if GameVar.state != 'RUNNING':
        return
    if GameVar.begin <100:
        GameVar.begin += 1
        return
    n = random.randint(0,100)
    if isActionTime(GameVar.lastTime, GameVar.interval):
        GameVar.lastTime = time.time()
        # 转身的概率:39％
        if n<=39:
            GameVar.teacher.face=True
            GameVar.teacher.img=t_f
        else:
            GameVar.teacher.face=False
            GameVar.teacher.img = t_b
# 根据游戏状态,控制游戏行为的方法
def gameControl():
    # 运行
    if GameVar.state == 'RUNNING':
        # 倒计时 
        gameTime()
        # 时间到了,状态变成时间到
        if GameVar.t<=0:
            GameVar.state = 'TIMEOVER'
    if GameVar.state == 'TIMEOVER':
        canvas.blit(timeOver,(50,200))
        canvas.blit(clock,(20,20))
        fillText(str(GameVar.t),(53,43))
    #   到,输了
    if GameVar.teacher.face==True and GameVar.go==True:
        GameVar.state = 'OVER'
    if GameVar.state =='OVER':   
        canvas.blit(bg1,(10,200))
        canvas.blit(clock,(20,20))
        fillText(str(GameVar.t),(53,43))
    # 如果游戏是运行状态没有输,并且没有按空格,那么就让学生往上走
    if GameVar.state == 'RUNNING' and GameVar.go==True:
        componentStep()
    # 如果学生的y坐标小于等于140,就表示胜利
    if GameVar.stu.y<=140:
        GameVar.state = 'WIN'
        canvas.blit(bg2,(10,200))
        canvas.blit(clock,(20,20))
        fillText(str(GameVar.t),(53,43))
# 死循环
while True:
    # 画组件
    componentPaint()
    # 调用游戏控制方法
    gameControl()
    # 调用老师转身方法
    turn()
    # 更新屏幕
    pygame.display.update()
    # 检测事件
    handleEvent()


