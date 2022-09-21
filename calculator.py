#!C:/Users/evanj/AppData/Local/Programs/Python/Python310/python.exe

import math
import sys

def calculation(number1, number2, operator):
	output = 0
	
	if operator.lower() == 'add':
		output = int(number1) + int(number2)

	if operator.lower() == 'subtract':
		output = int(number1) - int(number2)

	if operator.lower() == 'multiply':
		output = int(number1) * int(number2)

	if operator.lower() == 'divide':
		output = int(number1) / int(number2)

	if operator.lower() == 'power':
		output = int(number1) ** int(number2)

	return print(output)


print("Welcome! This is a simple calculator which operates on two numbers.")
function = ""
number1 = ""
number2 = ""
output = 0
operations = ['add', 'subtract', 'multiply', 'divide', 'power']

"""Checks if input is valid"""
while True:
	function = input("Which math function do you want to use? \n >{} \n\n >>>".format(operations))
	if function.lower() not in operations:
		print("Invalid input!")
		continue

	elif function.lower() in operations:
		break

while True:
	number1 = input("Which number do you want to use? \n\n>>>")
	number2 = input("WHich additional number do you want to use? \n\n>>>")
	if number1.isnumeric() == False or number2.isnumeric() == False:
		print("Invalid input!")
		continue
	
	if number1.isnumeric() == True and number2.isnumeric() == True:
		break

calculation(number1, number2, function)
