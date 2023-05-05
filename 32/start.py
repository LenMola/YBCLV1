# 动漫快看
# 导入tkinter模块
import os
import tkinter as t
# 导入ImageTk模块
from PIL import ImageTk
# 导入os模块------------------------------------------------------------------------------------------------------------


# 创建窗口，赋值给变量window
window = t.Tk()
# 设置标题
window.title('动漫快看')
# 设置窗口宽高
window.geometry('1130x830')
# 固定窗口大小
window.resizable(0,0)
# 绘制背景三步曲
# 第一步：加载图片
bg = ImageTk.PhotoImage(file = 'images/凹凸世界.jpg')
# 第二步：创建标签——存储图片，文字等信息的介质
b = t.Label(window,image=bg)
# 第三步：放置标签/打包标签
b.pack()
# 跳转函数
def begin():
    print('点击了开始按钮！')
    # 销毁当前窗口
    window.destroy()
    os.system('python index.py')

# 创建开始按钮
# 第一步：加载图片
start = ImageTk.PhotoImage(file='images/start.png')
# 第二步：创建按钮
s = t.Button(window,image=start,bd=0,command=begin)
# 第三步：放置按钮
s.place(x = 460,y = 700)




# 主循环
window.mainloop()

