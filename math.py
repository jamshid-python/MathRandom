import random													  
while True:
	key = ["+", "-", "*", "/"]									  
	key_a = random.choice(key)
	number1 = random.randint(1, 501)							  
	number2 = random.randint(1, 100)							  
	if key_a == "+":											  
		que = int(input(f"{number1} + {number2} = "))		      
		if que == number1 + number2:                              
			print("True")										  
		else:													  
			print("False")										  
	if key_a == "-":											 
		que1 = int(input(f"{number1} - {number2} = "))			  
		if que1 == number1 - number2:							  
			print("True")										  
		else:													 
			print("False")		