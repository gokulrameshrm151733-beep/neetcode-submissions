class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for chi in strs:
            aq=" ".join(sorted(chi))
            d[aq].append(chi)
        return list(d.values())    
        