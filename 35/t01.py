# 获取fruits文件夹中所有的水果图片，并筛选所有带'桃'的水果
import os
# 检索文件夹中的所有文件
fruits = os.listdir('fruits')
# 输出所有文件
print(fruits)
# 创建列表，准备放置所有'桃'
tao = []
# 遍历检索结果
for fruit in fruits:
    # 判断是否含“桃”
    if '桃' in fruit:
        # 含“桃”的放入列表
        tao.append(fruit)
# 输出最终结果
print(tao)


