import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	d = {}
	for i in a:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
	ans = 0
	for i in range(n):
		s = a[i]
		for j in range(i+1,n):
			s += a[j]
			if s in d:
				ans += d[s]
				del d[s]
	print (ans)