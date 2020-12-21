s = input()
l1 = []
for i in range(len(s)):
    for j in range(len(s)):
        if i == j:
            l1.append(s[i])
        elif j<i:
            pass
        else:
            s1 = s[i:j+1]
            res = s1 == s1[::-1]
            if res == True:
                l1.append(s1)
            else:
                pass

                    
l1.sort(key = len)
print(l1[-1])


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