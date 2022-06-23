# MEDIUM
#
# Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram
# is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original
# letters exactly once.
#
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Example 2:
#
# Input: strs = [""]
# Output: [[""]]
# Example 3:
#
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
#
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            chars = [char for char in s]
            chars.sort()
            key = "".join(chars)
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)

        return list(groups.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(solution.groupAnagrams([""]))
    print(solution.groupAnagrams(["a"]))
