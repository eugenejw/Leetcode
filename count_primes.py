"""
Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.

Hint:

Let's start with a isPrime function. To determine if a number is prime, we need to check if it is not divisible by any number less than n. The runtime complexity of isPrime function would be O(n) and hence counting the total prime numbers up to n would be O(n2). Could we do better?
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        counter = 0
        prime_lst = []
        for x in xrange(2,n):
            if self.isPrime(x):
                counter += 1
                prime_lst.append(x)

        print "Count: {}".format(counter)
        print "Count: {}".format(len(prime_lst))
        print "Prime List: {}".format(prime_lst)
        return counter

    def isPrime(self, num):
        found = False
        if num == 2:
            return True
        tmp_num = num/2
        while tmp_num > 1 and found == False:
            if num % tmp_num != 0:
                tmp_num -= 1
            else:
                print "num: {0} divided by {1}".format(num, tmp_num)
                return False
        return True
            
        
s = Solution()
s.countPrimes(100000)
