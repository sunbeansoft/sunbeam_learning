"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, total = 0, len(height) - 1, 0
        while l < r:
            w = l - r
            total = max(min(height[l], height[r]) * w, total)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return total

    def maxArea_discuss(self, height):
        maxarea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea
