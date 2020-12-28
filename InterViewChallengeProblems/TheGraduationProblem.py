from itertools import product
def Solve (N):
    # Write your code here
  l = list()
  l2 = list()
  l3 = list()
  for i in product(["A","P"],repeat = N):
    for j in range(1,N):
      if i[j] == i[j-1] and i[j] == "A":
        break
    else:
      l.append(i)
  Total_count = len(l)
  for i in l:
    if i[-1] == "A":
      l2.append(i)
  p_count = len(l2)
  a = "{}/{}".format(p_count,Total_count)
  l3.append(Total_count)
  l3.append(a)
  return l3# Dummy return
    

N = int(input())

out_ = Solve(N)
for i_out_ in out_:
    print (i_out_)
	
	
	
"""
The graduation problem:

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. You are not allowed to miss classes for two or more consecutive days. 
For example, if you miss a class today, then you must attend it tomorrow. Your graduation ceremony is on the last day of the academic year that is the Nth day.
Your task is to determine the following:
• The number of ways to attend classes over N days.
• The probability that you will miss your graduation ceremony.

Note:

Probability = (No. of ways of being absent at the ceremony) / (Total no. of ways to attend classes over N days)
• You do not have to reduce the fraction. For example, if prob=10/20, then the output should be 10/20 and not 1/2.
Input format
• The first and the only line of input contains an integer N denoting the number of days.
Output format
You are required to print the following in a new line:
• The number of ways to attend classes over N days.
• The probability that you will miss your graduation ceremony.

Input :
3

Output :
5  
2/5

Explanation:

Let's call the day she's absent as A. And the day she's present as P
Then all possible attendance combinations for n=3 days will be -
AAA, AAP, APA, APP, PAA, PAP, PPA, and PPP -> Now in combinations AAA, AAP, and PAA, she's absent for more than or equal to two consecutive days.
Thus, we'll reject these.

Required Combinations: APA, APP, PAP, PPA, and PPP -> 5 ways Print 5
Now, in 2 combinations (APA & PPA) from 5 possible combinations, she'll not be able to attend the ceremony
Thus, print Probability as 2/5
"""