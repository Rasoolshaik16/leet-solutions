class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        nums.sort()

        n = len(nums)
        mid = (n + 1) // 2

        small = nums[:mid]
        large = nums[mid:]

        i = len(small) - 1
        j = len(large) - 1
        k = 0

        while i >= 0:
            nums[k] = small[i]
            k += 2
            i -= 1

        k = 1

        while j >= 0:
            nums[k] = large[j]
            k += 2
            j -= 1