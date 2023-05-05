# 禁止套娃！！
a = '清明上河图'
b = ['清明上河图']
c = [a,b]
d = '1234 5678'
e = ['123',123,c]
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(c[1]))
print(len(e[0]))



