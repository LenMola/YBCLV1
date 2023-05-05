# 酷猫音乐
# 导入模块
import tkinter as t
from PIL import ImageTk
import pygame,easygui
pygame.init()
# 创建窗口
window = t.Tk()
# 设置标题
window.title('酷猫音乐')
# 设置大小
window.geometry('360x480')
# 背景图片三步曲
# 第一步：加载图片
bg = ImageTk.PhotoImage(file = 'images/Q版猫咪.png')
# 第二步：创建标签
b = t.Label(window,image=bg)
# 第三步：打包标签
b.pack()
# 声明变量表示歌曲名称
name = None
# 请在下方补充代码：---------------------------------------------------------------------------------------------------








# 主循环
window.mainloop()
