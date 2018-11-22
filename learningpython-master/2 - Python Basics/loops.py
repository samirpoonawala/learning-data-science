# Example file for working with loops

def main():
	x = 0

	# define a while loop
#	while (x<5):
#		print(x)
#		x = x+1

# use a for loop over a collection
#	for x in range(5,10):
#		print(x)

#	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#	for day in days:
#		print(day)

# use the break and continue statements
#	for x in range(5, 10):
#		#if (x==7): break
#		if (x % 2 == 0): continue
#		print(x)

# using the enumerate() function to get index
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	for i, day in enumerate(days):
		print(i+1, day)


if __name__ == "__main__":
	main()