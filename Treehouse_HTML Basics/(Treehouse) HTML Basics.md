# (Treehouse) HTML Basics
[link](https://teamtreehouse.com/library/html-basics-2)
Learn HTML (HyperText Markup Language), the language common to every website. HTML describes the basic structure and content of a web page. If you want to build a website or web application, you'll need to know HTML.

What you'll learn:
* semantic markup
* formatting page content
* understanding file paths
* displaying images
* inline vs. block level elements

## Getting started with HTML
HTML is a markup language the browser uses to present content to users, like text, links, images and more. It's a basic component from which all websites and applications on the web are built.

### What is HTML?
HTML is understood by all browsers, from browsers on phones, to tablets to desktop computers. That's why every website and web app you use is made using HTML - it's the language of the web
* markup language

### Global structure of an HTML document
Even though most web pages look different from one another, every web page follows a common HTML structure

### Headings and paragraphs
The most common HTML elements used to structure and organize content are headings and paragraphs

### Creating lists
Lists are an important component of web design and front end web development. Just about every website or application on the web uses lists to display navigation links, shopping cart items, movie listings and more

* `<ul>`:  unordered list
* `<ol>`:  ordered list
* `<dl>`:  description list

### Creating links
Lists are the single most important unifying component of the web. Links let you jump from page to page, adn website to website, to find the information you're looking for

## Structuring your content
Learn to write semantic HTML and use elements that describe sections of content

### Semantic HTML: header, footer and section
HTML's role in web design and development is to provide structure and meaning to content. In this video, you'll begin learning HTML's set of elements that describe sections of content

* **semantic HTML**: markup that describes the meaning of content instead of how it looks

```
<section>
  <h2>About this Site</h2>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse vehicula metus in bibendum laoreet. Aenean libero est, egestas eu eros pretium, sodales iaculis est.</p>
</section>
```

### Sectioning Content with article, nav and aside
Let's continue organizing and structuring our content into logical bits, using HTML's content sectioning elements. In this video, you'll learn how to use the `<article>`, `<nav>`, and `<aside>` tags in your project

### Marking up a blog post
Let's create a new page (a blog post) for the site. In the process, you'll use most of the HTML tags you've learned to mark up the content in a semantic way

### Grouping content with <main> and <div>
The `<main>` element represents the main content inside the body of the page, and `<div>` is a generic container that groups content

### Using multiple <header> and <footer> 
You can use multiple `<footer>` and `<header>` elements in one page. You nest footers inside other elements to contain footer information for that section of the page. Nested headers represent introductory content for a section of the page

## Images, Text and Links
Learn to display images, work with file paths, and define text with special meaning

### Understanding file paths
To display an image or link to another page in your site, you need to understand where the file "lives" within the folder structure of the site. In this video, we'll look at examples of how to adjust your file paths based on the directory a file is in

### Adding images to the page
Images draw users in and bring color and life to your pages. Designers and developers use images to display logos, avatars, photographs, illustrations, charts, and more

### Captioning images
HTML provides elements that add visible descriptions to `<img>` elements

### Creating breaks in content
Learn to create breaks in your content using `<br>`, and thematic breaks with `<hr>`

### Add meaning to words with text level elements
Sometimes you'll want to give a piece of text emphasis or importance. HTML provides semantic elements, like `<strong>`, `<em>`, and `<small>`, for formatting text. Other elements like `<span>` are used to mark up text just for styling purposes

## Going Further with HTML
Push your HTML skills further by learning more about file paths and linking to web pages. You'll also learn to work with special HTML characters, comment your code, and explore tips and resources that will help you go forward with HTML

### Linking to sections of a web page
Let's use anchor elements and id attributes to navigate to specific sections of a web page.

### Root-relative paths
Root-relative paths are commonly used when building and testing sites directly on the web or on a local web server

**Start a simple web server from any directory on your computer:**
Open your terminal (or console), navigate to the directory you want to use and enter the following command:
`python -m SimpleHTTPServeer 8000`

You can view your site at this address: localhost:8000

### Link to email
Learn to create "mailto" links that auto-launch a user's default email program with pre-filled subject, to, and from fields

### HTML entities and reserved characters
Certain characters are reserved for use in HTML code only. If you use reserved characters in your content, the browser will interpret them as HTML code, and the characters will not appear in your content as expected

* [Character entity chart](https://dev.w3.org/html5/html-author/charref)

### Adding developer notes with HTML comments
Developers use comments in their code to make parts of it easier to understand. HTML lets you write comments in the code that are ignored by the browser

### Working on a website project locally
You'll often work on websites locally on your own computer, using a text editor. In this video, you'll download the project files from Workspaces to your local drive, then open and preview the files

### Next steps
Learn additional tips, tools, and resources that will help you go forward with HTML

* be curious about how other websites and apps are built
* viewing how others solve problems could be a learning opportunity that provides you with new ideas and tips
* take advantage of browser developer tools like Chrome DevTools
* learn to change visual appearance of html elements with css