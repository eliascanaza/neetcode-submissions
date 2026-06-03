class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        mS = []
        mT = []

        for i in range(len(s)):
            mS.append(s[i])
            mT.append(t[i])

        mS.sort()
        mT.sort()
        for i in range(len(mS)):
            if mS[i] != mT[i]:
                return False
        
        return True