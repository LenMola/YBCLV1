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
# 下方书写代码----------------------------------------------------------------------------------------------------------






# 主循环
window.mainloop()

