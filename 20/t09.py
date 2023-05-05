# 点名
# 预留代码——读取文本中学生姓名
with open('学生姓名/class1.txt','r',encoding='utf-8') as f:
    names = f.read()
    class1 = names.split(' ')
with open('学生姓名/class2.txt','r',encoding='utf-8') as f:
    names = f.read()
    class2 = names.split(' ')
with open('学生姓名/class3.txt','r',encoding='utf-8') as f:
    names = f.read()
    class3 = names.split(' ')
with open('学生姓名/class4.txt','r',encoding='utf-8') as f:
    names = f.read()
    class4 = names.split(' ')
print('一班：',class1)
print('二班：',class2)
print('三班：',class3)
print('四班：',class4)
# 请在下面书写代码-------------------------------------------------------------------------------------------------------
# 利用while循环，逐个输出每个班级的学生：
# 一班：class1






# 二班：class2








# 三班：class3








# 四班：class4







