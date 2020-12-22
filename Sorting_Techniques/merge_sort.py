l = [1,4,5,6,7,2,3,4]
def merge(l):
	if(len(l)>1:
		m = len(l)//2
		le = l[:m]
		ri = l[m:]
		merge(le)
		merge(ri)
		i = j = k = 0
		while(i<len(le) and j<len(ri)):
			if le[i] < ri[j]:
				l[k] = le[i]
				i = i+1
			else:
				l[k] = ri[j]
				j = j+1
			k = k+1
		while(i<len(le)):
			l[k] = le[i]
			k = k+1
			i = i+1
		while(j<len(ri)):
			l[k] = ri[j]
			k = k+1
			j = j+1
merge(l)
print(*l)