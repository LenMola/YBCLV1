# 定时炸弹————读秒版
# 导入模块





# 预留代码，播放爆炸音效----------------------------------------------------------------------------------------------------------------------
import pygame,easygui
pygame.mixer.init()
pygame.mixer.music.load('sound/爆炸.mp3')
pygame.mixer.music.play()

easygui.msgbox('BOOM!!')




