class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # HashMap => Value : Key

        for index, num in enumerate(nums): #enumerate => index, value
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[num] = index
        return
