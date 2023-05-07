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






window.mainloop()