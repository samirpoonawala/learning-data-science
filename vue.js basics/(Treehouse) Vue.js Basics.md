# (Treehouse) Vue.js Basics
Vue.js is a front end JavaScript framework with a gentle learning curve. Vue's lower barrier to entry, ease of use and fantastic documentation make it a fun and accessible technology. In this course, you'll learn fundamental concepts that will help you get up and running with Vue. You'll also gain skills and foundational knowledge that will help prepare you to tackle the complexities of other frameworks.

What you'll learn:
* What is a front-end framework
* Templating and data binding
* Methods and directives
* Event handling
* Simple animation

## (1) Introducing Vue
In this stage, we'll build an understanding of JavaScript frameworks -- what they are, when to use them, and why Vue.js is a great choice. You'll learn how to add Vue to a project using a CDN and get familiar with the basic Vue syntax.

### Introducing Vue
Get to know Vue.js, a front end JavaScript framework that's easy to learn and fun to work with

### Frameworks, Vue and you
What's a JavaScript framework, and how does using one help you as a developer

### Add Vue to a project
Learn the different ways you can add Vue.js in a coding project

### Hello Vue
Learn how to set up a basic Vue application

* **Vue instance**
	* The root of a Vue application, created by using the new keyword. You pass the Vue instance an object containing options that give you the ability to store data and define methods (more about methods in a later video!). The data and methods you define are then used in a Vue template to control the behavior of your application
* **Templating**
	* a Vue template generally consists of HTML, data bindings and Vue directives (more about Vue directives in a later video!). This is where you lay out the rules of how Vue should display your data. In our example, we've built a template that creates two data bindings: a title and a message
* **Data binding**
	* data binding generally means establishing a connection between an application's data and the application's user interface. In the video we created a connection between the title and message data properties to the Vue template. Vue will make sure that this data is always in sync with the user interface. If title or message change, Vue will detect the change and updates the browser without any extra legwork from us

## (2) What a Beautiful Vue
Explore the power of templating with Vue, including event handling, conditional rendering, and using Vue directives.

### Marvelous Mustaches
Learn a few things you can do with templating and data binding, including using JavaScript right in your Vue templates

### Introducing Vue Directives
Learn about Vue directives -- special instructions just for Vue that help you control how your templates should display or behave.

* **Vue directive**: a special attribute that you add to an HTML element in a Vue template. These are like special instructions just for Vue -- used to define certain behaviors such as when a method should be called in response to an event, or when to show / not show pieces of a UI element
* **Vue directive syntax**: vue directives start with v-
	* For example: v-text, v-html, v-bind

### Basic event handling
Learn about the Vue directive v-on, and how to use it in conjunction with Vue methods to respond to user events, such as button clicks.
* **v-on**: a Vue directive used for event handling. Accepts events as arguments, such as:
	* click
	* dblclick
	* keypress
	* keydown
	* keyup
	* mouseover
	* submit

### Add interactivity with v-show and v-on
Learn how to show or hide part of your template based on certain conditions

## (3) Sweeping Vues: Loops, methods and directives
Use Vue to loop through multiple items in an array. Learn more about Vue directives, including how to use computed properties and how to bind classes and styles to a template
* v-show hides or shows an HTML element based on the value it is passed. When passed a "true" or truthy value, the element will show. When passed a "false" or falsey value, the element will be hidden

### Vue Devtools
Vue Devtools, available in popular browsers like Chrome and Firefox, is a powerful debugging tool that can help demystify the structure of Vue applications

### List rendering with v-for
Learn how to loop through a data structure and keep code DRY using Vue's v-for directive

### Getting loopier
Use v-for to loop through an array of objects and add Vue directives to provide interactivity to each and every item in the array

### v-show vs. v-if
In this video we'll explore the differences between v-show and v-if

### Events: Toggling and filtering
Use the event object in Vue to filter a list of items by type

### Computed properties
Computed properties are a feature of Vue that help us perform more complex calculations or operations that affect the way our data is displayed

### Conditionally adding or removing classes
In this video, we'll add flair and detail to the accordion menu by using v-bind to conditionally add or remove CSS classes from our Vue template

## (4) Building a flashcard app
Apply what you've learned about Vue so far to build a fun and interactive flashcard app! Learn about more Vue directives, such as v-model

### Displaying and flipping cards
Let's outline how to accomplish this project, and review how to loop through and display data

### Getting user input
Use v-model to get user input from a form
* In this video we use v-model to gather data from a text input field, but v-model can be used to get input from other form input fields such as textarea, checkbox, radio buttons and more

### Creating a new card
Use v-model and v-bind together to collect and display information gathered from an HTML form

### Deleting a card
In this video, we'll write JavaScript inside of a Vue directive to add functionality that deletes a card

### Flip transition!
Get a crash course in using Vue's transition component to animate the flashcard app

### Error handling and enhancements
We're almost done! Let's add some polish and do a bit of refactoring.

### Going further with Vue
Excellent work completing Vue.js Basics! What