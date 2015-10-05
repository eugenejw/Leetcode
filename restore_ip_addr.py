'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''
class Solution(object):
	def restoreIpAddresses(self, s):

		def search(s, subset_count, ip):
			if subset_count == 4:
				if s == '':
					ips.append(ip[1:])
				return

			for i in range(1,4): #1,2,3
				if i <= len(s):
					if int(s[:i]) <= 255:
						search(s[i:], subset_count+1, ip+'.'+s[:i])
					if s[0] == '0':
						break
		ips = []
		search(s, 0, '')
		return ips
		

s = Solution()
print s.restoreIpAddresses("25525511135")
