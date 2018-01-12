def collatz(number):
	if number%2==0:
		print(number//2)
		return number//2
	elif number%2!=0:
		print(3*number+1)
		return 3*number+1

#for i in range(1,7):
	#collatz(number=int(input()))

try:
	for i in range(1,7):
		collatz(number=int(input()))
except ValueError:
	for i in range(1,7):
		collatz(number=int(input('必须输入一个整数\n')))
