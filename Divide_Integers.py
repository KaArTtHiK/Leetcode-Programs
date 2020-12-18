class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = 2**31
        b = -a
        
        if dividend/divisor< 0:
            if dividend/divisor >= b:
                return -(abs(dividend)//abs(divisor))
            else:
                return b+1
        else:
            if dividend/divisor<a:
                return dividend//divisor
            else:
                return a-1


"""Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
"""