import random


def quick_sort(arr, left, right):
    if left >= right:
        return
    low = left
    high = right
    pivot = arr[left]
    while left < right:
        while arr[right] >= pivot and left < right:
            right -= 1
        arr[left] = arr[right]
        while arr[left] < pivot and left < right:
            left += 1
        arr[right] = arr[left]
    #   此时low==high,将pivot数字与low与high相遇处的数字进行交换
    #   这样一来，所有在pivot左边的数字都是小于pivot的，右边则都是大于pivot的
    arr[left] = pivot
    quick_sort(arr, low, left - 1)
    quick_sort(arr, left + 1, high)


a = [22, 1, 3, 88, 2, 21, 3, -1, 0, -10, 4, 5]
quick_sort(a, 0, len(a) - 1)
print(a)
