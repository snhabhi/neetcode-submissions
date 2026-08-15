class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 ={}
        for idx,num in enumerate(nums):
            diff = target - num
            if diff in dict1:
                return [dict1[diff],idx]
            
            dict1[num]=idx
         



       