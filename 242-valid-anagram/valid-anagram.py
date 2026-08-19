class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        if len(s)!=len(t):
            return False
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            freq[ch]=freq.get(ch,0)-1
        for ch in freq:
            if freq[ch]!=0:
                return False
        return True
        