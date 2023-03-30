class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        for char in s:
            if char in first:
                first[char] = first[char] + 1
            else:
                first[char] = 1

        for char in t:
            if char not in first:
                return False
            if char in second:
                second[char] = second[char] + 1
            else:
                second[char] = 1

        for char in first:
            if char not in second:
                return False
            if first[char] != second[char]:
                return False

        return True



if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    test = solution.isAnagram(s, t)
    print(test)