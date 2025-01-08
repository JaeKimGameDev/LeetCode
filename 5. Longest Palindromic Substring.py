class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLength = 0
        if len(s) < 2:
            return s[0]
        palindromic = s[0]
        for start in range(len(s)):
            for restOfLetters in range(start+1, len(s)+1):
                forwards = s[start:restOfLetters]
                backwards = forwards[::-1]
                #print("forward =", forwards, "  s[start:restOfLetters] = [", start, ":", restOfLetters, "]")
                if (forwards == backwards and maxLength < len(s[start:restOfLetters])):
                    palindromic = s[start:restOfLetters]
                    maxLength = len(palindromic)
        return palindromic
