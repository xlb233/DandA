def search_one_by_one(matrix, path_to_find):
    rows = len(matrix)
    cols = len(matrix[0])
    # 初始化二维数组，以记录matrix中被访问的元素
    visited = [[False for col in range(cols)] for row in range(rows)]
    # current_path_length变量用来记录已经找到的子路径的长度
    current_path_length = 0
    for row in range(rows):
        for col in range(cols):
            if has_path_core(matrix, rows, cols, path_to_find, row, col, current_path_length, visited):
                return True
    return False


def has_path_core(matrix, rows, cols, path_to_find, row, col, current_path_length, visited):
    if current_path_length is len(path_to_find):
        return True
    has_path = False
    if 0 <= row <= rows and 0 <= col <= cols:
        current_element = matrix[row][col]
        if current_element == path_to_find[current_path_length] and visited[row][col] is False:
            current_path_length += 1
            visited[row][col] = True
            has_path = has_path_core(matrix, rows, cols, path_to_find, row - 1, col, current_path_length, visited) or \
                       has_path_core(matrix, rows, cols, path_to_find, row + 1, col, current_path_length, visited) or \
                       has_path_core(matrix, rows, cols, path_to_find, row, col - 1, current_path_length, visited) or \
                       has_path_core(matrix, rows, cols, path_to_find, row, col + 1, current_path_length, visited)
    # 回溯
    if has_path is False:
        current_path_length -= 1
        visited[row][col] = False
    return has_path


print(search_one_by_one([['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']], 'bfce'))


