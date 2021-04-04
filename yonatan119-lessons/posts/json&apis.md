---
layout: post
title: JSON and API's
published: 2021-04-27T12:30:34+00:00
author: yonatan119
tags: JSON and API's
---

# **Json**
JSON stands for JavaScript Object Notation.   
JSON objects are used for transferring data between server and client, XML serves the same purpose.   
However JSON objects have several advantages over XML and we are going to discuss them in this lesson along with JSON concepts and its usages.

This is how JSON data will look: It basically has key-value pairs.
```json
const chaitanya = {
   "firstName" : "Chaitanya",
   "lastName" : "Singh",
   "age" :  "28"
};
```
___
**Features of JSON:**
- It is light-weight
- It is language independent
- Easy to read and write
- Text based, human readable data exchange format
___
**Why use JSON?**
Standard Structure: As we have seen so far that JSON objects are having a standard structure that makes our job easy to read and write code. 

- **Light weight:** When requesting data from an external server/data storage, it is important to load the data quickly and asynchronously(we will understand what this is further on) without requesting the page re-load. Since JSON is light weighted, it becomes easier to get and load the requested data quickly.

- **Scalable:** JSON is language independent, which means it can work well with most of the modern programming language.   
Let’s say if we need to change the server side language, in that case it would be easier for us to go ahead with that change as JSON structure is same for all the languages.
___
**JSON vs. XML**
Let see how JSON and [XML](https://www.w3schools.com/xml/xml_whatis.asp(similiar to html) look when we store the records of 4 students in a text based format so that we can retrieve it later when required.

JSON style:
```json
{"students":[
   {"name":"John", "age":"23", "city":"Agra"},
   {"name":"Steve", "age":"28", "city":"Delhi"},
   {"name":"Peter", "age":"32", "city":"Chennai"},
   {"name":"Chaitanya", "age":"28", "city":"Bangalore"}
]}
```
XML style:
```xml
<students>
  <student>
    <name>John</name> <age>23</age> <city>Agra</city>
  </student>
  <student>
    <name>Steve</name> <age>28</age> <city>Delhi</city>
  </student>
  <student>
    <name>Peter</name> <age>32</age> <city>Chennai</city>
  </student>
  <student>
    <name>Chaitanya</name> <age>28</age> <city>Bangalore</city>
  </student>
</students>
```
As you can clearly see JSON is much more **light-weight** compared to XML. Also, in JSON we take advantage of arrays that is not available in XML.
___
**JSON data structure types and how to read them:**
- JSON objects
- JSON objects in array
- Nesting of JSON objects

1. JSON objects:
```javascript
const chaitanya = {
  "name" : "Chaitanya Singh",
  "age" : "28",
  "website" : "beginnersbook"
};
```
The above text creates an object that we can access using the variable chaitanya.   
Inside an object we can have any number of key-value pairs like we have above.   
We can access the information out of a JSON object like this:
```json
document.writeln("The name is:  " +chaitanya.name);
document.writeln("his age is: " + chaitanya.age);
document.writeln("his website is: "+ chaitanya.website);
```
___
**2. JSON objects in array**
In the above example we have stored the information of one person in a JSON object suppose we want to store the information of more than one person; in that case we can have an array of objects.
```json
const students = [{
   "name" : "Steve",
   "age" :  "29",
   "gender" : "male"

},
{
   "name" : "Peter",
   "age" : "32",
   "gender" : "male"

},
{
   "name" : "Sophie",
   "age" : "27",
   "gender" : "female"
}];
```
To access the information out of this array, we will write the code like this:
```javascript
document.writeln(students[0].age); //output would be: 29
document.writeln(students[2].name); //output: Sophie
```
___
**3. Nesting of JSON objects:**
Another way of doing the same thing that we have done above.
```javascript
const students = {
  "steve" : {
  "name" : "Steve",
  "age" :  "29",
  "gender" : "male" 
},

"pete" : {
  "name" : "Peter",
  "age" : "32",
  "gender" : "male"
},

"sop" : {
  "name" : "Sophie",
  "age" : "27",
  "gender" : "female"
}
}
```
if you want to access the info from above nested JSON objects:
```javascript
document.writln(students.steve.age); //output: 29
document.writeln(students.sop.gender); //output: female
```
**JSON & JavaScript:**
JSON is considered as a subset of JavaScript but that does not mean that JSON cannot be used with other languages.   
In fact it works well with PHP, Perl, Python, Ruby, Java, Ajax and many more.

Just to demonstrate how JSON can be used along with JavaScript, here is an example:
If you have gone through the above examples, you are familiar with the JSON structures. A JSON file type is .json
___
**How to read data from json file and convert it into a JavaScript object?**
We can do this using JSON parser, Here is how to use it:
```javascript
const chaitanya = {
"name" : "Chaitanya Singh",
"age" : "28",
"website" : "beginnersbook"
};
```
We will converting the above JSON object to javascript object using JSON parser:
```javascript
const myJSObject = JSON.parse(chaitanya);
How to convert JavaScript object to JSON text?
By using method stringify

const jsonText= JSON.stringify(myJSObject);
```
___
**JSON rules and notes**
In JSON, values must be one of the following data types:

- a string
- a number
- an object (JSON object)
- an array
- a boolean
- null

In JSON, string values must be written with double quotes:   
Like this:
```json
{ "name":"John" }
```
to read more about json enter this link [W3Schools-Json](https://www.w3schools.com/js/js_json_intro.asp)
and learn the pages from **JSON** Intro up to **JSON HTML**.
for exercises enter [this link](http://www.steves-internet-guide.com/json-for-beginners/)
___
# **Api**

**What is an API and How Do They Work?**
*all examples and apis are taken from rapidapi.com*
In the process of improving your applications, you will eventually come across a term like API.   
API stands for **Application Programming Interface**.

API is like an open language, the rules of which are shared by a certain service.
You can teach your application the rules of this language, so it can communicate with the service and access all the functions and data that the service is ready to share.   
Speaking a little more formally, API is an interface that allows your application to interact with an external service using a simple set of commands.   
You do not need to know the internal logic of the service, just send a simple command and the service will return the necessary data.

*For example*, if you need to contact the [news aggregator API](https://rapidapi.com/blog/rapidapi-featured-news-apis/) and get ten of today’s most popular news from it, you refer to the “topnews” command (which the service described in advance in the public domain), and in response, the service will send you the latest collection of sensations.
___
**Why are APIs important?**
If there were no APIs, the functionality of your applications would be limited, and the development time would increase significantly since any function that is not implemented as a module of one of the programming languages would have to be developed independently.     
If there were no API, each application would be limited to a narrow list of its own functions without the possibility of expanding it to something that others have already invented and used for a long time.
___
**Benefits of APIs**
APIs allow you to save time when developing and help not to invent a bicycle.   
It is much more efficient and more convenient to use the capabilities of one of the APIs than to try to independently implement similar functionality.   
Moreover, it will be problematic to get some functions and data other than through the API (for example, a [weather forecast](https://rapidapi.com/blog/access-global-weather-data-with-these-weather-apis/), a thematic selection of news or a high-quality translation from almost any language).   

**Types of APIs**
There are four main types of APIs:

- **Open APIs**: Also known as Public APIs, there are no restrictions to access these types of APIs because they are publicly available.   
- **Partner APIs**: One needs specific rights or licenses in order to access this type of APIs because they are not available to the public.   
- **Internal APIs**: Also known as Private APIs, only internal systems expose this type of API, which is, therefore, less known and often meant to be used inside the company. The company uses this type of API among the different internal teams to be able to improve its products and services.   
- **Composite APIs**: This type of API combines different data and service APIs. It is a sequence of tasks that run synchronously as a result of the execution and not at the request of a task. Its main uses are to speed up the process of execution and improve the performance of the listeners in the web interfaces.   
You can read more about API types here: [Types of API](https://rapidapi.com/blog/types-of-apis/)

API Example
An API specification can take many forms, but often includes specifications for routines, data structures, object classes, variables, or remote calls. POSIX, Windows API and ASPI are examples of different forms of APIs. – Wikipedia
___
**Endpoints**
Endpoints are the key elements in the interaction of your application with the API. Usually, it is a specific address (for example, https://newssite.com/topnews), by referring to which you get access to certain features/functions (in our case – a list of top news).
Commonly, the name (address) of the endpoint corresponds to the functionality it provides.

to learn more about Api, which is highly recommended, see [this](https://www.w3schools.com/js/js_api_intro.asp) and go through the lessons from *Web API Intro* to *Web Geolocation API*
___
