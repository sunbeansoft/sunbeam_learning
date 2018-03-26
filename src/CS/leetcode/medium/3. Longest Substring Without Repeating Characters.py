"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.`
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        distinct = set()
        max_times = 0
        tmp_times = 0
        for c in s:
            if c in distinct:
                tmp_times = len(distinct)
                max_times = max(max_times, tmp_times)
                distinct = set()
                distinct.add(c)
            else:
                distinct.add(c)
                tmp_times = len(distinct)
        max_times = max(max_times, tmp_times)
        return max_times

    def lengthOfLongestSubstring_discuss(self, s):
        start = maxLength = 0
        usedChar = {}

        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength


print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution().lengthOfLongestSubstring("pwwkew")
print Solution().lengthOfLongestSubstring("bbbb")
print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution().lengthOfLongestSubstring("c")
print Solution().lengthOfLongestSubstring("dvdf")
