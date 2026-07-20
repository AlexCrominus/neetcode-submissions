class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # inc = []
        # dec = []

        # ret = [0 for a in range(len(temperatures))]

        # for i in range(len(temperatures)):
        #     print(inc, dec)

        #     t = temperatures[i]
        #     if len(inc) == 0:
        #         inc.append([t, i])
        #     elif t > inc[-1][0]:
        #         inc.append([t, i])
        #     else:
        #         dec.append([t, i])
            

        stack = []
        ret = [0 for a in range(len(temperatures))]

        for i in range(len(temperatures)):
            print(ret)
            t = temperatures[i]
            
            if not stack:
                stack.append([t,i])
                continue

            if t <= stack[-1][0]:
                stack.append([t,i])

            if t > stack[-1][0]:
                while stack and t > stack[-1][0]:
                    for s in stack:
                        ret[s[1]]+=1
                    val = stack.pop()

                stack.append([t,i])

        for s in stack[:-1]:
            ret[s[1]]=0

        return ret

