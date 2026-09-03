class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, freq in count.items():
            buckets[freq].append(n)

        ans = []

        for freq in range(len(nums), 0, -1):
            for n in buckets[freq]:
                ans.append(n)
                if len(ans) == k:
                    return ans    