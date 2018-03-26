"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        label = 1
        if x < 0:
            x *= -1
            label = -1
        result = 0
        while x >= 1:
            tmp_result = x % 10
            result = result * 10 + tmp_result
            x = x / 10

        return result * label


print Solution().reverse(123)
