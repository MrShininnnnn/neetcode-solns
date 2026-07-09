class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seens = set()
        for n in nums:
            if n in seens:
                return True
            seens.add(n)
        return False
