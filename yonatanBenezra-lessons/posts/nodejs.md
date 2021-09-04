---
layout: post
title: Node JS
published: 2021-03-30T13:30:34+00:00
author: yonatanBenezra
tags: node.js, Server-side
---
**Server-side development.**

*Client-side means that the action takes place on the user’s (the client’s) computer.
Server-side means that the action takes place on a web server.*

Up until now we talked mostly about the client side, the frontend part of our application with which the user interacts. 
In the next lesson we will start setting up our backend using Node JS.

In this lesson we will learn:
- What Node is
- JS vs. Node
- Running Node code
- Debugging using VS Code
- Modules in Node: exporting and requiring them

**NODE JS**

Node.js is another JavaScript runtime environment
which means it's somewhere we can run JS code that's not the browser.
Lets call it Node for simplicity.

***important note: When said writing in node, mostly the meaning is not to write in node but in Javascript in a node environment***

Up until now we wrote frontend code which means we used JS to write code that runs only the client's device (browser).
Node code is referred to as backend code because the user has virtually zero interaction with it.

Node allows us to:
- Create servers
- Serve data to users
- Communicate with external APIs
- Communicate with databases simply



---

**Clients & Servers**

![](https://techterms.com/img/lg/client-server_model_1253.png)

Lets understand what clients and servers are, including the differences.  
Until now we've only worked on client code.  
In which the web browser (can be thought of as the client) shows the user beautiful interactive web pages using your HTML, CSS and (client-side) JavaScript files.

These files up to now, came directly from our file system, which is why you always saw something like C:/Users/.../index.html in the browser's URL.

But now we'll learn how to use Node to create servers,
and those servers will host our files.
Meaning that *our node servers will serve the client-side of our apps.*

To make this more clear, this is what happens when you enter a site like `ebay.com`,
the browser is making a GET request to the site's server for you - the browser requests all the HTML, CSS, and JS files necessary to let you shop online!

Node.js is a popular open source and cross platform project on GitHub.
Node's JavaScript engine is written in C, and is Google's JavaScript engine.

For the most part, **running JS in node or in the browser is the same** - that is, same syntax, same built-in methods, same objects available to us - **but browser-specific operations are different**.
If we get a little more into the technical side, the interpreter (*the interpreter is the part that actually reads our JS code and translates it to computer commands*) doesn’t pause or sleep while waiting for results. The interpreter is available for serving other requests. When one of the results is ready, a callback is invoked.

We will learn more deeply what a callback is later on.

* **Installing Node**
The first step towards using our computer as a server is to install node, lets do that!

If you do not have Node installed, go ahead and [install it now](https://nodejs.org/en/download/).

THE NODE SHELL

Node has it's own shell where we can write JavaScript and run it, lets check it out.
Open up your terminal (or command-prompt) and type node.
*make sure you have node installed and you are in a new terminal*

Now, try out writing and running some JavaScript:

right this in:

```javascript
let whenDoWeWantToLearnNode = "now"
```
and then
```javascript
whenDoWeWantToLearnNode
```

As you can probably tell, this is the Node equivalent of working in the browser's console - great place to test out small bits of code, but not much else.

To exit the shell, type CTRL + C.

**Running Files with Node**  
*executing JS code from a file using node.*  

Lets create some dummy JS file, and write code that has some console output in it.  
It could be a console log, a function call, anything - you call it.  
Now, in your terminal - make sure you're in the same directory as your file - then type:

```javascript
node yourFileName.js
```
and hit enter.  
You should see your code's output in the terminal.  
this is certainly a much friendlier way to test your JS code, as opposed to creating an HTML file, connecting it to JS, and running it in the browser.

---

Exercise: Copy the following code into your dummy JS file, run it, and solve the problem. Notice how much easier it is to work with JS in this way!

```javascript
const goodies = [
    { g: "Chocolate" },
    { g: "Popcorn" },
    { g: "A good movie" }
]

for (let goodie in goodies) {
    console.log(goodie.g)
}
```

---

**VS Code & Debugging**
But we dont work without our debugger, and Chrome gave us a great tool for that.

if you're using Visual Studio Code, then there's a built-in node debugger!

In fact, you can run JS code directly in VS Code, and see the results in your own terminal. 

And it's very simple: just press F5 to run your code - it can take a moment, but shortly after you should see the Debug Console open up with your code results.

Now to actually debug (i.e. stop your code execution and see what's what), click just to the left of the line numbers where you want your code to stop executing. When you hover your mouse over it, you should see a dull red dot appear:

The dot should turn bright red once you click it.

Then, run your code again ( press F5 ) and you should see a mostly familiar interface:

---

**Node JS Modules**

Modules in node are similar to regular JS modules we've learned about, but now these work as an actual feature of the environment.

By that we mean that in node, every file you write is automatically wrapped in a module for you this means that every file in node is a module.

This is exciting because node allows us to export and import modules from one file to another - this means that we no longer have to rely on our index.html to import everything and allow every piece of our code to be accessible on a global level.  
As an example: create a circleUtils.js file, and add the following code inside:

```javascript
const title = "Circle Utility";
const pi = 3.14159;

const calcCircleArea = function (radius) {
  return pi * radius * radius;
};

module.exports.pi = pi;
module.exports.calcCircleArea = calcCircleArea;
```

we've defined three variables:

A title - a string
The const pi - a number
The calcCircleArea function -  which receives a radius and returns the area of a circle

You didn't think I will leave you hanging withouth explaining about the module.exports right?
every node file (i.e. module) has a built in exports object.
We can assign new keys to this object in order to export (i.e. expose) them to other files. Without this, no other module could access this piece of code.

To see what this means, go ahead and create another file called shapesApp.js, and add the following code there:

```javascript
const circleUtilities = require('./circleUtils');
console.log(circleUtilities);
```

To connect (import) the keys that we exported we will use the require function which takes one argument, a string with a path the file desired.

In this case, the file desired is in the same directory, so we preface its filename with ./ - notice also that we don't have to write out the .js extension, just the filename is enough.

If you run the above code (of course, using the node shapesApp.js command in your terminal, or by pressing F5 in VS Code), you'll see the following object in the console:

```javascript
{ pi: 3.14159, calcCircleArea: [Function] }
```

Yes, circleUtilities is now a plain JS object with two keys:
pi - a number - and calcCircleArea - a method.

However, if you try to run any of these inside of shapesApp.js, you'll get an error:

```javascript
console.log(pi)
console.log(title)
console.log(calcCircleArea)
```

You'll see an error because these only exist in the scope of the circleUtils module!
To access them from shapesApp.js you have to access their values from the circleUtilities object, like so:

```javascript
const circleUtilities = require('./circleUtils')

const r = 4
console.log(`The area of a circle with radius ${r} is ${circleUtilities.calcCircleArea(r)}`)
//^prints "The area of a circle with radius 4 is 50.26544"
```

Just plain dot notation to access the calcCircleArea method from the circleUtilities object.

*separation of concerns is key.*
We have one module, circleUtils which has all the utilities we need for dealing with circles: pi, a function to calculate the area of a circle, and we could add more.

But the actual usage of these utilties is in another module: shapesApp - this is the module that needs access to everything, so it imports them. Now each module is responsible for its own, separate concern.

So we use module.exports to export, and require to import. 
*this only works in node, this will not work if you try to run it in the browser.*

Of course, since module.exports is just an object, there's no reason for us to not be able to just assign it more simply, like so:

```javascript
const title = "Circle Utility";
const pi = 3.14159;

const calcCircleArea = function (radius) {
  return pi * radius * radius;
};

module.exports = {
    title: title,
    pi: pi
}
```

* **Global Scope and Node**

In Node, any variables in the "global" scope are assigned to the module of the file unless you explicitly assign them to the module.exports object.
*which is different from the browser that are variables in the "global" scope are assigned the the window object

If you do not declare a variable with a let or const, it will be assigned to the global scope and will be accessible by any file.
**doing this can lead to the appearance of bugs which are very hard to find.**

Summary:
Node is is not a language, or a server but just a JS runtime environment.
It gives us the ability to run JS, create servers and make dreams come true.

If you'd like to know more about what's going on behind the scenes in node, [here's](http://www.c-sharpcorner.com/article/node-js-v8-javascript-engine-day-one/) something with a little more depth.

This was a very big lesson, the next lessons will be on servers and express,
make sure you get back to this lesson if you don't fully understand something or having trouble in this subjects project.