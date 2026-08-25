class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
       
        low = 1
        high = max(nums)

        while low < high:
            mid = (low + high) // 2
            total = 0

            for x in nums:
                total += (x + mid - 1) // mid

            if total <= threshold:
                high = mid
            else:
                low = mid + 1

        return low