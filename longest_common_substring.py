# 最长公共子串长度


def lcs(str_a, str_b):
    len_a = len(str_a)
    len_b = len(str_b)
    # 定义dp表格
    dp = [[0] * len_b] * len_a
    for row in range(len_a):
        for col in range(len_b):
            if str_a[row] == str_b[col]:
                if col == 0 or row == 0:
                    dp[row][col] = 1
                elif row > 0 and col > 0:
                    dp[row][col] = dp[row - 1][col - 1] + 1

    return dp


print(lcs('fisher', 'hsiher'))
