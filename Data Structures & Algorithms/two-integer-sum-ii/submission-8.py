class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hi = len(numbers)-1
        lo = 0
        while lo<hi:
            if numbers[lo]+numbers[hi] < target:
                lo+=1
            if numbers[lo]+numbers[hi] > target:
                hi-=1
            if numbers[lo]+numbers[hi] == target:
                return [lo+1,hi+1]
        return [lo+1,hi+1]

