class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = [[] for _ in range(numRows)]
        p = numRows if numRows == 1 else 2*numRows -2
        for i,c in enumerate(s):
            mod = i%p
            row = mod if mod<numRows else 2*numRows - mod - 2
            l[row].append(c)
        return (''.join(itertools.chain.from_iterable(l)))
        
"""		
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
P   A   H   N
A P L S I I G
Y   I   R



Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I


Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""