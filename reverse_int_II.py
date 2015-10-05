class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)
        
        new_int = 0
        while x > 0:
            new_int = new_int*10 + x%10
            x = x / 10

        return new_int * sign

s = Solution()
print s.reverse(-123)
