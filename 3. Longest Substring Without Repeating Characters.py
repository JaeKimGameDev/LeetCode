def NoDuplicates(start, end, theArray, compare):
    for leftSide in range(start, end):
        if (theArray[leftSide] == theArray[compare]):
            return False
    return True

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, middle, end = 0, 0, 0
        currentCounter, longestCounter = 0, 0

        #iterate through whole string (start to end)
        for start in range(len(s)):
            if (longestCounter < currentCounter):
                longestCounter = currentCounter
            currentCounter = 1
            middle = start + 1

            #iterate through all right side (middle to end)
            for rightSide in range(start+1, len(s)):

                #iterates through left side to compare (start to middle)
                check = NoDuplicates(start, middle, s, rightSide)
                if (check == True):
                    middle += 1
                    currentCounter += 1
                else:
                    break

        if longestCounter < currentCounter:
            longestCounter = currentCounter


        return longestCounter