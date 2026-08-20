class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [0] * n

        left = 0
        right = n - 1
        position = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                answer[position] = nums[left] * nums[left]
                left += 1
            else:
                answer[position] = nums[right] * nums[right]
                right -= 1

            position -= 1

        return answer