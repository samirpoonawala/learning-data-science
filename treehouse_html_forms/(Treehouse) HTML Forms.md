# (Treehouse) HTML Forms

The web is a two-way communication medium. There's lot of HTML elements for displaying data and producing output, and conversely, there's also lots of HTML elements for accepting input. Accepting input from the user means creating web forms. In this course, we'll learn about all the most important form elements that web professionals use on a daily basis

What you'll learn:
* forms
* input elements
* select menus
* radio buttons
* checkboxes

## Form Basics
To learn about forms, we're going to create a simple sign up form for an imaginary web app. Our form won't actually submit anywhere, since that requires additional server-side code. However, we'll learn about all the most important HTML form elements.

### Overview of forms
Accepting input from the user means creating a web form, which is typically composed of form controls like text fields, radio buttons. checkboxes, select menus and more.

https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms

### The form element
The first element we'll learn about is the form element. This special element wraps all the other elements that go inside of our form.

HTML elements:
* `<form>`: the form element wraps a section of the document that contains form controls. The action attribute specifies the web address of a program that processes the information submitted via the form. The method attribute specifies the HTTP method that the browser should use to submit the form, such as POST or GET. Forms cannot be nested inside one another.

### The input element
The input element is the most commonly used form element. We can use the input element to make text fields, and much more.

HTML elements:
* `<input>`: the input element is used to create many different types of form controls. The type attribute specifies what kind of form control should be rendered, such as text, email, passwords, and more. The name attribute is submitted with form data so that server-side code can . parse the information

### The Textarea element
Sometimes a single line of text isn't enough and a simple input element won't work. For example, maybe you have a contact form and you need a place for people to type a message. In those cases, it's best to use a textarea.

HTML elements
* `<textarea>`: the textarea element accepts multiple lines of text from the user. Most browsers will render the textarea element with a widget to allow for resizing the editing area

### The button element
A form is not complete without a submit button. Once a user has finished filling out a form, they should be able to click a button that sends their data to the web server

HTML elements
* `<button>`: just as the name implies, the button element will render a clickable button. The type attribute specifies whether the button should submit the form data, reset the form, or have no default behavior for use with JavaScript

## Organizing forms
A form can be created with just a form element and some controls, but it's helpful to the user if the form is organized with labels and fieldset elements.

### The label element
Right now, it's impossible for the user to tell what kind of information they should type into each form field. We can label form controls using the label element.

HTML elements
* `<label>`: the label element helps to organize forms by assigning some helpful text to a form control. We can label form controls using the label element

### Fieldsets and legends
Sometimes, certain form controls belong together in a logical grouping. Form controls can be grouped together using fieldsets and then labeled using a legend.

HTML elements
* `<fieldset>`: the fieldset element wraps multiple form elements into common groups. This can help organize a form and make it easier to understand for users
* `<legend>`: the legend element is similar to the label element, but instead of labeling a form control, it labels a fieldset. Adding a legend to a fieldset can provide some helpful context for users that are filling out a form

## Choosing options
Sometimes when creating a form, it's better for the user to choose from predefined options rather than typing in text. This can be accomplished with select menus, radio buttons, and checkboxes.

### Select menus
A text input isn't ideal for every situation. The select element can be used in cases where the user should pick from a set of predefined options.

HTML elements:
* `<select>`: the select element renders a drop-down menu that contains selectable options. This type of form control is ideal for scenarios where the menu must choose one option for a preset list of 5 or more choices
* `<option>`: the option element represents one of the choices that a user can choose in a select menu. It should always be nested inside of a select element
* `<optgroup>`: the optgroup element wraps one or more option elements and helps to create logical groups. The label attribute specifies the text that the optgroup should display above the nested options

### Radio buttons
If the user only needs to choose from 5 or fewer options, then it's better to use radio buttons instead of a select menu

* Remember that in order to group radio buttons together, they must all share the same value for the name attribute

### Checkboxes
Sometimes there might be a group of predefined options where the user can select multiple items. That's where checkboxes are a better choice than radio buttons or select menus

### Going further
We've learned about lots of HTML form elements, but what if you want to learn more? Here's a few challenges for you

