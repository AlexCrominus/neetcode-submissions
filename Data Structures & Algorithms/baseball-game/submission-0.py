class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            match op:
                case "+":
                    v1 = stack[-1]
                    v2 = stack[-2]
                    stack.append(v1+v2)
                case "D":
                    stack.append(stack[-1]*2)
                case "C":
                    stack.pop()
                case _:
                    stack.append(int(op))

        return sum(stack)