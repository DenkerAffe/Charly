from commands import commands
from errors import CommandNotExistingException, MissingCharacterException, InvalidVariableNameException
from iposTypes import Integer, String, Commands, Item

variables = {
	"A" : String("abcdefghijklmnopqrstuvwxyz"),
	"D" : String("0123456789"),
	"E" : String(""),
	"S" : String(" "),
	"T" : Integer(2),
}

def handleIntegerLiteral(stack, code, index):
	"""
	Pushes the integer literal starting at the given index to the stack.
	Returns the index of the first character after the integer literal.
	"""
	x = index
	while code[x].isdigit():
		x += 1
		if x == len(code):
			break
	stack.append(Integer(int(code[index : x])))
	
	return x
	

def handleCharLiteral(stack, code, index):
	"""
	Pushes the character literal at the given index to the stack.
	Returns the index of the first character after the character literal
	"""
	if index + 1 < len(code):
		stack.append(String(code[index + 1]))
		index += 2
	else:
		raise MissingCharacterException(index + 1)
		
	return index
	

def handleStringLiteral(stack, code, index):
	"""
	Pushes the string literal starting at the given index to the stack.
	Returns the index of the first character in the code ofter the string literal.
	"""
	quoteIndex = code.find("\"", index + 1)
	if quoteIndex == -1:
		stack.append(String(code[index + 1 :]))
		index = len(code)
	else:
		stack.append(String(code[index + 1 : quoteIndex]))
		index = quoteIndex + 1
		
	return index
	

def handleSpace(code, index):
	"""
	Returns the index of the first non-whitespace character in the code
	starting at the given index
	"""
	while code[index].isspace():
		index += 1
		if index == len(code):
			break;
		
	return index
	
	
def handleVariable(stack, code, index):
	"""
	Pushes the value of the  the variable at the given index to the stack
	Returns the index of the next character in the code
	"""
	value = variables[code[index]]
	
	stack.append(value)
		
	return index + 1

	
def assignVariable(stack):
	from functions import popArguments
	modeList = [{
			"types" : [Item, String],
			"name" : "assignVariable"
		},
	]
	
	M, B, A = popArguments(stack, modeList, 2, unpack=False)
	
	# Assign the B to a variable named A and leaves the value of A on the stack
	if M == "assignVariable":
		if len(A.value) != 1:
			raise InvalidVariableNameException(A.value)
		else:
			variables[A.value] = B
			
			if isinstance(B, String):
				stack.append(String(B.value))
			elif isinstance(B, Integer):
				stack.append(Integer())
			elif isinstance(B.value, Commands):
				stack.append(Commands(B.value))

def handleCommand(stack, code, index):
	"""
	Executes the command at the given index in the code.
	Returns the index of the first character after the command
	"""
	if code[index] in commands:
		commands[code[index]](stack)
		index += 1
	else:
		raise CommandNotExistingException(index, code[index])
		
	return index

def joinStack(stack):
	"""Joins the stack into one string and return it. Skips Commands."""
	return "".join([str(e.value) for e in stack if not isinstance(e, Commands)])

def run(code, stack):
	""""
	Runs the code with the given stack
	The stack is modified in-place but also gets returned
	"""
	
	# loop through the code with i as index
	i = 0
	while i < len(code):
		# If current char is a digit, search the next non-digit char
		# and push all the digits between them to the stack as one integer literal
		if code[i].isdigit():
			i = handleIntegerLiteral(stack, code, i)
			
		# If the current char is a single quote we push the following
		# character to the stack as  a string literal
		elif code[i] == "'":
			i = handleCharLiteral(stack, code, i)
		
		# If the current char is a double quote, we search the ending one and push
		# the string between them to the stack. If there is no ending quote we take everything
		elif code[i] == "\"":
			i = handleStringLiteral(stack, code, i)
		
		# If current char is a space, find the next non-space char and point i on it
		elif code[i].isspace():
			i = handleSpace(code, i)
		
		# If current char is a variable, replace it with its value and set i to the next char		
		elif code[i] in variables:
			i = handleVariable(stack, code, i)
		
		# If the current char is equal sign, assign the 2nd top value to a variable given in the string at the top
		elif code[i] == "=":
			assignVariable(stack)
			i += 1
		
		# Current char is a command
		else:
			i = handleCommand(stack, code, i)
	
	return stack
