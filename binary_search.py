def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return arr[mid]
    return None


def binary_search_recursive(arr, target, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    if arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return mid


print(binary_search_recursive([3, 4, 5, 6, 8, 9, 10], 9, 0, 6))
