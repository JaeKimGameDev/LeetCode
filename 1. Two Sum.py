#https://leetcode.com/problems/two-sum/description/
class Solution:
    def twoSum(self, nums, target):
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

    def twoSumVer2(self, nums, target):
        d = {}
        for position, value in enumerate(nums):
            y = target - value
            if y in d:
                return [d[y], position]
            d[value] = position

nums = [2,7,11,15]
target = 9

myInstance = Solution()
result = myInstance.twoSumVer2(nums, target)
print(result)