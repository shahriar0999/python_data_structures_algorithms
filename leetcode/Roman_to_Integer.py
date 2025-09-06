# https://leetcode.com/problems/roman-to-integer/description/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ans = 0
        for i in range(len(s)):
            if i + 1 < len(s) and sym_val[s[i]] > sym_val[s[i+1]]:
                ans += sym_val[s[i]]
            elif i + 1 < len(s) and sym_val[s[i]] < sym_val[s[i+1]]:
                ans -= sym_val[s[i]]
            elif i + 1 < len(s) and sym_val[s[i]] == sym_val[s[i+1]]:
                ans += sym_val[s[i]]
            else:
                ans += sym_val[s[-1]]

        return ans
    