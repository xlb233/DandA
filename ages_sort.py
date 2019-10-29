# 《剑指offer》上的例题
# 要求在O(n)时间和常数级的空间内对上万名员工的年龄进行排序
# 可以采用类似hash表的方式进行实现
# 该算法可以用在由非负整数构成的有限数组的排序中


def ages_sort(arr):
    # 由于统计的是员工年龄，区间应该为0-100，所以声明一个新数组，用来统计每个年龄出现次数，该数组长度应该是101
    arr_for_count = [0] * 101
    # 对每个年纪的人进行计数，比如18岁的人便在arr_for_count[18]的值自加1
    for age in arr:
        if age < 0 or age > 100:
            return "please enter correct ages"
        arr_for_count[age] += 1
    # 声明排序后的数组下标为0开始
    new_index = 0
    # 对arr_for_count数组进行遍历，若是对应年龄有值(arr_for_count[i]>0)，则进入内层循环，开始对原数组arr进行排序
    for i in range(len(arr_for_count)):
        for j in range(arr_for_count[i]):
            # 从下标为0开始重新给arr赋值
            arr[new_index] = i
            new_index += 1
    return arr


print(ages_sort([18, 29, 3, 1, 44, 0, 99, 100, 12, 6, 21, 23, 24]))
