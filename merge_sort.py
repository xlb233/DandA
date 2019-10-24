# 分治，分和治
# merge是和(治)
import random


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        for obj in left[i:]:
            result.append(obj)
    if j < len(right):
        for obj in right[j:]:
            result.append(obj)
    return result


# merge_sort是分
def merge_sort(arr):
    # 终止条件
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 此处再次给left和right赋的值是终止条件后的left和right
    # 也就是只有一个值的数组
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


print(merge_sort([random.random() * 5000 for _ in range(10000)]))
