# MEDIUM
#
# You are given a string s. A split is called good if you can split s into two non-empty strings sleft and sright where
# their concatenation is equal to s (i.e., sleft + sright = s) and the number of distinct letters in sleft and sright
# is the same. Return the number of good splits you can make in s.
#
# Example 1:
#
# Input: s = "aacaba"
# Output: 2
# Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
# ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
# ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
# ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
# ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
#
# Example 2:
#
# Input: s = "abcd"
# Output: 1
# Explanation: Split the string as follows ("ab", "cd").
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.

from collections import Counter


class Solution:
    def numSplits_naive(self, s: str) -> int:
        s_chars = [char for char in s]
        count = 0

        for idx in range(1, len(s_chars)):
            s_l = s_chars[:idx]
            s_r = s_chars[idx:]

            if len(set(s_l)) == len(set(s_r)):
                count += 1

        return count

    def numSplits(self, s: str) -> int:
        count = 0
        s_l = Counter()
        s_r = Counter(s)

        for i in range(1, len(s)):
            s_r[s[i - 1]] -= 1
            if s_r[s[i - 1]] == 0:
                del s_r[s[i - 1]]

            s_l[s[i - 1]] += 1
            if s_l[s[i - 1]] == 0:
                del s_l[s[i - 1]]

            if len(s_l) == len(s_r):
                count += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.numSplits("aaaaa"))  # 4
    print(solution.numSplits("aacaba"))  # 2
    print(solution.numSplits("abcd"))  # 1
