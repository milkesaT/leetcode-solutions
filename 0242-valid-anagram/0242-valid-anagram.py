class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        count1 = {}
        for ch in t:
            if ch in count1:
                count1[ch] += 1
            else:
                count1[ch] = 1
        return count==count1
        