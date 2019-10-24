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
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


print(merge_sort([random.random() * 5000 for _ in range(10000)]))
