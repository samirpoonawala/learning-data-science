# (Treehouse) HTML Tables
[link](https://teamtreehouse.com/library/html-tables)

The web is filled with text and images, but it's also filled with information like sports scores throughout the years, list of employee names and email addresses, or nutrition facts for your favorite foods. HTML tables display the information in what is commonly known as tabular data, which is information that's stored in a table-like structure of columns and rows. In general, anything that you might put into a spreadsheet could go in a table. There are many use cases for a table, so it's important to add them to your skills because it's a very common method for displaying information.

What you'll learn:
* table elements
* organizing tables

## Table basics
Tables are a little bit more involved than other HTML elements like paragraphs and images, because in order to construct a table, you need to use elements to represent the individual table cells, the rows that contain those cells, as well as the table itself.

### Overview of tables
It's very common for tables to be populated with information from a database. We're going to build a static table in plain HTML without a database, but for the sake of learning, we're going to imagine that we have a company with a few employees. Each em

### Create a basic table
Similar to an HTML form, you start out creating an HTML table by using the `<table>` element. It has an opening and closing tag, and it wraps all the table rows and table cells inside of it

HTML elements
* `<table>`: the table element represents data in a series of rows and columns. Tables should only be used for displaying tabular data, and never for page layout
* `<tr>`: the table row element defines a row of cells in a table. Table rows can be filled with table cells and table header cells
* `<td>`: the table cell element contains data and represents a single table cell. Each table cell should be inside a table row

### The table header cell element
The table header cell element helps to differentiate between header cells and regular table data. This is helpful for search engine crawlers and screen readers, as well as for CSS styling.

HTML elements
* `<th>`: the table header cell helps label a group of cells in either a column or a row

## Structuring tables
Extra structure can be helpful for automated pieces of software like search engines or screen readers, but it's also helpful for designers because it adds some additional elements that can be targeted with CSS.

### The table head and body elements
The table head element is a completely different element from the table header cell element. In combination with the table body element, the table will gain additional structure.

HTML elements
* `<thead>`: the table head element (not to be confused with the table header cell element) defines a set of rows that make up the header of a table
* `<tbody>`: the table body element defines one or more rows that make up the primary contents (or "body") of a table

### The table foot element
In general a table footer element should contain a summary of the table. This might be some final cells that are sums, totals, and averages for each column. A table footer might also just contain some meta information about the table itself, such as how frequently the table is updated, copyright information, or perhaps the source of the data within the table

HTML elements
* `<tfoot>`: the table foot element contains a summary of the table. This might be totals for columns of numerical data or meta information about the source of data

### The caption element
The caption element is basically a title for the table, and it should come immediately after the opening table tag. This is nice to add because it quickly summarizes what a table might contain.

HTML elements
* `<caption>`: the caption element reflects the title of the table

### More table tips
Tables should only be used for displaying tabular data and not for positioning 

### Extra credit
* If you continue to learn about front-end development, try adding some jQuery to your table. With the right plugin, you can add features like sorting and filtering to an otherwise static table
* If you learn about back-end languages like Ruby, PHP, or Python, try to see if you can populate a table dynamically by using data from a database