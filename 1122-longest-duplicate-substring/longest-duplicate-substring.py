class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        n = len(s)

        def check(k):
            seen = set()
            for i in range(n - k + 1):
                x = s[i:i+k]
                if x in seen:
                    return x
                seen.add(x)
            return ""

        l, r = 1, n - 1
        ans = ""

        while l <= r:
            m = (l + r) // 2
            x = check(m)

            if x:
                ans = x
                l = m + 1
            else:
                r = m - 1

        return ans