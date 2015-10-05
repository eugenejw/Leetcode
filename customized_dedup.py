'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_seen = dict()
        for each in nums:
            if each in num_seen:
                if num_seen[each] == 2:
                    pass
                else:
                    num_seen[each] += 1
            else:
                num_seen[each] = 1
        #re-create the list
        new_lst = []
        for key in num_seen.keys():
            iter_num = num_seen[key]
            while iter_num >= 1:
                iter_num -= 1
                new_lst.append(key)

        return new_lst

s = Solution()
print s.removeDuplicates([1,1,1,2,2,3])
