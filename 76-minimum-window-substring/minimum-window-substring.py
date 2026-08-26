class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        left = 0
        count = 0
        start = 0
        min_len = float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] <= need[c]:
                count += 1

            while count == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                x = s[left]
                window[x] -= 1

                if x in need and window[x] < need[x]:
                    count -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]