class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix[0])*len(matrix) - 1
        print("l", l, "r", r)
        while l <= r:
            m = (l + r) // 2

            (lst, pos) = self.expandToMatrix(m, matrix)
            print(m, (lst, pos))
            if matrix[lst][pos] == target:
                return True
            elif matrix[lst][pos] > target:
                r = m - 1
            else:
                l = m + 1

        return False

    def expandToMatrix(self, pos: int, matrix: List[List[int]]) -> (int, int):
        return (pos//(len(matrix[0])), pos%len(matrix[0]))