def shell_sort(arr):
    n = len(arr)
    # 定义递增序列的间距，并逐步缩小间距直到1
    gap = n / 2
    while gap > 0:
        # 对递增序列进行插入排序
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= gap
        gap /= 2
    return arr


print(shell_sort([3, -2, 0, 0, 7, 1, 2, 3, -9]))
