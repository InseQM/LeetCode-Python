
def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    res = list()
    if n < 2:
        return 0
    for i in range(2, n):
        if len(res) == 0:
            res.append(i)
            continue
        for v in res:
            if i % v == 0:
                break
        else:
            res.append(i)
    return len(res)


countPrimes(10)
