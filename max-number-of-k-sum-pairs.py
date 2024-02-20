class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:

        nums.sort()
        operation = 0
        left = 0
        right = len(nums) - 1  # 3

        while left < right:
            if (
                nums[left] + nums[right] == k
            ):  # nums[right] will be 4 - the last item in the array
                operation += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1

        return operation


solution = Solution()
print(solution.maxOperations([1, 2, 3, 4], 5))  # 5
