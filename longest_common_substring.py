# 最长公共子串长度


def lcs(str_a, str_b):
    # 定义答案需要的一些变量
    # 最长的公共字符串长度、起止点
    # 用一个数组将lcs存储起来（其实更pythonic的办法是直接用切片，但是过于pythonic会导致思维过于python化）
    max_length = 0
    substring_start_index = 0
    substring_end_index = 0
    longest_substring_lst = []
    # 定义dp表格
    rows = len(str_a)
    cols = len(str_b)
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    # 用str_a的字符逐个遍历str_b的字符，看有无相同的
    for row in range(rows):
        for col in range(cols):
            # 若是有相同的，便从dp表格上一行的上一列数字上加上1，表示公共字符串延长了1
            if str_a[row] == str_b[col]:
                # 此处判断行或列是否为0，主要是为了防止在第一行或是第一列就出现相同字符的情况，防止从前行或前列的最后一个数字来加一，导致数据出错。
                if col == 0 or row == 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row - 1][col - 1] + 1
            # 此处判断公共字符串是否已经最长
            if dp[row][col] > max_length:
                max_length = dp[row][col]
                # 若已经是最长的，则以str_a为标杆，LCS的终点就是row，行号
                substring_end_index = row
                # LCS的列就是row行号减去LCS的长度加上1
                substring_start_index = substring_end_index - max_length + 1
    # 将找到的子字符串放入list中
    for i in range(substring_start_index, substring_end_index + 1):
        longest_substring_lst.append(str_a[i])
    return dp, max_length, ''.join(longest_substring_lst)


print(lcs('fisher', 'hsiher'))
