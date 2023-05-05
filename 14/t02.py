# 吭思仁抽奖系统
import easygui,random
# 欢迎词
easygui.msgbox('欢迎参与吭思仁大抽奖！')
# 设置奖项：
prizes = [
    '一等奖：华为笔记本一台！',
    '二等奖：华为平板一台！',
    '三等奖：华为耳机一副！',
    '四等奖：游乐园一日游！',
    '特等奖：五套试卷！',
]

# 生成随机数
n = random.randint(1,5)
# 根据随机数的值范围指定奖品
# 随机数为1则是一等奖
if n == 1:
    easygui.msgbox('恭喜您获得：'+prizes[0])
# 随机数为2则是二等奖
elif n == 2:
    easygui.msgbox('恭喜您获得：' + prizes[1])
# 随机数为3则是三等奖
elif n == 3:
    easygui.msgbox('恭喜您获得：' + prizes[2])
# 随机数为4则是四等奖
elif n == 4:
    easygui.msgbox('恭喜您获得：' + prizes[3])
# 其他的都是特等奖
else:
    easygui.msgbox('恭喜您获得：' + prizes[4])

