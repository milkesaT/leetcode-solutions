class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        b=sorted(heights)
        count=0
        for i in range(len(b)):
            if b[i]!=heights[i]:
               count+=1

            
        return count