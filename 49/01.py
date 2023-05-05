import os
n = 1
# 获取当前目录所以文件
for name in os.listdir('./'):
    print(name)
    # 分隔文件名和后缀
    print(os.path.splitext(name))
    if n<=9:
        # 重命名
        os.rename(name,'0'+str(n)+os.path.splitext(name)[1])
    else:
        # 重命名
        os.rename(name, str(n) + os.path.splitext(name)[1])
    n+=1

