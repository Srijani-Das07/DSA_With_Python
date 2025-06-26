class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        length = 0
        power = 1
        for ch in reversed(s):        
            if ch == '0':
                length += 1           
            elif power <= k:          
                length += 1
                k      -= power      
            
            power <<= 1
           
        return length