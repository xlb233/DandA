# 《图解算法》将一块矩形土地划分为小方块，求最大方块的边长

# divide a rectangular land into several smaller square lands, seek a longest geometry


def divide_land(a, b):
    if a > b:
        width = a
        height = b
    else:
        width = b
        height = a
    if width % height == 0:
        return height
    else:
        a = height
        b = width % height
        return divide_land(a, b)


print(divide_land(1680, 640))
