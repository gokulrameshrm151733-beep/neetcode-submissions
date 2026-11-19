from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        ft=sorted(count.keys(),key=count.get,reverse=True)
        return ft[:k]
        
