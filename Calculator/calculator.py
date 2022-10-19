#!C:/Users/evanj/AppData/Local/Programs/Python/Python310/python.exe

import math
import sys

"""def calculate(number1, number2, operator):
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

	return print(output)"""


print("Welcome! This is a new and improved calculator which can handle longer strings of input, with spaces between the elements.\nExample: 3 + 4 / 2 * 5 which would equal 13.")
operators = ['+', '-', '*', '/']

def new_func():
          print("Invalid input!")

while True:
	expression = input("Write an expression:\n>>> ")
	expression = expression.split()
	result = 0
	number = 0

	for element in expression:
		if element.isnumeric():
			number = float(element)
			continue
	print(result)
