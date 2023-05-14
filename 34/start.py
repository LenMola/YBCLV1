# 我的书架
# 导入模块
import tkinter as t
from PIL import ImageTk
import os
# 创建窗口
window = t.Tk()
# 设置标题
window.title('我的书架')
# 固定大小
window.resizable(0,0)
# 背景
# 1.加载图片
bgImg = ImageTk.PhotoImage(file = 'images/书架.jpg')
# 2.创建标签
bg = t.Label(window,image=bgImg)
# 3.打包标签
bg.pack()
# 输入框：颜色228 165 112，十六进制：#E4A570
entry = t.Entry(window,bg="#E4A570",font=('微软雅黑',20),width=15)
entry.place(x=86,y=50)
# 查找函数
def search():
    # 获取输入框的输入信息
    name = entry.get()
    print('您要查询的书名/作者为：' + name)
    # 获取所有的书籍文件名---------------------------------------------------------------------------------------





# 查找按钮
searchImg = ImageTk.PhotoImage(file = 'images/查找.png')
s = t.Button(window,image=searchImg,text='查找',font=('微软雅黑',15),
             compound='center',cursor="hand2",bd=0,command=search)
s.place(x = 356,y = 47)
# 主循环
window.mainloop()






