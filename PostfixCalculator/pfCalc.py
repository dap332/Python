#!/usr/bin/python
#Dhruv Patel
#
#


import sys


if(len(sys.argv) > 1):
	print "Too many arguments!"
	sys.exit()

f = sys.stdin
l = f.readline()


def parse(line):
	theList = line.strip('\n').split(" ")
	numberStack = []
	invalid = False
	for token in theList:
		try:
			numberStack.append(float(token))
		except ValueError:
			if ((len(numberStack)) < 2):
				invalid = True
			else:
				num2 = numberStack.pop()
				num1 = numberStack.pop()
				total = calculate(num1, num2, token)
				numberStack.append(total)
	
	if ( len(numberStack) > 1 ):
		invalid = True
	if (invalid ==  True):
		print "-E-"
	else:
		print numberStack.pop()


def calculate(operand1, operand2, operator):
	if operator == "+":
		return operand1 + operand2
	elif operator == "-":
		return operand1 - operand2
	elif operator == "*":
		return operand1 * operand2
	elif operator == "/":
		return operand1 / operand2
	elif operator == "^":
		return operand1 ** operand2
	else:
		return ("-E-")


while l:
   parse(l)
   l = f.readline()

