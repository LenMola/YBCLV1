#coding:utf-8
import pygame,time,random,sys,os,easygui
from pygame.locals import *
from sys import exit
#初始化pygame环境
pygame.init()
pygame.font.init()
os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d"%(50,60)
#创建窗口
canvas = pygame.display.set_mode((1214,608))
canvas.fill((255,255,255))
#设置窗口标题
pygame.display.set_caption("元宵节猜灯谜")
bg = pygame.image.load('images/bg.jpg')
#写文字方法
def fillText(text, position):
    TextFont = pygame.font.Font('images/font1.ttf', 30)
    newText = TextFont.render(text, True, (255,255,255))
    canvas.blit(newText, position)
#创建列表存储灯谜和答案
questions = ['古代有，现代无;商周有，秦汉无;唐朝有，宋朝无。 (打一字)','句中有一字，每月猜三次，就是秀才猜，也得猜十日。 (打一字)',
             '年轻头发白，年老黑油油，睡觉常戴帽，著书扶它走。 (打一文具)','身穿八卦，脚踏钉耙，胡椒眼睛，锥子尾巴。 (打一动物)',
             '铜盆底，铁盆盖，两把剪，八根带。 (打一动物)','绒毛轻又轻，飞舞像伞兵。随风到处飘，安家把根生。 (打一植物)',
             '本来一大片，变成条条线，是线不做衣，碗里常常见。 (打一食物)','弯弯的背，细细的牙，一早在人头上爬。 (打一物)',
             '两兄弟一样高，一日三餐不长高。 (打一物)','有风身不动，一动就生风，只怕秋风起，凄凉入冷宫。 (打一物)']
answers = ['口','旬','毛笔','乌龟','螃蟹','蒲公英','面条','梳子','筷子','扇子']
def handleEvent(): 
    for event in pygame.event.get():
        #退出窗口
        if event.type == QUIT or  event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
#循环显示灯谜    
while True:
    #添加喜庆背景
    canvas.blit(bg,(0,0))
    #随机产生灯谜
    a = random.randint(0,len(questions)-1)
    fillText(questions[a],(170,300))
    pygame.display.update()
    time.sleep(1)
    #循环猜灯谜
    while True:
        answer = easygui.enterbox('请猜灯谜答案：')
        if answer == answers[a]:
            easygui.msgbox('您猜对了！')
            questions.pop(a)
            answers.pop(a)
            break
        elif answer == None:
            break
        else:
            easygui.msgbox('您猜错了！')   
    pygame.display.update()
    handleEvent()