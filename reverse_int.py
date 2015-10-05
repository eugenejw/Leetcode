'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp_x = abs(x)
        string_x = str(tmp_x)
        lst = []
        for each in string_x:
            lst.append(each)
        lst.reverse()
        new_string = ''.join(lst)
        new_int = int(new_string)
        if x < 0:
            new_int *= -1

        return new_int

s = Solution()
print s.reverse(-123)
print s.reverse(456)
        
        
        
