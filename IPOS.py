import sys
import argparse
from commands import commands
from errors import CommandNotExistingException, MissingCharacterException, IposException

def run(code, stack):
	# loop through the code with i as index
	i = 0
	while i < len(code):
		# If current char is a digit, search the next non-digit char
		# and push all the digits between to the stack as one integer literal
		if code[i].isdigit():
			x = i
			while code[x].isdigit():
				x += 1
				if x == len(code):
					break
			stack.append(int(code[i : x]))
			# set i on the non-digit char for the next iteration
			i = x
			
		# If the current char is a single quote we push the following
		# character to the stack as  a string literal
		elif code[i] == "'":
			if i + 1 < len(code):
				stack.append(code[i + 1])
				i += 2
			else:
				raise MissingCharacterException(i + 1)
		
		# If the current char is a double quote, we search the ending one and push
		# the string between them to the stack. If there is no ending quote we take everything
		elif code[i] == "\"":
			index = code.find("\"", i+1)
			if index == -1:
				stack.append(code[i+1 :])
				i = len(code)
			else:
				stack.append(code[i+1 : index])
				i = index + 1
		
		# Current char is a command
		else:
			if code[i] in commands:
				commands[code[i]](stack)
				i += 1
			else:
				raise CommandNotExistingException(i, code[i])
	
	return "".join([str(e) for e in stack])


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description="A golfing language made for string processing.")
	parser.add_argument("code", help="The code that shall be executed.")
	parser.add_argument("-i", "--input", help="The input string which is initially placed on the stack.")
	args = parser.parse_args()
	
	if args.input:
		stack = [args.input]
	else:
		stack = []
	
	try:
		print(run(args.code, stack))
	except IposException as e:
		print(e.message)
