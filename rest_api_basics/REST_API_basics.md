# REST API Basics

[Link to course](https://teamtreehouse.com/library/rest-api-basics)

***About this course***

Many of the APIs you'll encounter on the Web use an underlying design idea known as REST, which stands for Representational State Transfer. Understand what and how a REST API provides will help you build better and stronger APIs for your users.

***What you'll learn:***
* REST concepts
* URI Design
* Other API concepts

## Getting the REST you need
The RESTful API design pattern is a common, useful, and real world design pattern for turning your web app into a useful tool for building web apps, bots, desktop and server scripts, and more. Let's talk about what REST is, the building blocks and terminology of REST, and how you'll be using REST here at Treehouse.

* **Introduction**
  * REST stands for Representational State Transfer. REST sits on top of HTTP and defines how your API works. Mostly, it's a set of rules for how to use the HTTP framework to access bits and pieces of your application or data in reliable and predictable ways
  * API = Application Programming Interface
  * The web is, by design, stateless
* **Endpoints**
  * Endpoints are the workhorses of our APIs. Let's talk about what they're expected to do and how to design them
  * A resource is a piece of data, which usually comes out of a database (but doesn't have to!). Resources are gathered together into collections. Resources are usually available at endpoints that either point individual resources or collections of resources. Endpoints don't represent actions that you take on those resources, though. Actions are determined by the data provided to an endpoint and the HTTP method used to access the endpoint
  * By combining endpoints and HTTP methods, we can build complete sentences with just HTTP and REST
  * ***GET*** is used for fetching either a collection of resources or a single resource
  * ***POST*** is used to add a new resource to a collection
  * ***PUT*** is the HTTP method, or verb, that we use when we want to update a record. We wouldn't use PUT on collection or list URLs
  * ***DELETE*** is used for sending a DELETE request to a detail record, a URL for a single record, should delete just that record. Sending DELETE to an entire collection would delete the whole collection but that's usually not implemented, with good reason
* **Requests**
  * With our endpoint nouns and HTTP method verbs, we can start to build up the design of our API, but what happens when we need more information than those two things can give us?
  * Query strings come after a question mark (?) in a URL. They have keys and values
  * [Here is a complete list](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields) of HTTP header fields that are available on requests. For many clients and servers, you can also create your own, usually following a format like `X-MY-SPECIAL-HEADER`
* **Responses**
  * Once a client sends us a request, we need to generate and send back a response. There's more to a response, though, than just the data content
    * like an HTTP request, an HTTP response also has headers
  * [HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
    * 200-299 --> good
    * 300-399 --> understood, located elsewhere
    * 400-499 --> errors (client end)
    * 500-599 --> errors (server end)
* **Security**
  * Very few REST APIs are open for unlimited public consumption. Let's see what steps we can take to make our API stronger and safer
  * A cache is a service that holds onto data that you need to be able to retrieve quickly
  * "rate limiting"
  * authentication
    * API tokens
