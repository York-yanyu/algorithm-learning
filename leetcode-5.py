# -*- coding: UTF-8 -*-
#最长回文子串
#leetcode-5
#难度：中等
#动态规划做法 dp[i][j]判断的是从i到j是否是回文子串

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return None
        l=len(s)
        if l==1:
            return s
        dp=[[0]*l for i in range(l)]
        left=0
        right=0
        lt=0
        for i in range(l):
            for j in range(0,i):
                dp[j][i]=(s[i]==s[j] and (i-j<2 or dp[j+1][i-1]))#这步是关键，比如要判断s[1]==s[5],那么还要判断是否相邻，相邻的话肯定是，不相邻的话就要判断2到4是否是回文的，这在之前已经判断好了
                if dp[j][i] and lt<i-j+1:#用来判断是否最长，并且记录最长是从哪儿到哪儿
                    lt=i-j+1
                    left=j
                    right=i
            dp[i][i]=1
        return s[left:right+1]
a=Solution()
b='adingidigni'
c=a.longestPalindrome(b)
print c