class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            old_max = current_max

            current_max = max(
                num,
                num * current_max,
                num * current_min
            )

            current_min = min(
                num,
                num * old_max,
                num * current_min
            )

            result = max(result, current_max)

        return result 