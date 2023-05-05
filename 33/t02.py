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
def Login():
    global name ,password
    name = e1.get()
    password = e2.get()
    # 验证账号密码
    if not name :
        easygui.msgbox('请输入微信号！')
        return
    if not password :
        easygui.msgbox('请输入密码！')
        return
    if name == 'xiaoyuan' and password == '666999':
        easygui.msgbox('登录成功！')
    else:
        easygui.msgbox('登录失败，请检查账号或密码！')
# 账号输入框
e1 = t.Entry(window,width=16,font = ('微软雅黑',21))
e1.place(x=80,y=170)
# 密码输入框
e2 = t.Entry(window,width=16,font = ('微软雅黑',21))
e2.place(x=80,y=220)
# 设置密文显示
e2['show'] = '*'
# 登录按钮
Limg = ImageTk.PhotoImage(file = 'images/登录1.png')
L = t.Button(window,bd = 0,image=Limg,command=Login)
L.place(x = 80,y = 520)
# 窗口循环
window.mainloop()

