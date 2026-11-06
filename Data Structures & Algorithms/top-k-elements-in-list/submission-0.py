class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
        return [i[0] for i in sorted(hmap.items(), key=lambda item: item[1], reverse=True)[:k]]
                