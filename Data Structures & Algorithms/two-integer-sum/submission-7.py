class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum1 = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in sum1:
                return [sum1[diff],i]
            sum1[n]=i
        return 

            


            