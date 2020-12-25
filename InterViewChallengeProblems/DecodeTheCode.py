from itertools import product
class Solution:
	def breakCode(self, digits):
		l = list()
		for i in (digits):
			if i = '2':
				l.append(['a','b', 'c'])
			elif i = '3':
				l.append(['d', 'e','f'])
			elif i= '4':
				l.append(['g','h','i'])
			elif i = '5':
				l.append(['j', 'k', 'l'])
			elif i= '6':
				l.append(['e', 'n','o'])
			elif i= '7':
				l.append(['p', 'q','r','s'])
			elif i= '':
				l.append(['t','u', 'v'])
			elif i= '9':
				l.append(['w','x', 'y','z'])
			else:
				pass
		12 = [' join(j) for j in product(l)]
		return 12

def main():
	combos = Solution().breakCode(input())
	for i in combos:
		print(i, end = ' ')

if __name__ =='__main__':
	main()
	
	
"""
Input : 23
output:
ad
ae
af
bd
be
bf
cd
ce
cf

here 2 has elements a,b,c and 3 has d,e,f in the same way as the mobile numbers in buttons mobile or dial box of calls
"""