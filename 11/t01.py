import easygui
score = easygui.enterbox('')
if score>100:
    easygui.msgbox('1')
else:
    easygui.msgbox('2')