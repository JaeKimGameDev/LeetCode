class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        back = -1

        for i in range(len(xStr) // 2):
            print(xStr[0], xStr[back] )
            if xStr[i] != xStr[back]:
                return False
            back += -1
        return True


class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        y = xStr[::-1]

        if xStr == y:
            return True
        return False