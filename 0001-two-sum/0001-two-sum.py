class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    val = {}
    for i , n in enumerate(nums):
        diff = target-n
        if diff in val:
            return [val[diff],i]
        val[n]=i