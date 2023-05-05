# 导入运行库
import pygame,sys,os,easygui
from pygame.locals import *
pygame.init()
# 创建窗口界面,起名canvas
canvas = pygame.display.set_mode((1024,642))
pygame.display.set_caption('我的mp3')
# 加载图片
bg = pygame.image.load('images/MP3.jpg')
ball = pygame.image.load('images/球.png')
last = pygame.image.load('images/上一页.jpg')
next = pygame.image.load('images/下一页.jpg')
add = pygame.image.load('images/音量+.jpg')
minus = pygame.image.load('images/音量-.jpg')
play = pygame.image.load('images/播放.jpg')
mouse = pygame.image.load('images/鼠标.png')
# 初始化音乐组件
pygame.mixer.init()
# 加载默认的背景音乐
pygame.mixer.music.load('mp3/文武贝 - 夜的钢琴曲5.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
# 创建事件检测方法
def handleEvent():
    # 遍历所有事件
    for event in pygame.event.get():
        # 处理关闭界面
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        # 鼠标移动事件控制鼠标图片
        if event.type == MOUSEMOTION:
            Mp3Var.mx = event.pos[0]
            Mp3Var.my = event.pos[1]
        # 按下键盘:实现暂停和继续播放
        if event.type == KEYDOWN and event.key == K_SPACE:
            # 如果暂停标志是True,就暂停,并让标志变为False
            if Mp3Var.pause == True:
                pygame.mixer.music.pause()
                Mp3Var.pause = False
            # 否则就继续播放,并将标志变为True
            else:
                pygame.mixer.music.unpause() 
                Mp3Var.pause = True
        # 鼠标点击事件：
        if event.type == MOUSEBUTTONDOWN :
            # 测试鼠标当前坐标
#             print(event.pos[0],event.pos[1])
            # 按键说明的展开与关闭
            if 780<=event.pos[0]<=1016 and 200<=event.pos[1]<=235:
                if Mp3Var.switch == False:
                    Mp3Var.switch = True
                elif Mp3Var.switch == True:
                    Mp3Var.switch = False
            # 点击了播放按钮,就可以播放选中的音乐啦
            if 388<=event.pos[0]<=636 and 204<=event.pos[1]<=452:
                if Mp3Var.play == True:
                    pygame.mixer.music.play(0)
                    Mp3Var.play = False
                elif Mp3Var.play == False:
                    pygame.mixer.music.stop()
                    Mp3Var.play = True
            # 如果点击了下一页按钮:
            if 660<=event.pos[0]<=710 and 210<=event.pos[1]<=450:
                Mp3Var.n += 1
            # 上一页
            elif 315<=event.pos[0]<=365 and 210<=event.pos[1]<=450:
                Mp3Var.n -= 1
            # 音量加
            if 385<=event.pos[0]<=620 and 130<=event.pos[1]<=170:
                if Mp3Var.volume<=1:
                    Mp3Var.volume += 0.1
                pygame.mixer.music.set_volume(Mp3Var.volume)
            # 音量减
            elif 385<=event.pos[0]<=620 and 475<=event.pos[1]<=520:
                if Mp3Var.volume>=0:
                    Mp3Var.volume -= 0.1
                pygame.mixer.music.set_volume(Mp3Var.volume)
            # 根据鼠标点击的文字坐标范围,选中相应的歌曲
            # 如果是第一页歌单
            if Mp3Var.n%3==0:
                if 25<=event.pos[0]<=215 and 225<=event.pos[1]<=245:
                    Mp3Var.name = '萧敬腾 - 百里守约'
                    pygame.mixer.music.load('mp3/百里守约.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=257 and 265<=event.pos[1]<=290:
                    Mp3Var.name = '伊格赛听、叶里 - 谪仙'
                    pygame.mixer.music.load('mp3/谪仙.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=175 and 300<=event.pos[1]<=325:
                    Mp3Var.name = '张韶涵 - 破茧'
                    pygame.mixer.music.load('mp3/破茧.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=219 and 345<=event.pos[1]<=365:
                    Mp3Var.name = '要不要买菜 - 下山'
                    pygame.mixer.music.load('mp3/要不要买菜 - 下山.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=252 and 390<=event.pos[1]<=410:
                    Mp3Var.name = '沈谧仁、奇然 - 琵琶行 '
                    pygame.mixer.music.load('mp3/沈谧仁、奇然 - 琵琶行.mp3')
                    Mp3Var.play = True
            # 第二页歌单
            if Mp3Var.n%3==1:
                if 25<=event.pos[0]<=260 and 225<=event.pos[1]<=245:
                    Mp3Var.name = 'Ice Paper - 心如止水'
                    pygame.mixer.music.load('mp3/Ice Paper - 心如止水.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=240 and 265<=event.pos[1]<=290:
                    Mp3Var.name = '梦然 - 少年 '
                    pygame.mixer.music.load('mp3/梦然 - 少年.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=285 and 300<=event.pos[1]<=325:
                    Mp3Var.name = 'July - My Soul'
                    pygame.mixer.music.load('mp3/July - My Soul.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=255 and 345<=event.pos[1]<=365:
                    Mp3Var.name = '无限王者团 - 千灯之约'
                    pygame.mixer.music.load('mp3/千灯之约.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=285 and 390<=event.pos[1]<=410:
                    Mp3Var.name = 'Two Steps...-Victory '
                    pygame.mixer.music.load('mp3/Two Steps From Hell - Victory.mp3')
                    Mp3Var.play = True
            # 第3页歌单
            if Mp3Var.n%3==2:
                if 25<=event.pos[0]<=260 and 225<=event.pos[1]<=245:
                    Mp3Var.name = '海伦 - 桥边姑娘'
                    pygame.mixer.music.load('mp3/海伦 - 桥边姑娘.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=240 and 265<=event.pos[1]<=290:
                    Mp3Var.name = '朴树 - 平凡之路 '
                    pygame.mixer.music.load('mp3/朴树 - 平凡之路.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=285 and 300<=event.pos[1]<=325:
                    Mp3Var.name = '音阙诗听... - 落雁'
                    pygame.mixer.music.load('mp3/音阙诗听、王梓钰、昆玉 - 落雁.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=255 and 345<=event.pos[1]<=365:
                    Mp3Var.name = '周深 - 大鱼'
                    pygame.mixer.music.load('mp3/周深 - 大鱼.mp3')
                    Mp3Var.play = True
                if 25<=event.pos[0]<=285 and 390<=event.pos[1]<=410:
                    Mp3Var.name = '阿冗 - 你的答案 '
                    pygame.mixer.music.load('mp3/阿冗 - 你的答案.mp3')
                    Mp3Var.play = True
            
# 存储音乐播放器相关变量的类(类属性)
class Mp3Var():
    # 音量
    volume = 0.5
    # 歌名
    name = '......'
    # 歌单页码
    n = 0
    # 按键说明的开关
    switch = False
    # 播放或者停止的控制变量
    play = True
    # 暂停或者续播的控制变量
    pause = True
    # 鼠标图片的x，y坐标
    mx = 500
    my = 500
# 写文字方法
def fillText(text, position):
    TextFont = pygame.font.Font('images/kaiti.TTF',20)
    newText = TextFont.render(text,True,(255,255,125))
    canvas.blit(newText, position)
# 第一页歌单
def mp3_0():
    fillText('A.萧敬腾 - 百里守约 ', (25,225))
    fillText('B.伊格赛听、叶里 - 谪仙 ', (25,265))
    fillText('C.张韶涵 - 破茧 ', (25,305))
    fillText('D.要不要买菜 - 下山 ', (25,345))
    fillText('E.沈谧仁、奇然 - 琵琶行', (25,385))
# 第二页歌单
def mp3_1():
    fillText('A.Ice Paper - 心如止水', (25,225))
    fillText('B.梦然 - 少年 ', (25,265))
    fillText('C.July - My Soul ', (25,305))
    fillText('D.无限王者团 - 千灯之约 ', (25,345))
    fillText('E.Two Steps...-Victory', (25,385)) 
# 第三页歌单
def mp3_2():
    fillText('A.海伦 - 桥边姑娘', (25,225))
    fillText('B.朴树 - 平凡之路 ', (25,265))
    fillText('C.音阙诗听... - 落雁 ', (25,305))
    fillText('D.周深 - 大鱼 ', (25,345))
    fillText('E.阿冗 - 你的答案', (25,385)) 
# 主控方法
def control():
    # 画背景
    canvas.blit(bg,(0,0))
    # 隐藏鼠标
    pygame.mouse.set_visible(False)
    # 显示使用说明
    fillText('退出请按ESC',(780,130))
    fillText('已选歌曲:'+Mp3Var.name+'点击播放按钮播放',(300,600))
    # 第一页歌单
    if Mp3Var.n%3==0:
        mp3_0()
    # 第二页歌单
    if Mp3Var.n%3==1:
        mp3_1()
    # 第三页歌单
    if Mp3Var.n%3==2:
        mp3_2()
    # 按键说明的显示
    canvas.blit(ball,(770,200))
    fillText('点击展开/关闭按键说明', (810,208))
    if Mp3Var.switch == True:
        canvas.blit(last,(818,266))
        fillText('上一页', (868,266))
        canvas.blit(next,(818,316))
        fillText('下一页', (868,316))
        canvas.blit(add,(818,366))
        fillText('音量+', (868,366))
        canvas.blit(minus,(818,416))
        fillText('音量-', (868,416))
        canvas.blit(play,(818,461))
        fillText('播放/停止', (868,466))
        fillText('鼠标点击选歌',(818,516))
        fillText('空格暂停/继续',(818,566))
    # 画鼠标
    canvas.blit(mouse,(Mp3Var.mx,Mp3Var.my))
# 主循环
while True:
    # 调用主控方法
    control()
    # 调用事件监测方法
    handleEvent()
    # 刷新屏幕界面
    pygame.display.update()











