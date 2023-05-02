from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        xmin, ymin = 0, 0
        xmax, ymax = len(matrix)-1, len(matrix[0])-1
        response = []
        iter = 0
        l1, l2 = len(matrix)-1, len(matrix[0])-1
        if l1 == l2 and l1 == 0:
            return [matrix[0][0]]

        if l1 == 0:
            return matrix[0]
        if l2 == 0:
            response = [i[0] for i in matrix]
            return response

        while True:
            for j in range(ymin, ymax):
                print("1. index: {}, {}".format(xmin, j))
                response.append(matrix[xmin][j])
                # print(matrix[xmin][j])
            for i in range(xmin, xmax):
                print("2. index: {}, {}".format(i, ymax))
                response.append(matrix[i][ymax])
                # print(matrix[i][ymax])
            if l1 == l2:
                for j in range(ymax, ymin - 1, -1):
                    print("3. index: {}, {}".format(xmax, j))
                    response.append(matrix[xmax][j])
                    # print(matrix[xmax][j])
                for i in range(xmax - 1, xmin, -1):
                    print("4. index: {}, {}".format(i, ymin))
                    response.append(matrix[i][ymin])
                    # print(matrix[i][ymin])
            else:
                for j in range(ymax, ymin-1, -1):
                    print("3. index: {}, {}".format(xmax, j))
                    response.append(matrix[xmax][j])
                    if (l1 + 1) * (l2 + 1) == len(response):
                        return response
                    # print(matrix[xmax][j])
                # if (l1+1) * (l2+1) == len(response):
                #     return response
                for i in range(xmax-1, xmin, -1):
                    print("4. index: {}, {}".format(i, ymin))
                    response.append(matrix[i][ymin])
                    # print(matrix[i][ymin])

            xmax -= 1
            ymax -= 1
            xmin += 1
            ymin += 1

            iter += 1
            if len(matrix)-1 == iter or len(matrix[0]) - 1 == iter:
                return response


object_sol = Solution()
answer = object_sol.spiralOrder([[1,2,3,4],
                                 [5,6,7,8],
                                 [9,10,11,12]])
# answer = object_sol.spiralOrder([[2,3,4],
#                                  [5,6,7],
#                                  [8,9,10],
#                                  [11,12,13],
#                                  [14,15,16]])
# answer = object_sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12], [13, 14, 15, 16]])
# answer = object_sol.spiralOrder([[1, 2, 3, 4, 17],
# [5, 6, 7, 8, 18],
# [9, 10, 11, 12, 19],
# [13, 14, 15, 16, 20]])
print(*answer, sep=', ')

"""
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

0,0 x min y inc. xmin=0
0,1 
0,2
0,3 x inc y max ymax=3
1,3 
2,3 
3,3 x max y dec xmax=3
3,2 
3,1 
3,0 x dec y min ymin=0
2,0 
1,0 
1,1 xmin y inc ymax=2, xmin=1
1,2 
2,2 xmax y dec ymin=1 xmax=2
2,1

1 2 3 4 17
5 6 7 8 18
9 10 11 12 19
13 14 15 16 20

1 2 3 4 17 18 19 20 16 15 14 13 9 5 6 7 8 12 11 10

1  2  3  4  17 26
5  6  7  8  18 27
9  10 11 12 19 28
13 14 15 16 20 29
21 22 23 24 25 30

1 2 3 4 17 26 27 28 29 30 25 24 23 22 21 13 9 5 6 7 8 18 19 20 16 15 14 10 11 12
"""

"""
Explanation:
Anytime you are traversing in four directions only, left to right, top to bottom,
right to left and bottom to top.
"""
