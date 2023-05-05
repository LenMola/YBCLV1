# 动物大全
# 导入模块
import tkinter as t
from PIL import ImageTk
# 导入ttk模块
from tkinter import ttk

# 创建窗口
window = t.Tk()
# 设置标题
window.title('动物大全')
# 设置大小
window.geometry('600x568')
# 固定大小
window.resizable(0,0)
# 背景图片三步曲
# 第一步：加载图片
bg = ImageTk.PhotoImage(file ='images/动物世界.jpg')
# 第二步：创建标签
b = t.Label(window,image=bg)
# 第三步：打包标签
b.place(x = 0,y = 116)
# 声明变量表示歌曲名称
name = None
# 请在下方补全代码：---------------------------------------------------------------------------------------------------
# 创建下拉列表对象







# 创建展示函数
def show():
    # 获取下拉列表的选中项
    global name
    # 获取选中项：-------------------------------------------------------------------------------------------------------

    if name == None:
        return
    if name == '请选择动物':
        # 重新加载图片
        bg = ImageTk.PhotoImage(file='images/动物世界.jpg')
        # 更新标签
        b.image = bg
        b.config(image=bg)
    else:
        # 重新加载图片
        bg = ImageTk.PhotoImage(file='images/'+name+'.jpg')
        # 更新标签
        b.image = bg
        b.config(image=bg)

# 创建播放按钮
play = ImageTk.PhotoImage(file = 'images/start.png')
p = t.Button(window,image=play,bd = 0,command=show)
p.place(x = 360,y = 45)
# 主循环
window.mainloop()




