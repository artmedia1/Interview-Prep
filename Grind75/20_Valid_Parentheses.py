class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "[":
                stack.append("]")
            elif char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif len(stack) == 0 or stack.pop() != char:
                return False
        return len(stack) == 0 #Check for edge case when s is just 1 character, ie. s = "["

if __name__ == "__main__":
    test = Solution()
    numList = [2,16,25,33]
    pair = test.twoSum(numList, 35)
    print(pair)