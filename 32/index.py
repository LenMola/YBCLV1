# 选择动漫界面
import easygui

print('进入选择动漫界面！')
# 导入tkinter模块
import tkinter as t
# 导入ImageTk模块
from PIL import ImageTk
# 导入ttk模块
from tkinter import ttk
# 导入os模块
import os,easygui


# 创建窗口，赋值给变量window
window = t.Tk()
# 设置标题
window.title('动漫快看')
# 设置窗口宽高
window.geometry('1130x900')
# 固定窗口大小
window.resizable(0,0)
# 绘制背景三步曲
# 第一步：加载图片
bg = ImageTk.PhotoImage(file = 'images/bg2.jpg')
# 第二步：创建标签——存储图片，文字等信息的介质
b = t.Label(window,image=bg)
# 第三步：放置标签/打包标签
b.pack()
# 添加动漫选项下拉列表
cbox = ttk.Combobox(window,font = ('楷体',27,'bold'))
# 设置下拉列表的选项
cbox['values'] = ['请选择动漫：',
                  '猫和老鼠',
                  '蜡笔小新',
                  '海绵宝宝',
                  '爆笑虫子',
                  '喜羊羊与灰太狼',
                  ]
# 设置默认值
cbox.current(0)
# 设置只读
cbox['state'] = 'readonly'
# 放置下拉列表
cbox.place(x = 100,y = 80)

# 播放动漫函数
def play():
    print('点击了播放按钮')
    # 获取下拉列表的选中项
    name = cbox.get()
    print('播放：'+name)
    if name == '请选择动漫：':
        easygui.msgbox('请选择动漫哦！')
        return
    # 销毁当前界面-----------------------------------------------------------------------------------------------

    # 跳转动漫播放界面



# 创建开始按钮
# 第一步：加载图片
playimg = ImageTk.PhotoImage(file='images/播放2.png')
# 第二步：创建按钮
p = t.Button(window,image=playimg,bd=0,command=play)
# 第三步：放置按钮
p.place(x = 530,y = 72)



# 主循环
window.mainloop()





