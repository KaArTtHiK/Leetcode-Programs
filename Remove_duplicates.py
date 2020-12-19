class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)
		
"""Your input
[1,1,2]
Output
[1,2]
Expected
[1,2]
"""