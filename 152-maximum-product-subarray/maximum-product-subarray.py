class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        currMaxProductSubarr = nums[0]
        currMinProductSubarr = nums[0]
        maxProductAns = nums[0]
        for i in range(1, n):
            temp = currMaxProductSubarr
            currMaxProductSubarr = max(nums[i], max(currMaxProductSubarr * nums[i], currMinProductSubarr * nums[i]))
            currMinProductSubarr = min(nums[i], min(temp * nums[i], currMinProductSubarr * nums[i]))
            maxProductAns = max(maxProductAns, currMaxProductSubarr)
        return maxProductAns