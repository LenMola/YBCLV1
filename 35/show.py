# 导入模块
import tkinter as t,sys,os
from PIL import ImageTk
# 获取书籍名
name = sys.argv[1]
print(name)
# 获取书籍内容
novels = os.listdir('novel')
for novel in novels:
    if name in novel:
        # 读取书籍文件
        with open('novel/'+novel,'r',encoding='utf-8') as f:
            content = f.read()
# 创建窗口
window = t.Tk()
# 设置标题
window.title(name)
# 固定大小
window.resizable(0,0)
# 背景
# 1.加载图片
bgImg = ImageTk.PhotoImage(file = 'images/阅读器.jpg')
# 2.创建标签
bg = t.Label(window,image=bgImg)
# 3.打包标签
bg.pack()
# 创建多行文本框组件:指定字体，大小，宽高，背景色--------------------------------------------------------------------------

# 设置坐标

# 设置文本内容:预留代码中，我们已经将书籍的内容读取到了变量content中





window.mainloop()