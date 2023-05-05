import math


def getPoint(start, end):
    points = [(start[0], start[1])]
    len_x = end[0] - start[0]
    len_y = end[1] - start[1]
    length = math.sqrt(len_x ** 2 + len_y ** 2)
    if length <= 0:
        length = 0.01
    step_x = len_x / length
    step_y = len_y / length
    for i in range(int(length)):
        points.append((points[-1][0] + step_x, points[-1][1] + step_y))
    points = map(lambda x: (round(x[0]), round(x[1])), points)
    return list(set(points))
