from typing import List

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def sum(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        pref = [0]
        for x in nums:
            pref.append(pref[-1] + (1 if x == target else -1))

        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        fw = Fenwick(len(vals))
        ans = 0

        for p in pref:
            r = rank[p]
            ans += fw.sum(r - 1)
            fw.add(r, 1)

        return ans
        