"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = sum([len(nums1), len(nums2)])
        if total % 2 == 0:
            medium = total / 2
        else:
            medium = (total + 1) / 2

        result_nums1 = 0
        result_nums2 = 0
        result_medium = 0
        while result_medium < medium or result_nums1 < len(nums1) or result_nums2 < len(nums2):
            if nums1[result_nums1] < nums2[result_nums2]:
                if result_medium == medium:
                    return nums1[result_nums1]
                result_nums1 += 1
            else:
                if result_medium == medium:
                    return nums2[result_nums2]
                result_nums2 += 1
            result_medium += 1
