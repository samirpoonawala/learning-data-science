# (Treehouse) JavaScript Loops, Arrays and Objects

Storing, tracking and handling data is a large part of computer programming. Arrays provide a method for storing multiple values into a single variable. That makes an array a convenient way to pass around a list of items. In this course, you'll learn how to create arrays and use loops to access their contents. You'll also learn some advanced methods that make working with arrays easier.

what you'll learn:
* loops
* arrays
* objects
* DRY programming

## Simplifying repetitive tasks with loops
Loops are a way of repeating code - they're very handy for repetitive tasks. Loops are frequently used to cycle through an array and perform an action on each item in the array.

### Introducing loops, arrays and objects
Why you should learn these three important programming concepts

### What are loops?
Learn how to save time by using loops to run repetitive tasks

* structure of a while loop:
```javascript
while () {
	// this is the loop
}
```

* example: loop that runs 10 times:
```javascript
var counter = 1;
while ( counter <= 10 ) {
	console.log(counter);
	counter += 1;
}
```

### A closer look at loop conditions
How to use different test conditions to run and exit a loop. How to avoid endless loops.

Let's break this program down
1. Generate a random number from 1 to 10000. This is the number the computer needs to guess
2. Enter a while loop - inside this loop the computer will "guess" a random number. If the number the computer guesses matches the number generated at the beginning of the program, the loop ends, if not, the loop continues until the correct number is guessed
3. Exit the loop and print the random number and the number of times 

* condition is tested before the code is run

### `do... while` loops
Learn about another type of JavaScript loop.

Basic structure of a do... while Loop
```javascript
do {
	// code for loop goes here
	// it runs AT least one time
} while ( )
```
* unlike a while loop, a do while loop is always run at least once
	* condition is tested after the code is run

### For loops
Learn about the most common type of loop, the for loop.

Basic structure of a for loop:
```javascript
for (var i = 0; i < 10; i += 1) {
	// do something in here
}
```

You can also increment the counter using the ++ operator like this:

```javascript
for (var i = 0; i < 10; i++) {
	// do something in here
}
```

While loop vs. for loop:

```javascript
// while loop

var counter = 0;
while (counter < 10) {
	document.write ( counter );
	counter += 1;
}

for ( var counter = 0; counter < 10; counter += 1 ) {
	document.write( counter );
}
```

### Exiting loops
Learn how to exit loops using the break statement.

```javascript
while (true) {
	// this is an endless loop
	break;
	// but break, lets you "break out" of the loop
}
```

### The refactor challenge
Improve an existing JavaScript program by using loops and applying "DRY" programming principles
* "DRY" = "don't repeat yourself"

### The refactor challenge solution
See how the instructor solved the Refactor Challenge

### The refactor challenge, part 2
Keep refactoring that program! Make it more efficient and apply "DRY" programming principles
* functions allow you to create more modular, reusable code

## Tracking multiple items with arrays
Arrays provide a way to store multiple pieces of information in a single thing. An array is basically a list of values: numbers, strings, boolean values or even other arrays

### What is an array?
Learn about this common data structure for holding multiple pieces of information

Arrays:
```javascript
var scores = [100, 99, 72, 60];
var names = ['Joan', 'Amit', 'Sarah', 'Ricardo', 'Piers'];
var values = [1, -100, true, false, 'JavaScript']
```

### Accessing items in an array
How to use index values to access data at specific locations in an array

Chrome console keyboard shortcuts
* Windows: Ctrl + Shift + J
* Mac: Cmd + Option + J

### Adding data to arrays
Learn three common ways to add values to arrays

Add items to the end of an array with .push():

```javascript
var items = ['Hat', 'Ball', 'Shoes'];
items.push('Socks', 'Scarf')

// items is now ['Hat', 'Ball', 'Shoes', 'Socks', 'Scarf']
```

Add items to the beginning of an array with .unshift()

```javascript
var items = ['Hat', 'Ball', 'Shoes'];
items.unshift('Socks','Scarf');
// items is now ['Socks', 'Scarf', 'Hat', 'Ball', 'Shoes']
```

### Removing items from arrays
Learn how to remove values from the front and end of an array

Remove the first item from an array with .shift():
```javascript
var items = ['Hat', 'Ball', 'Shoes'];
var firstItem = items.shift();

// firstItem now holds 'Hat'
// and items is now ['Ball', 'Shoes']
```

Remove the last item from an array with .pop():
```javascript
var items = ['Hat', 'Ball', Shoes];
var lastItem = items.pop()
// lastItem now holds 'Shoes'
// and items is now ['Hat', 'Ball']

```

### Using for loops with arrays
Learn how to access items in an array by using for loops

```javascript
var students = ['Sascha', 'Lynn', 'Jennifer', 'Paul'];
for (var i = 0; i < students.length; i += 1){
	console.log(students[i])
}
```

### Useful array methods
Learn three of the nearly two dozen methods used to modify, search and combine arrays
* .indexOf()
* .join()

### Two-dimensional arrays
Learn how to create a spreadsheet-like data structure by storing arrays in arrays

### Build a quiz challenge, part 1
Use loops and an array to create a quiz application, that tracks the number of quiz questions answered correctly

### Build a quiz challenge, part 1 solution
Follow the instructor as he demonstrates one answer to the "build a quiz" challenge

### Build a quiz challenge, part 2
Improve on the quiz you built in the last challenge, by displaying a list of questions the player answered correctly and a list of questions the player got wrong.

### Build a quiz challenge, part 2 solution
Learn how the instructor improved on the quiz challenge.

## Tracking data using objects
Objects are a large part of JavaScript programming. In this lesson, we'll look at one part of JavaScript objects: using objects to store key / value pairs. Objects provide a flexible way to keep track of data by associating a name with a particular value. They're used all the time in JavaScript programming and, using a particular object format called JSON, they're used to transmit data between websites, databases and web pages.

### The object literal
Learn JavaScript object literal syntax for creating a variable that stores data as property / value pairs.

### Accessing object properties
Learn how to retrieve and set values in objects using property names using both bracket and dot notation.

### Using `for in` to loop through an object's properties
Learn how to access each property name and property value by looping through an object's keys

```javascript
var student = {
	name: "Dave",
	grades: [80, 85, 90, 95]
};
for ( var key in student ) {
	// do something
}
```
### Mixing and matching arrays and objects
Learn how to combine these two data-structures to create even more powerful ways to store and retrieve information

### JavaScript Object Notation
Learn how JavaScript objects are used to transfer information between browsers, servers, databases and other online services.
* commonly used with AJAX
* teamtreehouse.com/samirpoonawala.json

### The build an object challenge, part 1
Use your knowledge of JavaScript objects to create an array of student data. Each student's information is represented by an object

* Let's break this down into two steps
	* Each object should have the following properties
		* Name
		* Track
		* Achievements (should hold a number value)
		* Points
	* Create at least five student objects

### The build an object challenge, part 1, solution
The instructor shows you how to create a data structure using an array of objects.

### The build an object challenge, part 2
Create a program that runs through an array of student information and prints out data specific to each student

### The build an object challenge, part 2 solution
Learn how the instructor programmed a solution for this challenge

### The student record search challenge
Use your knowledge of arrays, objects and loops to create a program that searches a database of students for individual students

### The student record search challenge solution
Learn how the instructor implemented a program for searching student records