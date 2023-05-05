# 微信
# 导入模块
import tkinter as t
from PIL import ImageTk
import easygui
# 创建窗口
window = t.Tk()
# 设置标题
window.title('微信')
# 固定大小
window.resizable(0,0)
# 背景三步曲-----------------------------------------------------------
# 1.加载图片
bgImg = ImageTk.PhotoImage(file = 'images/微信1.jpg')
# 2.创建标签
bg = t.Label(window,image=bgImg)
# 3.打包标签
bg.pack()
# 声明变量表示用户名和密码
name = None
password = None
# 输入账号函数
def input1():
    global name
    name = easygui.enterbox('请输入微信号：')
# 输入密码函数
def input2():
    global password
    password = easygui.enterbox('请输入密码：')
def Login():
    # 验证账号密码
    if name == None:
        easygui.msgbox('请输入微信号！')
        return
    if password == None:
        easygui.msgbox('请输入密码！')
        return
    if name == 'xiaoyuan' and password == '666999':
        easygui.msgbox('登录成功！')
    else:
        easygui.msgbox('登录失败，请检查账号或密码！')
# 输入账号按钮
uImg = ImageTk.PhotoImage(file = 'images/微信号1.jpg')
u = t.Button(window,bd = 0,image=uImg,command=input1)
u.place(x = 110,y = 170)
# 输入密码按钮
pImg = ImageTk.PhotoImage(file = 'images/密码1.jpg')
p = t.Button(window,bd = 0,image=pImg,command=input2)
p.place(x = 110,y = 222)
# 登录按钮
Limg = ImageTk.PhotoImage(file = 'images/登录1.png')
L = t.Button(window,bd = 0,image=Limg,command=Login)
L.place(x = 80,y = 520)
# 窗口循环
window.mainloop()

