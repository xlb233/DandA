import random


def shell_sort(arr):
    n = len(arr)
    # 定义递增序列的间距，并逐步缩小间距直到1
    gap = 1
    while gap < len(arr) / 3:
        gap = gap * 3 + 1
    while gap > 0:
        # 对递增序列进行插入排序
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j] < arr[j - gap]:
                arr[j], arr[j - gap] = arr[j - gap], arr[j]
                j -= gap
        gap = int(gap / 3)
    return arr


print(shell_sort([random.random() * 5000 for _ in range(10000)]))
