def fib(n):
	if n<=1:
		return 1
	else:
		return (fib(n-1)+fib(n-2))
a=int(input("how many terms"))
if a<=0:
	print("please enter the positive number")
else:
	print("enter the number")
	for  i in range (a):
	   print(fib(a))
