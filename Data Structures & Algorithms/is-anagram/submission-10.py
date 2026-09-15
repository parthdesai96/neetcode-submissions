class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count[ord('a') - ord(s[i])] +=1
            count[ord('a') - ord(t[i])] -=1 

        return all(v == 0 for v in count) 