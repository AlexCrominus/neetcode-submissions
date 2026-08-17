class Solution:
    def climbStairs(self, n: int) -> int:
        mem = collections.defaultdict(int)

        def dfs(n):
            if n == 0:
                return 1
            if n < 0 :
                return 0
            if n in mem:
                return mem[n]

            count = 0

            count += dfs(n-1)
            count += dfs(n-2)
            mem[n] = count

            return count

        return dfs(n)