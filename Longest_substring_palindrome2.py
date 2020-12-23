def pa(s):
    m = ''
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            if len(m)>j-i:
                break
            elif s[i:j]==s[i:j][::-1]:
                m = s[i:j]
    return m
s = 'babad'
l =pa(s)
print(l)
                


"""
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

"""