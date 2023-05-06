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
# 背景三步曲
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
    # 4.获取输入框内容


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
# 1.账号输入框


# 2.密码输入框


# 3.设置密文显示


# 登录按钮
Limg = ImageTk.PhotoImage(file = 'images/登录1.png')
L = t.Button(window,bd = 0,image=Limg,command=Login)
L.place(x = 80,y = 520)
# 窗口循环
window.mainloop()

