
# 文化长廊
import tkinter as tk
from PIL import ImageTk
from PIL import Image
import os
import easygui
from tkinter import ttk
# 界面搭建
window = tk.Tk()
window.title('文化长廊')
window.geometry('1200x800')
window.resizable(0, 0)
image = Image.open('images/文化长廊背景.jpg')
bg = ImageTk.PhotoImage(image)
bgLabel = tk.Label(window,image = bg,)
bgLabel.pack()
# 读取知识
def read(name):
    with open(name,encoding = 'utf-8') as f:
        return f.read()
# 展示信息
def showMsg(*args):
    # 获取下拉列表的选项
    msg = cbox.get()
    if msg == '开国大典':
        show(read('知识库/开国大典.txt'))
    elif msg == '抗美援朝':
        show(read('知识库/抗美援朝.txt'))
    elif msg == '两弹一星':
        show(read('知识库/两弹一星.txt'))
    elif msg == '尼克松访华':
        show(read('知识库/尼克松访华.txt'))
    elif msg == '改革开放':
        show(read('知识库/改革开放.txt'))
    elif msg == '上海世博会':
        show(read('知识库/上海世博会.txt'))
    elif msg == '香港回归':
        show(read('知识库/香港回归.txt'))
# 创建下拉列表
cbox = ttk.Combobox(window,width = 25,font = ('黑体',15,'bold italic'))
# 设置下拉列表的选项
cbox['values'] = ['请选择事件',
                  '开国大典',
                  '抗美援朝',
                  '两弹一星',
                  '尼克松访华',
                  '改革开放',
                  '上海世博会',
                  '香港回归',
                  ]
# 设置默认值
cbox.current(0)
# 设置只读
cbox['state'] = 'readonly'
# 放置下拉列表
cbox.place(x = 0,y = 260)
# 为下拉列表的点击事件绑定处理函数
cbox.bind('<<ComboboxSelected>>',showMsg)




# 右侧文化展示区
def show(message):
    img = ImageTk.PhotoImage(file = 'images/文化长廊背景遮盖.jpg')
    bg2 = tk.Label(window,image = img,bd = 0)
    bg2.place(x = 400,y = 0)
    # 文本框组件------------------------------------------------------------------------------------------------------

    # 放置文本框

    # 显示文本信息



    window.mainloop()


window.mainloop()






