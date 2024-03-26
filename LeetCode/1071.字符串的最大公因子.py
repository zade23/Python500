#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        t = math.gcd(len(str1), len(str2))
        if t > 0 and max(len(str1), len(str2)) % t == 0:
            return str1[:t] if str1 + str2 == str2 + str1 else ""
        return ""
# @lc code=end

