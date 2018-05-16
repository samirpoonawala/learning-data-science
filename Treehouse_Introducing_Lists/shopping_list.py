# Create a new list named shopping_list
shopping_list = []



def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items
Enter 'HELP' for this help
Enter 'SHOW' to see the current list
    """)

show_help()


def add_to_list(item):
    # add item to list
    shopping_list.append(item)
    # notify user that the item was added, and state the number of items in the list currently
    if len(shopping_list) == 1:
        print("Congratulations, you added your first item to the shopping list!")
    else:
        print("Added! List has {} items.".format(len(shopping_list)))

# define a function named show_list that prints all the items in the list
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

while True:
    new_item = input("> ")
    
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue # completes the current iteration
    elif new_item == "SHOW":
        show_list()
        continue

    # call add_to_list with a new item as an argument
    add_to_list(new_item)


show_list()