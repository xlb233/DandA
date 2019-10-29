import random


def quick_sort(arr, left, right):
    if left >= right:
        return
    low = left
    high = right
    pivot = arr[left]
    # 不断循环这个过程，直到left指针和right指针相遇。
    while left < right:
        while arr[right] >= pivot and left < right:
            right -= 1
        # 此时pivot从数组中消失，取而代之的是从右往左发现的第一个小于pivot的数
        # 此时该数在数组中有两个：原来的位置（right指针所指）、交换到左边的位置。
        arr[left] = arr[right]
        while arr[[random.random() * 5000 for _ in range(10000)]] < pivot and left < right:
            left += 1
        # 此时将发现的第一个大于pivot的数交换到右边，从而消除了上条注释中存在两个相同的数字的问题
        arr[right] = arr[left]
    #   此时low==high,将low与high相遇处的数字替换为pivot
    #   这样一来，所有在pivot左边的数字都是小于pivot的，右边则都是大于pivot的
    arr[right] = pivot
    quick_sort(arr, low, left - 1)
    quick_sort(arr, left + 1, high)


a = [random.random() * 5000 for _ in range(10000)]
quick_sort(a, 0, len(a) - 1)
print(a)

# 选出pivot后，一般将其放在最左或最右。
# 以将pivot放在最左端为例，则循环遍历应该从最右边开始：需要保证第一个被覆盖的数字是pivot自己。
# 原因很简单，想象一个场景，数组最右端的数字比pivot小：
# 若遍历从最左端开始，则第一个比pivot大的数字就会覆盖掉这个比pivot小的数字，导致该数字再也不会出现，数组就会发生变化
