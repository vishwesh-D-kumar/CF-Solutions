for nt in range(int(input())):
	s = input()
	ans = s[0]
	for i in range(1,len(s),2):
		ans+=s[i]
	print (ans)