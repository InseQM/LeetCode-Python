"""
1071. 字符串的最大公因子

对于字符串 s 和 t，只有在 s = t + ... + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。
给定两个字符串 str1 和 str2 。返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2 。

LeetCode: https://leetcode.cn/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
"""

# 最大公因子长度 均能被str1、str2长度整除, 即可枚举取长度合适的字符串, 补齐判断是否相等

def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    for i in range(min(len(str1), len(str2)), 0, -1):
        if len(str1) % i == 0 and len(str2) % i == 0:
            if str1[:i] * (len(str1) // i) == str1 and str1[:i] * (len(str2) // i) == str2:
                return str1[:i]
    return ""

# 因为abc 是str1和str2 的最大公因子; 即可 str1 + str2 == n(abc) == str2 + str1 有解; 如有解, 则能被str1、str2长度整除的最大长度为结果
def gcdOfStrings2(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    for i in range(min(len(str1), len(str2)), 0, -1):
        if len(str1) % i == 0 and len(str2) % i == 0:
            return str1[:i]