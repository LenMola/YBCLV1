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
    # 获取所有的书籍文件名
    novels = os.listdir('novel')
    result = []
    for novel in novels:
        if name in novel:
            print('猜您想看：' + novel)
            result.append(novel)
    if result == []:
        print('未查询到相关书籍！')
    else:
        pass
        # 在查询到的书籍文件名中分隔出书名
        # 1.创建新列表存储所有书名
        names = []
        for r in result:
            names.append(r.split('-')[0])
        print(names)

        # 书籍按钮列表
        books = []
        x = 10
        y = 164
        bookImg = ImageTk.PhotoImage(file='images/封面.jpg')
        for name in names:
            # 创建书籍按钮
            b = t.Button(window, bd=0, image=bookImg, font=('微软雅黑', 10, 'bold'), text=name, compound='center')
            books.append(b)
        # 记数换行
        i = 0
        for book in books:
            book.place(x = x,y = y)
            x += 130
            i += 1
            if i % 3 == 0:
                y += 225
                x = 10

        window.mainloop()

# 重置界面
def update():
    global window,entry,s
    window.destroy()
    # 创建窗口
    window = t.Tk()
    # 设置标题
    window.title('我的书架')
    # 固定大小
    window.resizable(0, 0)
    # 背景
    # 1.加载图片
    bgImg = ImageTk.PhotoImage(file='images/书架.jpg')
    # 2.创建标签
    bg = t.Label(window, image=bgImg)
    # 3.打包标签
    bg.pack()
    # 输入框：颜色228 165 112，十六进制：#E4A570
    entry = t.Entry(window, bg="#E4A570", font=('微软雅黑', 20), width=15)
    entry.place(x=86, y=50)
    # 创建窗口
    window = t.Tk()
    # 设置标题
    window.title('我的书架')
    # 固定大小
    window.resizable(0, 0)
    # 背景
    # 1.加载图片
    bgImg = ImageTk.PhotoImage(file='images/书架.jpg')
    # 2.创建标签
    bg = t.Label(window, image=bgImg)
    # 3.打包标签
    bg.pack()
    # 输入框：颜色228 165 112，十六进制：#E4A570
    entry = t.Entry(window, bg="#E4A570", font=('微软雅黑', 20), width=15)
    entry.place(x=86, y=50)
    # 查找按钮
    searchImg = ImageTk.PhotoImage(file='images/查找.png')
    s = t.Button(window, image=searchImg, text='查找', font=('微软雅黑', 15),
                 compound='center', cursor="hand2", bd=0, command=search)
    s.place(x=356, y=47)



# 查找按钮
searchImg = ImageTk.PhotoImage(file = 'images/查找.png')
s = t.Button(window,image=searchImg,text='查找',font=('微软雅黑',15),
             compound='center',cursor="hand2",bd=0,command=search)
s.place(x = 356,y = 47)
# 主循环
window.mainloop()






