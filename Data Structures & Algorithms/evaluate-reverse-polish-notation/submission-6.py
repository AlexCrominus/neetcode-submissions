class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        op_list = "+-*/"
        
        for tok in tokens:
            if tok not in op_list:
                stack.append(tok)
            else:
                val1 = stack.pop()
                val2 = stack.pop()

                res = eval(f"{val2} {tok} {val1}")
                print(res)
                stack.append(int(res))
        print(stack)
        return int(stack.pop())