# Example file for Variables

# Declare a variable and initialize it
f = 0
print(f)

# Re-declaring the variable works
f = "abc"
print(f)


# ERROR: variables of different types cannot be combined
	#print("This is a string" + 123)
		#TypeError: cannot concatenate 'str' and 'int' objects
	#this however will work:
print("This is a string " + str(123))

# Global vs. local variables in functions
def someFunction():
	global f # makes f a global variable; affects f outside the function
	f = "def"
	print(f)

someFunction()
print(f)