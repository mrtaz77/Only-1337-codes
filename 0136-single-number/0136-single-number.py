class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for _ in nums:
            res ^= _
        return res
        