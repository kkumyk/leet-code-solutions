"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

class Solution:
    def moveZeroes(self, nums: list[int]):
        # initialise a variable to keep track of the position where non-zero elements should be places:
        non_zero_pos = 0

        for i in range(len(nums)):  # i = 0 1 2 3 4
            if nums[i] != 0:  # returns True when the found number is not zero: 1 3 12
                # if the current element is not zero, swap it with the element at non_zero_pos
                nums[i], nums[non_zero_pos] = nums[non_zero_pos], nums[i]
                non_zero_pos += 1
        return nums

    
solution = Solution()
print(solution.moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
