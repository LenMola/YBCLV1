# 对口令
import tkinter as t
from PIL import ImageTk
window = t.Tk()
window.title('宝藏')
window.resizable(0,0)
bgImg = ImageTk.PhotoImage(file = 'images/钟离的宝库.jpg')
bg = t.Label(window,image=bgImg)
bg.pack()
# 创建输入框进行输入口令----------------------------------------------------------------------------------------------
p1 = t.Entry(window,bg = 'black',font=('隶书',34,),fg='white')
p1.place(x = 544,y = 70)
p2 = t.Entry(window,bg = 'black',font=('隶书',34,),fg='white')
p2.place(x = 544,y = 190)
# 验证函数
def check():
    # 获取输入框内容
    s1 = p1.get()
    s2 = p2.get()
    # 验证暗号
    if s1 == '宝塔镇河妖' and s2 == '地瓜地瓜，我是土豆':
        goldImg = ImageTk.PhotoImage(file = 'images/宝藏.jpg')
        gold = t.Label(window,image=goldImg)
        gold.place(x = 210,y = 270)
        # 循环+刷新屏幕
        window.mainloop()
    else:
        wrongImg = ImageTk.PhotoImage(file='images/守卫.png')
        gold = t.Label(window, image=wrongImg)
        gold.place(x=210, y=270)
        window.mainloop()
# 验证按钮
okImg = ImageTk.PhotoImage(file = 'images/确定.png')
ok = t.Button(window,bd=0,image=okImg,bg='black',command=check)
ok.place(x=1050,y = 120)

window.mainloop()