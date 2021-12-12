class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        # define an array dp same as the size of nums, fill it with 0
        dp = [0 for i in range(len(nums))]
        # set the first to the first in nums
        dp[0] = nums[0]
        # find the maximum of the previous plus current OR the current
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            
        return max(dp)