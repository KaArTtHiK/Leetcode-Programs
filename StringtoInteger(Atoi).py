class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0 or (len(s) > 0 and not (s[0] in ['+','-'] or s[0].isdigit())):
            return 0

        value = 0
        sign = -1 if s[0] == '-' else 1
        i = 1 if not s[0].isdigit() else 0

        while i < len(s) and s[i].isdigit():
            value = (value * 10) + (ord(s[i]) - ord('0'))
            i += 1
        value *= sign

        if value < -(2**31):
            return -(2**31)
        elif value > (2**31)-1:
            return (2**31)-1

        return value 
        
       
	   
"""Example 1:

Input: str = "42"
Output: 42
Example 2:

Input: str = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: str = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: str = "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.
"""