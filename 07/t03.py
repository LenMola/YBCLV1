# 试玩弹窗
import easygui
# 输入年龄
age = int( easygui.enterbox('请输入你的年龄：') )
# 使用if-else语句判断是否需要买票
if age <= 6:
    easygui.msgbox('小朋友免费哦！')
else:
    easygui.msgbox('超过六岁要买票哦！')
