# 酷猫音乐
# 导入模块
import tkinter as t
from PIL import ImageTk
import pygame,easygui
pygame.init()
# 导入ttk模块
from tkinter import ttk

# 创建窗口
window = t.Tk()
# 设置标题
window.title('酷猫音乐')
# 设置大小
window.geometry('360x480')
# 固定大小
window.resizable(0,0)
# 背景图片三步曲
# 第一步：加载图片
bg = ImageTk.PhotoImage(file = 'images/Q版猫咪.png')
# 第二步：创建标签
b = t.Label(window,image=bg)
# 第三步：打包标签
b.pack()
# 声明变量表示歌曲名称
name = None
# 请在下方补全代码：---------------------------------------------------------------------------------------------------
# 创建下拉列表对象






# 创建播放函数
def _play():
    # 删除pass后进行补全代码
    pass






# 创建播放按钮
play = ImageTk.PhotoImage(file = 'images/播放.png')
p = t.Button(window,image=play,bd = 0,command=_play)
p.place(x = 220,y = 40)
# 主循环
window.mainloop()
