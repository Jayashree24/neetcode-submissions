class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        zeroes = nums.count(0)
        if zeroes >= 2:
            out = [0] * len(nums)
            return out

        p = zero_p = 1
        for n in nums:
            p *= n
            if n == 0:
                continue
            zero_p *= n

        for n in nums:
            if n == 0:
                out.append(zero_p)
                continue
            out.append(int(p/n))

        return out

        