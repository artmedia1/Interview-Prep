from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for idx, num in enumerate(nums):
            if num in dictionary:
                return [dictionary[num], idx]
            dictionary[target - num] = idx


if __name__ == "__main__":
    test = Solution()
    numList = [2,16,25,33]
    pair = test.twoSum(numList, 35)
    print(pair)