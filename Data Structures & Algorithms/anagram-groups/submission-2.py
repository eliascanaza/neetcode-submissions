class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            indexNum = 0
            sorted_s = "".join(sorted(s))
            m[sorted_s].append(s)
        print(m)
        return list(m.values())