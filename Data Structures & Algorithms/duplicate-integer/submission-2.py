class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_set=set()
        for i in nums:
            if i in map_set:
                return True
            map_set.add(i)
        return False
        