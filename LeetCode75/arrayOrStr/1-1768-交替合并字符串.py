""" 1768. 交替合并字符串
给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。
如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。返回 合并后的字符串 。

LeetCode:https://leetcode.cn/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
"""
def mergeAlternately(word1: str, word2: str) -> str:
    result = list()
    for i in range(0, max(len(word1), len(word2))):
        if len(word1) == i:
            result.append(word2[i:])
            break
        if len(word2) == i:
            result.append(word1[i:])
            break
        result.append(word1[i])
        result.append(word2[i])
    return "".join(result)
