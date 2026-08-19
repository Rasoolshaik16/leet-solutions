class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
           x=1/x
           n=-n
        result=1
        result*=x**n
        return result            