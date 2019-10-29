# 同样是《剑指offer》中的一道例题
# 把一个数组最开始的若干元素放到该数组最后去，我们称之为数组的旋转
# 求一个递增数组的旋转中的最小值
# 当然可以遍历寻找，但是这就不是面试官所想要看到的解法了
# 使用二分查找的思路进行解答


def min_of_rotated_array(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    # 定义左右指针
    # 由于是递增数组的旋转，所以左边数字应该大于或者是等于右边数字的（当然若是旋转0个数字的话即没有发生任何旋转，那么就是左边数字小于右边数字）
    left = 0
    right = len(arr) - 1
    # 将mid_index初始化为左侧指针，是为了防止出现旋转0位数字的情况
    mid_index = left

    # 顺序查找的代码
    def min_in_order(lst):
        result = lst[0]
        for i in range(len(lst)):
            if result > lst[i]:
                result = lst[i]
        return result

    while arr[left] >= arr[right]:
        # 当left和right指针相距1时，right指针指向的就是最小值
        if right - left == 1:
            mid_index = right
            break
        # 取得数组中间的数arr[mid_index]
        # 若该数大于left，则说明中间数在前一个递增数组中，最小值在后面与第二个递增数组交界处，则将left指针移到mid_index处；
        # 反之则mid_index出现在后一个递增数组中，最小值是自己或在前面，将right指针移至mid_index处
        mid_index = (right + left) // 2
        # 当左右两侧数字与中间数字相等时，无法判断中间数字到底属于哪一个子序列，所以只能顺序查找
        if arr[left] == arr[right] == arr[mid_index]:
            return min_in_order(arr)
        if arr[mid_index] >= arr[left]:
            left = mid_index
        elif arr[mid_index] <= arr[right]:
            right = mid_index
    return arr[mid_index]


print(min_of_rotated_array([1]))
