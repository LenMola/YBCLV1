import easygui
# 输入一个整数，判断是奇数还是偶数
n = int( easygui .enterbox('请输入一个整数：') )
if n%2 == 0:
    easygui.msgbox(str(n)+'是偶数')
else:
    easygui.msgbox(str(n)+'是奇数')