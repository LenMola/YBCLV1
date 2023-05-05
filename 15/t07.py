# 随机点名系统
# 导入模块
import random,easygui

# 创建列表存储学生姓名
names = ['嘟嘟','熊大','熊二','光头强','李老板']

# 随机数:表示学生下标，应该是0-学生人数-1
n = random.randint(0,4)

# 将随机数作为下标获取学生名称
easygui.msgbox('本次中奖幸运观众为'+names[n])
