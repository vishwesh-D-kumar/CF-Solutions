import sys
input = sys.stdin.readline
for nt in range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	if a.count(a[0])==n:
		print (n)
	else:
		print (1)
