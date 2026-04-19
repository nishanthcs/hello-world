class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i,n in enumerate(nums):
            if n in sum_dict:
                return [sum_dict[n],i]
            else:
                sum_dict[target-n] = i
        
        
        