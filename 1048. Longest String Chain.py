# Using Tabulation Method
# Time Complexity is O(n*n*n)
# Space Complexity is O(n)
class Solution:
    def is_predecessor(self, word1, word2):
        # Check if word2 is a predecessor of word1
        if len(word1) != 1 + len(word2):
            return False
        first = 0
        second = 0
        while first < len(word1):
            if second < len(word2) and word1[first] == word2[second]:
                first += 1
                second += 1
            else:
                first += 1
        return first == len(word1) and second == len(word2)
            
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key=len)
        dp = [1]*n
        maxi = 1
        for i in range(1, n):
            for prev_ind in range(i):
                if self.is_predecessor(words[i], words[prev_ind]) and 1 + dp[prev_ind] > dp[i]:
                    dp[i] = 1 + dp[prev_ind]
            if maxi < dp[i]:
                maxi = dp[i]
        return maxi 
        