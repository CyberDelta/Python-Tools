import os
clear = lambda: os.system('cls')

while(True):
	def error():
		print("Invalid input")
	def add(x, y):
		return x + y

	def subtract(x, y):
		return x - y

	def multiply(x, y):
		return x * y

	def divide(x, y):
		if y != 0:
			return x / y
		else:
			z = "NULL"
			return z

	print("Select operation:")
	print("")
	print("1.Add")
	print("2.Subtract")
	print("3.Multiply")
	print("4.Divide")
	print("5. Exit Program")
	print("")
	print("Enter your choice(1/2/3/4/5):")
	calc = input(">>")
	
	if calc == '5':
		exit()
	
	print("Enter first number: ")
	num1 = int(input(">>"))
		
	print("Enter second number: ")
	num2 = int(input(">>"))
		
	if calc == '1':
		print(num1,"+",num2,"=", add(num1,num2))

	elif calc == '2':
		print(num1,"-",num2,"=", subtract(num1,num2))

	elif calc == '3':
		print(num1,"*",num2,"=", multiply(num1,num2))

	elif calc == '4':
		print(num1,"/",num2,"=", divide(num1,num2))
	else:
		error()
	spinit = input("Press any key to continue...")
	clear()