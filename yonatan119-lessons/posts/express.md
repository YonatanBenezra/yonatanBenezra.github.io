---
layout: post
title: Express
published: 2021-03-23T16:30:34+00:00
author: yonatan119
tags: express
---

# **Express and servers**

Let's talk about servers before getting to express.
First, what is a server?  
A server is a physical machine.  
any data, code, and program, is stored or executing on a physical machine somewhere on the ground (or underwater), nothing is in an actual cloud or in the sky - yet.  
We use servers to serve data such as files, images or videos - what you see on a webpage is mostly being served to you from some server, somewhere.  
some important notes about servers:
- There can be thousands of servers serving the same data/files - but there will virtually always be more clients than servers, and the server will always serve some information to the clients.
- servers should be stateless, this means that the server itself does not keep any information about the client.
lets make the second note clear, because it is very important.  
Any communication between the server and client is a one-time deal, and should include all the necessary information to complete a transaction.
*The server may receive data from the client, then store that data in a database but it should never "keep a state" or "remember" anything about the client.*
A valid request-response cycle is when the client requests for data and the server optionally does something, then sends a response in return.  
We will see plenty examples further on the course.

Alright, we've been teasing servers for a while. Now it's time to actually build a real one. It will still run on localhost (your machine) for now, but it will be a real server.

- The express package
- Routes
- Parameters

**EXPRESS**
Express is an NPM package that allows us to create servers easily.  
NPM is the world's largest software library, it basically lets you install packages easily.
so go ahead and open a new directory and create a file named "server.js". go to this directory in the terminal and write:

```javascript
npm install express
```

inside of your server.js file add to the top

```javascript
const express = require('express')
```

We need to require every NPM package we want to use.
By convention, we invoke express and store its value in a variable called "app" or "server":

```javascript
const app = express()
```

One of the more method we will use is the listen method. We invoke it like this:

```javascript
const port = 3000
app.listen(port, function(){
    console.log(`Running server on port ${port}`)
})
```

Now - in your terminal, in the same directory where this file is - run the file:
```javascript
node server.js
```
This will start a server that is listening on port 3000 (notice the callback function that gets invoke after the server starts running).  
You are probably wondering what the server is listening to, so the basic answer is - requests.  servers are responsive entities, they listen for requests and only act when asked to.  
The requests can come from wherever like browsers, apps, code.  
The server will respond, it doesn't care who is asking.  
This piece of code goes at the bottom of our server.js file - everything we add from now one should come before that.

Lets go to localhost:3000, we should see an error "Cannot GET /".  
The reason for this error, is we are not doing anything in our server.js file except run the server so when we try to go to localhost:3000, the browser is making a GET request and receives nothing.
Add the following code to your file before the app.listen section:

```javascript
app.get('/', function (request, response) {
    console.log("Someone is coming!")
})
```

Now, whenever the browser (or anyone) tries to visit localhost:3000/,our server invokes this callback function with these two parameters - we'll talk about these parameters and what "/" means in a minute.
lets see this happening, restart your server by saving (Ctrl + C) then in your terminal write 

```javascript
node server.js
```

refresh the page.  
We see nothing on the browser! but... if we go back to our terminal we should see our console "Someone is coming!  
But if you look closely at the browser, you'll see that the page is forever loading. This happens because the client (the browser) has made a request, but the server never made a response! The request-response cycle has not ended! And so our client will wait forever!  
We don't want our client to keep on waiting forever so lets send a response.  

```javascript
app.get('/', function (request, response) {
    console.log("Someone is coming!")
    response.send("Wont keep you waiting..")
})
```

We're taking advantage of the response object to invoke the send method - this sends a response to the client!  
lets restart the server and return to the browser and see what happens.  
**Congratulations**, you created a server!

---

**Nodemon**
I want to show you a cool npm package named Nodemon that will save us the trouble of pressing ctrl + c and then running again "node server.js".  
Open your terminal and run the command npm install -g nodemon.  
The -g is a flag the tells the computer to install the package globally which means that you can run the command in any project without installing the package again and again.  
Now, instead of running node server.js you should run nodemon server.js.  
try changing something in the server.js, save it, go to the browser and refresh the page.  
isn't it cool?

---

