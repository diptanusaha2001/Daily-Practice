class Solution(object):
    def trailingZeroes(self, n):
        if(n < 0):
            return -1
        output = 0
        while(n >= 5):
            n //= 5
            output += n
        return output
