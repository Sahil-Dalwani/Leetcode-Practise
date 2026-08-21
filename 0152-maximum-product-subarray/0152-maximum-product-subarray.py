class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = minp = ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                maxp, minp = minp, maxp

            maxp = max(num, num * maxp)
            minp = min(num, num * minp)

            ans = max(ans, maxp)

        return ans