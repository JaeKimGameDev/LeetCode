#https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        firstNumCounter = -1
        firstNum = None
        secondNum = None
        for i in range(len(nums), 0, -1):
            firstNumCounter += 1
            firstNum = nums[firstNumCounter]
            secondNumCounter = firstNumCounter

            for k in range(1, i):
                secondNum = nums[firstNumCounter + k]

                if (target == firstNum + secondNum):
                    return firstNumCounter, firstNumCounter + k

        return