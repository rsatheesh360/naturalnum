def sumall():
	n=int(input())
	l=[]
	sum=0
	for i in range(n):
		l.append(int(input()))
		sum+=l[i]
	print(sum)
try:
	sumall()
except:
	print('invalid')
  print(n)
