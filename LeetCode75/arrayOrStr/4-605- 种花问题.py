"""
605. 种花问题
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，
能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false 。


LeetCode: https://leetcode.cn/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
"""


def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    tmp = flowerbed[0]
    for i in flowerbed:
        if tmp == 0 and i == 0:
            tmp = 1
            n -= 1
            continue
        if tmp == 1 and i == 0:
            tmp = 0
            continue
        if tmp == 1 and i == 1:
            n += 1
            continue

    return n <= 0


print(canPlaceFlowers([1,0,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,1], 2))


