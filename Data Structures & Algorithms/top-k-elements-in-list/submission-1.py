class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i]=0
            count[i]+=1
        
        sort = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

        res = list(sort.keys())[:k]
    
        return res
