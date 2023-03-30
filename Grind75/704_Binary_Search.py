from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        copy = nums
        start = 0
        end = len(nums)
        middle = int((start + (end-start)/2))

        for i in range(len(nums)):
            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                end = middle
                middle = int((start + (end-start)/2))
            else:
                start = middle
                middle = int((start + (end-start)/2))
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,3,5,9,12,14,16] 
    target = 16
    test = solution.search(nums, target)
    print(test)