class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            stack.append(i)

            if len(stack) >= 3 and ''.join(stack[-3:]) == "abc":
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack) == 0
            