import pygame
from tool.tools import getPoint
pygame.init()
canvas = pygame.display.set_mode((1000,600))
pygame.display.set_caption('DIY小元宵')

case1 = pygame.image.load("images/case1.png")
case2 = pygame.image.load("images/case2.png")
case3 = pygame.image.load("images/case3.png")
canvas.blit(case1,(0,0))

rgbs=[(255,0,0),(255,255,0),(0,255,0),(0,255,255),
      (0,0,255),(255,0,255),(255,255,255),(0,0,0)]
rects=[pygame.Rect(12,188,18,18),pygame.Rect(12,213,18,18),pygame.Rect(12,238,18,18),
       pygame.Rect(12,263,18,18),pygame.Rect(12,288,18,18),pygame.Rect(12,313,18,18),
       pygame.Rect(12,338,18,18),pygame.Rect(12,363,18,18)]

colors=[]
for (i,rgb) in enumerate(rgbs):
    colors.append((rects[i],rgb))
def check(pos):
    global penColor
    for (i,color) in enumerate(colors):
        if color[0].collidepoint(pos):
            penColor=color[1]
#2.创建画笔函数
penColor=(0,0,0)
startPos = None
drawing=False
def draw(position,penColor):
    global startPos
    if drawing:
        pointsList = getPoint(startPos, position)
        for p in pointsList:
            pygame.draw.circle(canvas,penColor, p, 2)
    startPos = position
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouseX=pos[0]
            mouseY=pos[1]
            check(pos)
            #1.切换方案
            if 942 <= mouseX <= 992 and 231 <= mouseY <= 281:   
                canvas.blit(case1,(0,0))
            elif 942 <= mouseX <= 992 and 296 <= mouseY <= 346:  
                canvas.blit(case2,(0,0)) 
            elif 942 <= mouseX <= 992 and 361 <= mouseY <= 411:  
                canvas.blit(case3,(0,0)) 
         
            #3.实现画笔功能    
            if 170 <= mouseX <= 820 and 190 <= mouseY <= 490:        
                drawing=True
                startPos = pos

            
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            mouseX=pos[0]
            mouseY=pos[1]
            if not (170 <= mouseX <= 820 and 190 <= mouseY <= 490):    
                drawing=False
            #3.实现画笔功能
            if drawing:
                draw(pos,penColor)
        if event.type == pygame.MOUSEBUTTONUP:
            #3.实现画笔功能
            drawing = False
    pygame.display.update()
