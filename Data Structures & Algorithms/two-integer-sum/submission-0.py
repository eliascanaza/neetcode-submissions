class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            if target - nums[i] in m:
                return [m.get(target - nums[i]), i]
            m[num] = i
        
        return [0,0]