class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter


        frequency = Counter(s)

        chars = sorted(frequency, key=frequency.get, reverse=True)

        result = ""

        for ch in chars:
            result += ch * frequency[ch]

        return result