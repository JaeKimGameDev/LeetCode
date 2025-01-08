class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sLen = len(s)
        num = roman[s[sLen-1]]

        for i in range(sLen-2, -1, -1):
            if (roman[s[i]] >= roman[s[i+1]]):
                num += roman[s[i]]
            else:
                num -= roman[s[i]]

        return num