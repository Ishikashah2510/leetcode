# matrix = []
# g = 0
#
#
# def dfs(arr, ind):
#     global matrix
#     if ind == len(arr):
#         return True
#
#     set_flag = False
#     sum_val = 0
#     count = 0
#     temp = []
#
#     for i in range(ind, len(arr)):
#         sum_val += arr[i]
#         count += 1
#
#         if sum_val / count >= g:
#             set_flag = True
#             if not dfs(arr, i + 1):
#                 continue
#             temp.extend(arr[ind:i + 1])
#             matrix.append(temp.copy())
#             break
#
#     return set_flag
#
#
# def check_size(matrix, arr):
#     c = sum(len(subarray) for subarray in matrix)
#     return c == len(arr)
#
#
# if __name__ == "__main__":
#     N, g = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     dfs(arr, 0)
#
#     if not matrix or not check_size(matrix, arr):
#         print(-1)
#     else:
#         print(len(matrix))
#         # matrix = sorted(matrix, key=lambda x: len(x))
#         for subarray in matrix[::-1]:
#             print(len(subarray), end=" ")
#             # print(subarray)
#
# # 19 -3
# # -6 -9 -9 5 1 7 0 -14 5 -6 -15 -9 -8 4 8 10 -11 9 -4
#
#
# # 4
# # 6 1 9 3


strList = ['zoom', 'wz', 'wedhwezwz']


# zoom
result = []

for each_str in strList:
    char_to_swap = each_str[0]
    swap = 'z'

    if char_to_swap == 'z':
        for each_char in each_str[1:]:
            if each_char != 'z':
                char_to_swap = each_char
                swap = 'y'
                break

    res_str = ""
    for each_char in each_str:
        if each_char == char_to_swap:
            res_str += swap
        elif each_char == swap:
            res_str += char_to_swap
        else:
            res_str += each_char

    result.append(res_str)

print(result)