PC users:  
If you are running into a error message saying something like this:

```javascript
nodemon : File C:\Users\yoni\AppData\Roaming\npm\nodemon.ps1 cannot be loaded because running scripts is disabled on this system.   
For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
```

Open your "Window PowerShell" as administrator (You can search for it in the search panel), and run

```javascript
Set-ExecutionPolicy remotesigned
```

Mac users:  
If you running into problems installing the package, try sudo npm install -g nodemon  and enter your mac password.

**Routes**
Now our users can go to `http://localhost:3000/` but what happens if we having several pages?
For instance if we go to ebay.com and click on Electronics we can see the url change to something like this: "https://il.ebay.com/b/Electronics/bn_7000259124".  
This "/Electronics" is a route, lets add one to our app.  

```javascript
app.get('/', function (request, response) {
    console.log("Someone is coming!")
    response.send("Wont keep you waiting..")
})

app.get('/electronics', function (request, response) {
    response.send("Here will be electronic stuff")
})

app.get('/clothes', function (request, response) {
    response.send("Here will be clothes stuff")
})
```
***The "base" / is known as the root route and has no specific name.***
Lets restart our app, go to each of these routes and see what happens.  
Right now these routes are just returning simple strings (i.e. data), but soon we'll see how to return entire files/directories/json.

---

**Params**

Sometimes we need to send information from the client to the server when we make requests.  
Lets try this with sending a private welcome message. 

```javascript
app.get('/landing/:username', function (request, response) {
    response.send(`Hi there, ${request.params.username}`)
})
```

Now go to `http/localhost:3000/landing/"username"`.  
*Switch "username" with your own name, this will be what I will write:

```javascript
http/localhost:3000/landing/yonatan
```

What did we do here?
- We used the request object to access the params (parameters) property, which allows us to access anything the is sent through the route.
- We used /:username as a placeholder for anything that comes after /landing.
*Any part of the route that starts with /: will be a variable that has to come in through the route*.  
Parameters that are part of the route (like :/username or :username from above) are required parameters. If you go to /landing/:username without supplying a username, it will not work.
However, we can also accept optional parameters like this:
```javascript
app.get('/electronics', (request, response) => {
    let params = request.query
    response.send(params)
})
```
This code allows us to send an optional parameter after electronics like this
```javascript
/?{KEY}={VALUE}.
```
*It stores the key and value inside an object.*
We can add as many parameters as we want in our route. We just need to separate each key-value pair with an ampersand: &.  
Try this out!

**Serving Files**
Lets see how we can serve files instead of a string or object.  
To show how this works, go ahead and create a folder called **dist**, and inside of it add three files:
- index.html
- style.css
- main.js

The dist folder is a directory that our server will serve to whoever asks.  
The name dist is a convention, other known names are client, build, or public.  
Lets add some code to our files for an example of how to serve files.

html:

```html
<!DOCTYPE html>
<html>

<head><meta charset="utf-8" /><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>Awesome site</title><link rel="stylesheet" type="text/css" media="screen" href="style.css" />
</head>

<body>
<div onclick=changeColor(this)></div><script src="main.js"></script>
</body>

</html>
```


style.css:

```css
div{
    width: 100px;
    height: 100px;
    background-color: #e67e22;
    box-shadow: 1px 1px 3px black;
}
```

main.js:

```javascript
const changeColor = function (div) {
    div.style.backgroundColor = "#3498db"
}
```

server.js:

```javascript
const express = require('express')
const path = require('path')
const app = express()

app.use(express.static(path.join(__dirname, 'dist')))

const port = 3000
app.listen(port, function () {
    console.log(`Running server on port ${port}`)
})
```
You can see your first served application if you restart your app and go to localhost:3000.  
Think you can serve one of your projects using what you learned? go for it!

---

**CRUD**

Up to now, we've only worked with GET requests.
We use GET requests (and GET routes) to get or serve information from some server.  
This makes sense when working with APIs/simple servers but eventually we'll have data that we want to update/delete in our own databases.
That means we need methods not just for GETting data, but also for
- Creating (POST) data
- Reading (GET) data
- Updating (PUT) data
- Deleting (DELETE) data
These four data-related operations are known as CRUD operations.  
