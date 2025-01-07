class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        nums3Length = len(nums3)
        remainder = nums3Length % 2
        if (remainder != 1):
            middleLeft = nums3Length // 2-1
            return (nums3[middleLeft] + nums3[middleLeft+1])/2

        return nums3[nums3Length//2]