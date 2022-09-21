#!/usr/bin/env python3

import math

function = input("Which math function do you want to use? \n >Square \n\n >>>")
number = input("Which number do you want to use? \n\n>>>")
output = 0

if function.lower() == "square":
	output = math.pow(int(number), 2)

print(output)
