---
layout: post
title: Blog Fullstack
published: 2021-05-04T13:30:34+00:00
author: yonatanBenezra
tags: node, js, javascript, express, mongodb, react
---

Project Setup
- Create a directory for your project and cd into it
```javascript
 mkdir mern-blog && cd mern-blog
```
Structure
- server.js - JS file
- models - Folder
  - article.js
- routes - File
  - index.js
___
**Package.json**
Generate a package.json file. This file contains the metadata for a Node.js project. Adding the --yes flag will use the defaults for the fields.
```javascript
npm init -y
```
Packages:
- express
- mongoose
```javascript
npm install express mongoose
```
Your package.json file should look something like the below. A list of the project's installed packages with version is saved under dependencies.  
If we ran npm install then npm would attempt to install or update the packages listed there.  
Make sure the "main" property's value is "server.js". Change it if it isn't.  
Also make sure you have the "start" script. Add it if you don't.  
We can run the commands in the scripts object from the command line with 
```javascript
npm run script-name
```
I'll explain more in the next section.
```javascript
//package.json
{
  "name": "mern-blog",
  "version": "1.0.0",
  "description": "Web app built with Node.js, Express, MongoDB, and React",
  "main": "server.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "node server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.17.1",
    "mongoose": "^5.6.6"
  }
}
```
You will also see a file named package-lock.json.  
That lists all the project's installed packages with their versions and their dependencies.
___
**Express Web Framework**
*Server.js*
Populate the server.js file with a hello world app powered by Express:
```javascript
// server.js
const express = require('express');
const app = express();
const PORT = 3001;

app.get('/', function(request, response) { response.send('Hello World!') });

app.listen(PORT, function() { console.log(`Server listening on port ${PORT}`) });
```
This simple file, with the Express library, will create a server.  
There are a few different commands you can use to run it. I'll cover them briefly.  

- First there is a standard node command to execute any file:
***node server.js*** or just ***node server***
This should log "Server listening on port 3001" in the terminal, and if you open a browser to localhost:3001 you should get "hello world". To stop the server, from the terminal press CTRL+C,

- NPM init generated a script to run this command in our package.json file. You call the scripts in your package.json file with npm run script-name or in a few cases "run" is optional.  
***npm start***  

- The third way to execute the server.js file is to use the nodemon command. We installed nodemon for hot reloading. To use it just enter nodemon and it looks for a file named server.js to run by default. This is the command we'll use throughout this project.
```javascript
nodemon
```
A quick note on syntax. Node recognizes most, but not all, ES6 syntax. Notably it does not recognize import/export statements, so we won't use them here. You have the option of installing Babel which will translate it for you. Since it's not critical to this project we won't do it. Also, as default I am using the declaration syntax for functions rather than arrow functions. That just makes it consistently explicit what your function is returning or if it isn't returning anything.
___
**MongoDB database**
MongoDB offers a cloud database called Atlas, or you can download the "community version" on your local machine. You may want to use mlabs like in our previous projects but it will be good to practice different ways. Which to use? I generally prefer a local version to work with in development. Sometimes there are connection issues with a cloud version (which I ran into). But if you deploy your app then you need a cloud solution. I will explain both ways.
*Reminders*
"Collections" are like tables in a relational database and "documents" are like records.
Also, don't worry about creating the collections. Once you create the database and connect to it, MongoDB will automatically create a collection for you when you save a document to a collection that doesn't exist yet.
___
**Option 1) MongoDB Atlas**
At the time of this writing you can set up a free account for a small project like this one at mongodb.com/cloud/atlas. It is very fast and straight-forward to set up. Just follow their steps, but note a few things:

- It will ask you for a name and password for the project. You will use these to access the database.
- In one of the steps they will ask you to whitelist the IP addresses that will be accessing your database. For a practice app like this just click on "add IP" and select the "Allow access from anywhere" option.
- Skip seeding the database.
- For the last step you select a connect option. We want the "Connect your application" option. That will provide you with a link to add to your application. Something like
```javascript
mongodb+srv://user:password@cluster-number.mongodb.net/test?retryWrites=true&w=majority
```
Copy this and paste it into the server.js file (which we'll cover next).
___
**Option 2) MongoDB local "community" version**
in case it is not installed yet, installation instructions are at docs.mongodb.com/manual/project/install-mongodb-on-windows.
Once it's installed you run MongoDB from the terminal (from any directory) and have to leave that window open and running to access the database:
```javascript
mongod
```
Stop MongoDB from the same terminal window with CTRL+C.

**MongoDB Shell**
You can interact with the database directly using the MongoDB shell from the Terminal. There are also GUI tools like Robo T3 if you prefer that but frankly for small projects I find the command line easier to work with. To use the shell from anywhere in the terminal run:

**Mongoose ORM**
We installed the mongoose package in our app. Just a reminder, Mongoose is a middleware library that performs the Object Relational Mapping (ORM) between our Express application and MongoDB. In essence it does the translations allowing them to talk to each other.
We'll start by using Mongoose to connect to MongoDB in our server file. Let's replace the hello world response with our real code and then we'll go through it line by line.
Try by yourself first.  
- Start by importing our express and mongoose packages and our Express router which we'll define shortly.
- Calling the express() function will create our running app object.
- The Express listen method called at the bottom of our file uses 3000 as it's default port for it's server. We'll declare a new PORT constant to give us the flexibility to use different ports depending on whether we are in development or production.
- Assigning constants for things like port number and the database URL gives us the flexibility to change the values in one place.
If you are using the MongoDB Atlas cloud database then paste the link there.
If you are using the local version, MongoDB is accessed through localhost on port 27017 by default, and the path is the database name. We'll just call ours my_local_db.
- Chaining Express's use method to our app object gives us access to the libraries we imported. express.urlencoded({ extended: true }) and express.json() are middleware for parsing requests with JSON payloads (for POST and PATCH/PUT requests).
- Apply the Express router object to your Express app. I'll explain this in the routing section.
- mongoose.connect() connects to our MongoDB database
- Optionally, log a message if the above connection was successful and one if it is not.
- Chain the Express listen method to our app. This will listen for connections on the specified port.

```javascript
// server.js
const express = require('express'); 
const mongoose = require('mongoose');
// const cors = require('cors');
const router = require('./routes/index');

const app = express(); 
const PORT = 3001; 
const MONGODB_URI = "mongodb://localhost:27017/my_local_db"; 

// app.use(cors())
app.use(express.urlencoded({ extended: true })); 
app.use(express.json());
app.use('/api', router); 

mongoose.connect(MONGODB_URI, { useNewUrlParser: true, useFindAndModify: false }); 
mongoose.connection.once('open', function() { 
  console.log('Connected to the Database.');
});
mongoose.connection.on('error', function(error) {
  console.log('Mongoose Connection Error : ' + error);
});

app.listen(PORT, function() { 
  console.log(`Server listening on port ${PORT}.`);
});
```
___
**Cors**
Let's talk briefly about Cross-Origin Resource Sharing (CORS).  
By default Express will block cross-origin HTTP requests for security reasons.  
Cross-origin means the request is from a different origin (domain, protocol, and/or port) than its own origin.  
Our API is served on localhost port 3001, if our API is accessed by mobile apps for example they will be on a different origin and any requests will be rejected.  
There is an npm package called cors that will apply additional HTTP headers to tell the browser to allow access from a specified origin or any origin.

A standard MERN app is really an integrated single web application even if the back end and front end run independently.  
We only want to give access to the integrated front end (our React client in this case) and therefore won't use the cors package.  
There's an additional step when we build the React app that we'll cover there.

If, however, your API is meant to be accessed by mobile apps or other websites then you need to install the cors middleware package and connect it to your app.
```javascript
npm install cors
```
The server.js file comments out the cors package import and where it is applied to the app, to allow cross origin access uncomment those lines.  
For more on the CORS concept see developer.mozilla.org/en-US/docs/Web/HTTP/CORS
___
**Schema and Model**
Populate the model file with the below:
```javascript
// models/article.js
const mongoose = require('mongoose');

const articleSchema = new mongoose.Schema({ 
  title: {
    type: String,
    required: [true, "Title is required"]
  },
  content: {
    type: String,
    required: [true, "Content can't be blank"]
  }
});

module.exports = mongoose.model('Article', articleSchema); 
```
- A database schema is it's structure, the mongoose schema is a prototype that maps to a MongoDB collection and defines the shape of the documents within that collection.  
Here we are creating an instance of mongoose.Schema that defines two fields with type set to String and making them required.  
Read about Mongoose Schema at mongoosejs.com/docs/guide.html.
- Models represent the data in an application, a mongoose model is a constructor function that creates and reads documents to and from the underlying MongoDB database.  
The first argument is the singular uppercase name of your database collection.  
So Article represents the articles MongoDB collection.  
The second argument is the schema which we defined above.  
An individual article is an instance of the Article model.
___
**Routes**
Now that we have our server, database and model set up, the last step for our simple API application is routing.  
Routing refers to determining how an application responds to a client request to a particular endpoint. An endpoint is a combined URI and HTTP request method (GET, POST, PATCH or PUT, DELETE) that activates specific actions from our API.

We will apply database Create, Read, Update, and Delete (CRUD) actions to each endpoint.  
Meaning we will have an endpoint to return (Read) a JSON array of all our articles and another endpoint to return (Read) a JSON object for a specified article id.  
We will also have endpoints to Create, Update, and Delete articles, so our routes will be "RESTful" which essentially means our application routes and actions are built around performing these database CRUD actions.  
Populate the routes file:
___
Steps:
- Create an instance of the Express Router to be used as middleware for our routes.
- Import the Article model.
- For each API endpoint we will chain a method to the router object. The format is:
```javascript
router.HTTP Method(path, handler function)
```
We will import the Article model representing the articles collection in our database.  
We chain methods from the mongoose library to the Article prototype that will perform different types of CRUD actions.  
Our handler functions perform the CRUD operation and may return a response.  
Generally only return responses that will be used by the client.
- Get request to /articles returns a JSON array of all article objects found in the database.
- Get request to /articles/:id (:id is a variable representing an article's _id) returns a JSON object of the specified article if it exists, otherwise returns status 404 and "No result found"
- Post request to /articles creates a new Article instance from the JSON object in sent in the HTTP request body and saves it to the database.  
If successful a status 200 code is automatically returned. We'll add on to that a JSON response with the new article object we just added which includes the article _id generated by the database.
- Patch request to /articles/:id updates the specified article with the JSON object sent in the HTTP request body. You could use the PATCH, PUT or POST HTTP methods since they all send a payload. It's the handler function that determines what is done with the payload. On a successful update we are returning a JSON response just stating "Article updated". If the article did not update then we send an Unprocessable Entity code 422 response with a message.
- Delete request to /articles/:id first checks if the article exists. If so it deletes it and sends status 200 with a JSON response of "Article deleted".
- Export the router object with our Article endpoints.
Try it out yourself before going down.
```javascript
// routes/index.js
const express = require ('express'); 
const router = express.Router(); 
const Article = require('../models/article'); 

router.get('/articles', function(req, res) { 
  Article.find(function(err, articles) {
    res.json(articles);
  });
});

router.get('/articles/:id', function(req, res) {  
  Article.findById(req.params.id, function(err, article) {
    if (!article) {
      res.status(404).send('No result found');
    } else {
      res.json(article);
    }
  });
});

router.post('/articles', function(req, res) {     
  let article = new Article(req.body);
  article.save()
    .then(article => {
      res.send(article);
    })
    .catch(function(err) {
      res.status(422).send('Article add failed');
    });
});

router.patch('/articles/:id', function(req, res){    
  Article.findByIdAndUpdate(req.params.id, req.body)
    .then(function() {
      res.json('Article updated');
    })
    .catch(function(err) {
      res.status(422).send("Article update failed.");
    });
});

router.delete('/articles/:id', function(req, res) {  
  Article.findById(req.params.id, function(err, article) {
    if (!article) {
      res.status(404).send('Article not found');
    } else {
      Article.findByIdAndRemove(req.params.id)
        .then(function() { res.status(200).json("Article deleted") })
        .catch(function(err) {
          res.status(400).send("Article delete failed.");
        })
    }
  });
})

module.exports = router;
```
In the server.js file we imported our router object and then chained it to our Express app object.  
The first argument '/api' applies our router object when the '/api' path is called.
```javascript
// server.js
const router = require('./routes/index');
...
app.use('/api', router);
```
Rememmber the Model-View-Controller pattern (MVC)? Express uses that pattern as well.  
- Model we talked about. 
- Controller is a combination between the actions directly with the routes rather than separating them into separate route and controller files. 
- view will be our React front end. Or you may say our view is the JSON responses returned when accessed by our front end React app. Let's see those in action.  
With all the changes it's best to just restart your server:
```javascript
$ CTRL+C
$ nodemon
```
Then in your browser go to the API articles endpoint:
http://localhost:3001/api/articles
And you should see an empty array. Congratulations!  
All that hard work paid off, An empty array. Now lets test all the endpoints using Postman.
___
**Postman**
Here are the CRUD actions hitting our API's endpoints:
- Get Articles request: GET *`http://localhost:3001/api/articles`*
- Get Article request: GET *`http://localhost:3001/api/articles/article._id`*
- Add Article request: POST *`http://localhost:3001/api/articles`*
Headers: Content-Type application/json
Body: {"title": "Learn Web Development", "content": "Lorem ipsum."}
- Update Article request: PATCH *`http://localhost:3001/api/articles/article._id`*
Headers: Content-Type application/json
Body: {"title": "Learn APIs", "content": "Blah Blah Blah."}
- Delete Article request: DELETE *`http://localhost:3001/api/articles/article_id`*
___
If everything works then our simple API is done! We can use this API as the back end for a mobile app, or to be accessed by other websites to display our amazing articles.  
We will integrate it with React as the front end framework.

***You did alot, maybe take a coffee break and come back?***

**Frontend Setup**
*Create-react-app*
We already created an API that we will be using as our back end.  
We could keep the front end and back end code in completely separate locations, but if we are to deploy our application in production as an integrated web application it's easier to keep them together.  
We'll add a directory called client to our project and place our React application there.
```javascript
create-react-app client
cd client
```
Poof... we now have a working React app ready to go. Start the server:
npm start
And this should open your browser to localhost:3000 and greet you with a Welcome to React web page including a spinning logo. We're in business.
___
**Third party packages**
We will be using two third party packages, React Router for routing and Axios for AJAX requests.  
___
**client/package.json**
Inside our React file structure is package.json, this file lists the locally installed packages as dependencies.  
You should see react, react-dom, and react-scripts in there. You can read about it at docs.[npmjs.com - package.json](https://docs.npmjs.com/getting-started/using-a-package.json).

Install the react-router-dom (for routing), axios (for AJAX requests), and bootstrap packages. The bootstrap package is a popular CSS library that we'll use for convenience and discuss a bit more in the stylesheets section.
```javascript
npm install react-router-dom axios bootstrap
```
Now if you look back at the packages.json file you should see those packages as dependencies.  
Make one more change to the package.json file.  
- Add a proxy property set to your API's port.  
This will automatically be added to the API routes we call from our React front end, so we only have to use the paths, not the full URLs in our code. There are other ways we could accomplish the same thing, but this makes it easier if you deploy your app to a platform like Heroku. And we won't need to use the cors package in our API.
```javascript
// client/package.json
{
  "name": "client",
  "version": "0.1.0",
  "private": true,
  "proxy": "http://localhost:3001",
  "dependencies": {
    "axios": "^0.19.0",
    "bootstrap": "^4.3.1",
    "react": "^16.8.6",
    "react-dom": "^16.8.6",
    "react-router-dom": "^5.0.1",
    "react-scripts": "3.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  ...
}
```
**File Structure**
If you look at the files and directories generated in the client directory, besides a folder for the node_modules you'll see a "public" and a "src" directory.  
These are where you add your own files, right now there are no sub-directories in those folders so things can get pretty cluttered quickly if we don't add some structure.  
From the client directory you can use these UNIX commands to add and remove the relevant directories and files. Or do it from your text editor if you prefer.
```javascript
rm README.md
rm -rf .git
mkdir -p src/components/pages
touch src/components/pages/Home.js
mkdir src/components/articles
touch src/components/articles/ArticleList.js
touch src/components/articles/ArticleInfo.js
touch src/components/articles/ArticleAdd.js
touch src/components/articles/ArticleEdit.js
```
We removed some unnecessary files including the git repository that create-react-app generated for us ("**rm** does this"). We won't be using git in this project but if we were we would generate a git repository in the project root directory for our API and our React client combined.  
You can leave the .gitignore file though since git allows multiple gitignore files.
We left the logo.svg file for now so our app doesn't crash. You can delete it at the end.
___
**Stylesheets**
The index.css file is for our app-wide css. If you want to add custom CSS classes that apply to the whole app this is where you would do it.  
The App.css file is specific to the App.component we are going to fill out.  
Delete the CSS that's in there now so it doesn't conflict with our app.
```css
// src/stylesheets/App.css
/* Remove all the CSS classes */
```
To add css classes that apply only to a particular component you could create a css file in the same folder as that component and import it in the component(s) that use it.  
**Bootstrap**: For convenience we're using Bootstrap for our styling. We installed the bootstrap package earlier. Now import it to our index.js file.
```javascript
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';
import App from './App';
...
```
If you want to use the JavaScript features of Bootstrap like drop-down menus you can also install the react-bootstrap package,  
We won't use those in this project.
___
**public/index.html - Our Single Page App**
This is a Single-Page Application (SPA) with CRUD capabilities, it is indeed single page.  
We only have one html file sitting in the public folder: 
- public/index.html.  
It has your standard HTML page structure with one element inside the body. An empty div tag with id name of root <div id="root"></div>.  
That is where React renders it's output with JavaScript. There's nothing special about the name "root." It can be any name.
___
**src/index.js File**
In the src/index.js file we import the React library and render our main component. Other than adding the Bootstrap import above, we don't need to make any changes to the src/index.js file. It should look like this.
```javascript
// src/index.js
import React from 'react';                                   #1a
import ReactDOM from 'react-dom';                            #1b
import 'bootstrap/dist/css/bootstrap.css';          
import './index.css';
import App from './App';                                     #1c
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));   #2
serviceWorker.unregister();                                  #3
```
- #1 We import the React and ReactDOM libraries, and the App.jsx file (containing the App component).
- #2 The ReactDOM module's render method is what renders your React components to the public/index.html page. It takes two arguments. The first calls our component which is a custom React element called "App", or whatever name you want to give it. The second argument is the target element where we will render the output from <App />. In this case the element with the id of "root".
- #3 The service worker is a web API that helps you cache your assets and other files so that when the user is offline or on a slow network they can still see results on the screen. It is actually not activated by default so we're leaving it that way as well (change .unregister to .register to make it active).
___
**React Components**
*This is a sole reminder*
- With React you split your user interface into components, each component returns some JSX which ultimately gets rendered as HTML to the user interface.  
In our case we are creating the front end to a CRUD application.  
We need components to correspond with the API's endpoints to perform the CRUD actions.
- A few notes on syntax. We can use all the latest JavaScript syntax without worrying about browser compatibility because create-react-app installed Babel which compiles our JavaScript into ES5.  
We did not add the step of installing Babel in our API, so while we could still use most of the ES6 syntax, there are some features not yet supported by Node like the Import and Export syntax. But we can and will be using those here.  
Also, in general I am using the declaration syntax for functions rather than arrow functions just to make it explicit when you are returning a value.  
But it is recommended to use arrow functions if you prefer it.
- The App.js component file holds the structure for our web page:
  - The ArticleList
  - ArticleInfo
  - ArticleAdd
  - ArticleEdit 
These components represent views that correspond to the Read, Read and Delete, Create, and Update actions respectively.  
We'll also add a Home component to be our home page.  
*Note that component names must be capitalized.*  
In each file we will build one React component, with the exception of App.js where we build three.  
We could break it out even further, like a form component that gets imported to the ArticleAdd and ArticleEdit components, but we won't.
___
**Home Component**
Before we build our full CRUD app let's start out with a very simple component called Home. We already created an empty Home.js file. Populate it with the below:
```javascript
// src/components/pages/home.jsx
import React from 'react'; 

function Home() { 
  return (
    <div className="jumbotron">
      <h1>Home Page</h1>
    </div>
  );
}

export default Home; 
```
- We are 
  - importing React
  - creating a component
  - then exporting it
- Home simply returns some JSX. JSX looks like HTML but it actually isn't, not yet anyway.  
You'll notice subtle differences between JSX and HTML like you have to use the className attribute instead of class since "class" is a reserved word in JavaScript.  
But React ultimately converts JSX to HTML through its ReactDOM.render method. 

*Right now this file is just sitting in space not connected to anything*
___
**App component**
The term Single-Page App can be a little misleading. While it is indeed a single html page, that doesn't mean you can't have multiple views with changes to the URL.  
We will use the React Router package that we installed to do just that.  
We will also perform the standard CRUD actions in our single page interacting with the API to:
- get articles
- post new articles
- edit existing articles
- delete articles
Instead of doing those things all on separate HTML pages as you would in an traditional web app, we will do it from our single page using AJAX calls with the help of the Axios package we installed.  
React will move the data around using JavaScript which can add significant speed over entire page loads from the server.  
The top level component for our app is the App component. That is what is returning the Welcome to React page we see in the browser.  
Replace that with a Navigation bar and a place to render the other components. Here is the code for the App.js file all at once:
```javascript
// src/App.js

import React from 'react';
import {BrowserRouter as Router, Route, NavLink, Switch} from 'react-router-dom';
import './App.css';
import Home from './components/pages/Home';
import ArticleList from './components/articles/ArticleList';
import ArticleInfo from './components/articles/ArticleInfo';
import ArticleAdd from './components/articles/ArticleAdd';
import ArticleEdit from './components/articles/ArticleEdit';

function App() {
  return (
    <div className="App">     
      <Router>
        <Navigation />
        <div className="container">
          <Main />
        </div>
      </Router>
    </div>
  );
}

function Navigation() {
  return(
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
      <div className='container'>
        <ul className="navbar-nav mr-auto">
          <li className="nav-item"><NavLink exact className="nav-link" activeClassName="active" to="/">Home</NavLink></li>
          <li className="nav-item"><NavLink exact className="nav-link" activeClassName="active" to="/articles">Articles</NavLink></li>
        </ul>
      </div>
    </nav>
  );
}

function Main() {
  return(
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/articles" component={ArticleList} />
      <Route exact path="/articles/new" component={ArticleAdd} />
      <Route exact path="/articles/:_id" component={ArticleInfo} />
      <Route exact path="/articles/:_id/edit" component={ArticleEdit} />
    </Switch>
  );
}

export default App;
```
First thing's first. Once you add the code and save the file, go to the browser and make sure you didn't get any errors.  
We removed the Welcome to React header and logo and replaced it with a navigation bar with two links, and a simple home page jumbotron.  
If you do get an error try restarting the server: 
```javascript
$ CTRL+C 
$ npm start
```
If you click on the articles link it will give you an error because we haven't populated that yet.

This file actually contains three separate functional components
- App
- Navigation
- Main
But most of this code relates to Navigation and the React Router package. React Router is the most popular Routing package.  
The docs are at [reacttraining.com/react-router/web/guides](https://reacttraining.com/react-router/web/guides/philosophy) which looks like a third party training site, and it is.  
But they are the ones who created the React Router package (not Facebook's React team).  
Alright, let's break this down.

*At the top are all of our imports:*
```javascript
import React from 'react';                                                        #1
import {BrowserRouter as Router, Route, NavLink, Switch} from 'react-router-dom'; #2
import "bootstrap/dist/css/bootstrap.min.css";                                    #3
import '../stylesheets/App.css';              
import Home from './components/pages/Home';                                       #4
import ArticleList from './components/articles/ArticleList';
import ArticleInfo from './components/articles/ArticleInfo';
import ArticleAdd from './components/articles/ArticleAdd';
import ArticleEdit from './components/articles/ArticleEdit';
```
1) To create a component we need to import the React library.
2) Import the components you need from the react-router-dom module. React Router also has a react-router-native module for mobile apps. In this case we'll import the BrowserRouter (giving it an alias of Router), Route, NavLink, and Switch components.
3) Import the Bootstrap CSS library we added.
4) Import the other components that we will be calling with our Routes. Each of those files will contain a functional component.

**The App component's return statement:**
```javascript
function App() {
  return (
    <div className="App">  
      <Router>                            #1
        <Navigation />                    #2
        <div className="container">          
          <Main />                        #3
        </div>
      </Router>
    </div>
  );
}
```
1) In the App function's return statement we appended the <Router> element to manage our routing. It contains two custom elements:
2 & 3) ***<Navigation />*** and ***<Main />*** are custom elements that call the corresponding components.  
Nothing special about those names, you could call them what you like. Those components return JSX that gets inserted into the App component.

**The Navigation component:**
```javascript
function Navigation() {                                       #1
  return(
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
      <div className='container'>
        <ul className="navbar-nav mr-auto">
          <li className="nav-item">                             #2
            <NavLink exact className="nav-link" activeClassName="active" to="/">Home</NavLink>
          </li>                                                 #3
          <li className="nav-item">
            <NavLink exact className="nav-link" activeClassName="active" to="/articles">Articles</NavLink>
          </li>
        </ul>
      <div>
    </nav>
  );
}
```
1) The Navigation component returns JSX that ultimately renders the nav bar using the Bootstrap classes we provide here.
2 & 3) The React Router NavLink component is a subset of a Link component that we'll use shortly.  
It provides the activeClassName property to style the link differently when it's active.  
The other thing to note is the "exact" attribute, which is the shorthand for "exact=true."  
That means the route has to be the exact route provided with the "to" attribute. The default is that it just contains the route provided, so the "/" route by default would include any route that contains "/", which is all routes.  
So we need the *exact* attribute here.

**The Main component:**
```javascript
function Main() {                                                      #1
  return(
    <Switch>                                                           #2
      <Route exact path="/" component={Home} />                        #3
      <Route exact path="/articles" component={ArticleList} />
      <Route exact path="/articles/new" component={ArticleAdd} />
      <Route exact path="/articles/:_id" component={ArticleInfo} />
      <Route exact path="/articles/:_id/edit" component={ArticleEdit} />
    </Switch>
  )
);
```
1) The *Main* component is where we insert all our Route elements.
2) The React Router switch statement works like a JavaScript switch statement. It checks each statement below it in order until there is a match.
3) Route is a React Router element that takes as attributes the path and the component to call if there is a match. The "exact" attribute requires the match be exact.

*Note that throughout this project I will be using the function declaration syntax rather than function expressions or arrow functions, unless there is a specific reason those should be used. But if you prefer arrow function syntax feel free to change it.*
___
**ArticleList component**
Now it's time to do our first API call! We'll go to the server to retrieve a list of all the articles in the database.  
In our file structure setup we created the ArticleList.js file.  
Populate it with the ArticleList component below and save it.
```javascript
// src/component/articles/Articlelist.jsx

import React, { useState, useEffect } from 'react';
import  axios  from 'axios';
import { Link } from 'react-router-dom';

function ArticleList() {
  const [articles, setArticles] = useState([])

  useEffect(function() {
    async function getArticles() {
      try {
        const response = await axios.get("/api/articles");
        setArticles(response.data);
      } catch(error) {
        console.log('error', error);
      }
    }        
    getArticles();
  }, []);

  return (
    <div>
      <h2>
        Articles
        <Link to="/articles/new" className="btn btn-primary float-right">Create Article</Link> 
      </h2>
      <hr/>
      {articles.map((article) => {
        return(
          <div key={article._id}>
            <h4><Link to={`/articles/${article._id}`}>{article.title}</Link></h4>
            <small>_id: {article._id}</small>
            <hr/>
          </div>
        )     
      })}
    </div>
  )
}

export default ArticleList;
```
Let's see if it works. If you have a local MongoDB database make sure that is running, or start it in a separate terminal window (any directory will work):
```javascript
mongod
```
To start the API server in a separate terminal window go to the project's root directory:
```javascript
nodemon
```
Now if you go to the browser and click on the Articles link you should see a list of articles from the database. This corresponds with the JSON view at `http://localhost:3001/api/articles` which you can view in a separate browser tab.  
The connection to the API is working! Also, notice that we are running two separate servers on two different ports:
- For the back-end API app
- For the React front-end app.

Time to break it down starting with...

**The imports:**
```javascript
import React, { useState, useEffect } from 'react';  #1
import { get } from 'axios';                         #2
import { Link } from 'react-router-dom';             #3
```
1) React components require the React library. Additionally, import useState and useEffect to use the State and Effect hooks. Read Hooks at a Glance for a quick summary. 2) To access data from the API we'll make an AJAX get request using the Axios package we added earlier.
3) We will include links to the the individual Article pages and to the New Article form, so import the Link component from the react-router-dom module.

**Declare the ArticleList functional component:**
```javascript
function ArticleList() {
```
UseState Hook:
```javascript
  const [articles, setArticles] = useState([]) 
```
Set the initial state of our component to an empty array with the useState hook. UseState is a two element array that contains the current state as the first element and a function to update it as the second.  
Here we're assigning the (const) variable "articles" to the current state value, and "setArticles" to the update function.

**UseEffect Hook:**
```javascript
  useEffect(function() {                                #1          
    async function getArticles() {                      #2
      try {
        const response = await get("/api/articles");    #3
        setArticles(response.data);                     #4
      } catch(error) {
        console.log('error', error);
      }
    }        
    getArticles();
  }, []);                                               #5
```                                       
1) Place your asynchronous code here such as your API call. Code in the useEffect method runs after the initial render of the component and changes the state of the component.
2) The API call is asynchronous since it sends a get request to the API and waits for a response from the server.
3) We're using the Axios library to make an AJAX get request and convert the JSON response to a JavaScript object. We aren't including the domain part of the URL -- `http://localhost:3001` *-- because we added it as a proxy in the package.json file.*
4) Call the *setArticles* method to change the articles state, passing in the response object we got back from the API (which is an array of article objects). The React useState hook will change the articles state to this object.
5) The useEffect hook takes a second argument that instructs React to rerun the effect. We only want to run the effect once to get the list of articles so just set it to an empty array.

**Return statement:**
```javascript
  return (                                          #1
    <div>
      {articles.map((article) => {                  #2
        return(
          <div key={article._id}>                   #3
            <h2><Link to={`/articles/${article._id}`}>{article.title}</Link></h2>         #4
            <small>{article._id}</small>
            <hr/>
          </div>
        )     
      })}
      <Link to="/articles/new" className="btn btn-outline-primary">Create Article</Link>  #5
    </div>
  )
```
1) React components return JSX which is converted to HTML.  
2) Access the articles state object which is an array of the article objects we got from the API. The JavaScript map method iterates though the array transforming each item based on the function provided and returning a new transformed array.
3) React requires that we assign a unique key to each item when iterating though a list, so we are assigning the article id attribute.
4) Here we transform the article objects into JSX that puts the article title into a link, displays the article id, and adds a horizontal line at the bottom.
5) At the end we include a link to the new articles route.
___
**Chrome Developer Tools**
If you want to get a better understanding of state then make use of logging. Add 
```javascript
console.log(n, articles);
``` 
statements to your component with n being sequential numbers. 
- Refresh your browser
- open Chrome Developer Tools - Inspect and go to the Console tab.  
There you can see the console logs of the data pulled and the order the code is executed.
___
**ArticleInfo component**
On to the ArticleInfo component which corresponds to our API's Get /api/articles endpoint.  
Populate the file with the below and save it.
```javascript
// src/components/articles/ArticleInfo.js

import React, { useState, useEffect } from "react";
import axios from 'axios';                               #1
import { Link } from 'react-router-dom';

function ArticleInfo(props) {
  const [article, setArticle] = useState({});            #2

  useEffect(function() {                                 #3a
    async function getArticle() {
      try {
        const response = await axios.get(`/api/articles/${props.match.params._id}`); #3b
        setArticle(response.data);                       #3c
      } catch(error) {
        console.log('error', error);
      }
    }
    getArticle();    
  }, [props]);                                           #3d

  async function handleDelete() {                        #4a
    try {
      await axios.delete(`/api/articles/${props.match.params._id}`); #4b
      props.history.push("/articles");                   #4c
    } catch(error) {
      console.error(error);
    }
  }

  return (                                               #5
    <div>
      <h2>{article.title}</h2>
      <small>_id: {article._id}</small>
      <p>{article.content}</p>
      <div className="btn-group">
        <Link to={`/articles/${article._id}/edit`} className="btn btn-primary">Edit</Link> 
        <button onClick={handleDelete} className="btn btn-danger">Delete</button> 
        <Link to="/articles" className="btn btn-secondary">Close</Link>
      </div>
      <hr/>
    </div>
  );
};

export default ArticleInfo;
```
Now test it out in the browser. From the Articles page, if you click on an article title it should take you to the article page.  
Click the cancel button and it should take you back to the Article List page.  
Select another article and this time click delete.  
Poof, it's gone if everything is working correctly, which means you have both read and write access to the API. You should be back to the articles list page minus one article.

Let's break down the code.
1) The imports are the same as for ArticleList. The only thing to note is we are importing the whole Axios library rather than just the specific methods we are using (get and delete). That's because "delete" is a JavaScript reserved word. Since we're importing the whole Axios library, we call the specific methods with axios.get and axios.delete.
2) Call the useState hook and set the value to a variable called article with an initial state of an empty object {}. Assign the update function to the variable name setArticle. 
3a) The useEffect hook is similar to ArticleList.
3b) But this time we when we make our GET request to the API we need to send the article id. So now the props object comes into play. If you look in the Chrome Developer Tools "React" tab and search on ArticleList you'll see the props and state objects in the pane to the right. Props contains three objects, one of which is called Match. Match contains the path (articles/:_id), the url (articles/id), and another object called params. Params contains a single path param of :_id. So to get the article id we need to chain this all together with this.props.match.params._id.
3c) When the response to the AJAX request comes back we will use the setArticle method to assign response data from the API to the article object in the component's state.
3d) Adding props to the second argument of the useEffect hook instructs React to re-run the effect if props changes.

If you prefer to use the promise.then syntax rather than async/await, then the useEffect hook would look something like this:
```javascript
  useEffect(function() {
    axios.get(`/api/articles/${props.match.params._id}`)
      .then(function(response) {
        setArticle(response.data);
      })
      .catch(function (error) {
        console.log('error', error);
      });
  }, [props]);
  ```
4a) When the user clicks the "Delete" button, the onClick event calls the handleDelete handler function.
4b) We use the Axios library to send a delete request to the provided URL.
4c) When we get a response from the delete request we will redirect to the articles page using props.history.push("/articles").  
We saw earlier in Chrome Dev Tools that the props contained three objects: history, location, and match.  
The history object contains a stack of the URL locations visited with the most recent on top, including the current path at the very top.  
"Push" is a JavaScript method that adds an item to the end of an array, so pushing the articles route to the end (top) of the history stack will make that route the current location.

The promises.then syntax for the handleDelete function would look something like this:
```javascript
  function handleDelete() {
    axios.delete(`/api/articles/${props.match.params._id}`)
      .then(function() { props.history.push("/articles") })
      .catch(function(error) { console.log('error', error); });
  }
```
5) The component returns the JSX which is converted to HTML. It includes the article data and buttons for edit, delete and back.
___
**ArticleAdd component**
We've covered Read and Delete, how about Create? Populate the *ArticleAdd.jsx* file with the below.
```javascript
//src/components/articles/ArticleAdd.js

import React, { useState } from "react";                #1a
import { post } from 'axios';                           #1b

function ArticleAdd(props) {
  const initialState = { title: '', content: '' }
  const [article, setArticle] = useState(initialState)  #2

  function handleChange(event) {                        #3
    setArticle({...article, [event.target.name]: event.target.value})
  }

  function handleSubmit(event) {                        #4a
    event.preventDefault();                             #4b
    if(!article.title || !article.content ) return      #4c
    async function postArticle() {
      try {
        const response = await post('/api/articles', article); #4d
        props.history.push(`/articles/${response.data._id}`);  #4e
      } catch(error) {
        console.log('error', error);
      }
    }
    postArticle();
  }

  function handleCancel() {
    props.history.push("/articles");
  }

  return (                                              #5
    <div>
      <h1>Create Article</h1>
      <hr/>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Title</label>
          <input name="title" type="text" value={article.title} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Content</label>
          <textarea name="content" rows="5" value={article.content} onChange={handleChange} className="form-control" />
        </div>
        <div className="btn-group">
          <input type="submit" value="Submit" className="btn btn-primary" />
          <button type="button" onClick={handleCancel} className="btn btn-secondary">Cancel</button>
        </div>
      </form>
    </div>
  );
}

export default ArticleAdd;
```
Test it out to make sure it works. From the Articles List page click on the Create Article button, there should be a form.  
- First hit the cancel button to make sure you go back to the Articles list page. 
- Click Create Article again and this time write an article. 
- Write about anything you want. 
- Then click create and you should be taken to your new article info page. 
Nice! But, how did we get here?

- 1) In our React imports we will only be using the useState hook. For our Axios imports we'll be using a post request.
- 2) Our *useState* hook will create a state named article with initial state set to an object with title and content properties set to empty strings. We'll also set the function for updating state to variable "setArticle".
- 3) Every time a user types a character in a form input field the onChange property calls the handleChange handler function passing the event object as an implicit argument.  
The event object includes the target (i.e., the form field element) which has attributes for field name and value.  
The handleChange function in turn calls setArticle which updates the article state with the new value. You need to include the ...article spread operator so that the new character is added to the existing article value, otherwise it will just overwrite it. You can see the process in action by adding
```javascript
console.log(event.target); 
```
to the *handleChange* function then look at the console after typing in a character.  
You can also look at the React tab in the console after drilling down to the *ArticleAdd* component and you will see State update after every key is pressed.
- 4a) When the user clicks the form's submit button, it triggers the onClick event which calls the handleSubmit handler function.
- 4b) Normally when an HTML form is submitted a new page is called. Since we are sending the data via AJAX and don't want to be sent to a new page we need add preventDefault().
- 4c) We add a conditional that checks if either of the form fields are empty. If they are we stop the function by returning nothing. 4d) We'll sent a POST request to the API endpoint sending the current state.
- 4e) Then using ES6 promises, when the new article is returned we'll use the response.data object to get the id so we can redirect to the correct ArticleInfo route.
If you prefer to use the promises.then syntax it would look something like this:
```javascript
    axios.post('/api/articles', article)
      .then(function(response) {
        props.history.push(`/articles/${response.data._id}`);
      })
      .catch(function(error) { console.log('error', error) });    
```
- 5) Our return statement is the JSX for our form. Each form field element has properties for name, value (set to the article state) and onClick set to a handler function. The form element has an onSubmit property set to a handler function that is triggered when the user clicks the submit button.
___
**ArticleEdit component**
Only one more component to go. Here's the code.
```javascript
// src/components/articles/ArticleEdit.js

import React, { useState, useEffect } from "react";
import { get, patch } from 'axios';

function ArticleEdit(props) {

  const initialState = { title: '', content: '' }
  const [article, setArticle] = useState(initialState)

  useEffect(function() {
    async function getArticle() {
      try {
        const response = await get(`/api/articles/${props.match.params._id}`);
        setArticle(response.data);        
      } catch(error) {
        console.log(error);
      }
    }
    getArticle();    
  }, [props]);

  function handleSubmit(event) {
    event.preventDefault();
    async function updateArticle() {
      try {
        await patch(`/api/articles/${article._id}`, article);
        props.history.push(`/articles/${article._id}`);        
      } catch(error) {
        console.log(error);
      }
    }
    updateArticle();
  }

  function handleChange(event) {
    setArticle({...article, [event.target.name]: event.target.value})
  }

  function handleCancel() {
    props.history.push(`/articles/${article._id}`);
  }

  return (
    <div>
      <h1>Edit {article.title}</h1>
      <hr/>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Title</label>
          <input type="text" name="title" value={article.title} onChange={handleChange} className="form-control" />
        </div>
        <div className="form-group">
          <label>Content</label>
          <textarea name="content" rows="5" value={article.content} onChange={handleChange} className="form-control" />
        </div>
        <div className="btn-group">
          <button type="submit" className="btn btn-primary">Update</button>
          <button type="button" onClick={handleCancel} className="btn btn-secondary">Cancel</button>
        </div>
      </form>
    </div>
  );
}

export default ArticleEdit;
```
Save it, then edit an article to make sure it works.

This component is essentially a combination of the ArticleInfo and ArticleAdd components. So it would be a good exercise for you to go through the lines of code and make sure you understand what they are doing.
**This completes the React portion of this app!**
___
**Run the API and React Client with one command**
Right now we need separate terminal windows open to run our back end API server (port 3001) and our front end React app (port 3000), Not to mention our MongoDB server.  
For convenience we can run our API and React apps with one command using the Concurrently package.  
Make sure you are in the project's root directory (not in the client folder).  
Using the --dev flag installs it as a development environment dependency.
```javascript
npm install concurrently --save-dev
```
Open the *package.json* file in the project's root directory (not the one in the client folder) and add the highlighted script below.  
*Note that you need to add a comma after the start script.*
```javascript
//package.json
  ...
  "scripts": {
    "start": "node server.js",
    "dev": "concurrently \"nodemon server.js\" \"cd client && npm run start\""
  },
  ...
  "devDependencies": {
    "concurrently": "^4.1.1"
  },
```
This will run the nodemon command on the API application starting the server on port 3001. 
 Then it will cd to the client directory and run the start command which will run the React app on port 3000.  
 To execute this script, make sure you stop both servers first, then from the project's root directory run:
```javascript
npm run dev
```
This should start both servers and open the React app in your browser.
___
**Deployment**
*Dotenv Package and environmental variables*
Heroku requires you to use a cloud database platform for MongoDB. MongoDB's Atlas cloud service requires a user name and password as part of the URL.  
To keep these private you should use environmental variables so that they are not explicitly in your application's code.  
Assuming you are using Atlas for both development and production, you should add the dotenv package for your development environment if you expect to expose the file in a place like a public github repository.  
From the project's root directory:
```javascript
npm install dotenv
```
In Node, environment variables can be accessed on the process.env object. The dotenv middleware looks for a file called .env and loads it's contents into the process.env variable for use in your code.
Create a *.env* file in the project's root directory:
```javascript
touch .env
```
Add environmental variables on new lines in the form of NAME=VALUE.  
By convention, use names in all upper case with words separated by underscores like MONGODB_URI.  
Add your MongoDB Atlas database link since it contains your user name and password. Something like this:
```javascript
// .env

MONGODB_URI=mongodb+srv://user:password@cluster-number.mongodb.net/test?retryWrites=true&w=majority
```
We are only using the .env file in our development environment. When you deploy your app on Heroku you need to add this as an environmental variable on Heroku at that time.
___
**Server.js Update**
Update the server.js file with changes related to Heroku highlighted and explained below.
```javascript
// server.js

const express = require('express');
const mongoose = require('mongoose');
const router = require('./routes/index');
+ const path = require('path');               #1  
+ const PORT = process.env.PORT || 3001;      #2
+ require('dotenv').config();                 #3

const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use('/api', router);

+ mongoose.connect(process.env.MONGODB_URI, { useNewUrlParser: true }); #4
mongoose.connection.once('open', () => {
  console.log('Connected to the Database.');
});
mongoose.connection.on('error', err => {
  console.log('Mongoose Connection Error : ' + err);
});

+ if (process.env.NODE_ENV === 'production') {      #5     
+   app.use(express.static('client/build'));
+
+   app.get('*', (req, res) => {
+     res.sendFile(path.resolve(__dirname, 'client', 'build', 'index.html'));
+   });
+ }

app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}.`);
});
```
- 1) Path is a module within Node so we don't install it with npm. The path module provides utilities for working with file and directory paths and is needed to work on Heroku.
- 2) Heroku will assign a port via the PORT environmental variable. We'll use the or operator || to assign that as the port or 3001 if it is null (i.e., if we are in the dev environment).
- 3) Require and configure dotenv middleware.
- 4) Connect to the database URI taken from the environmental variable.
You could use a local MongoDB instance for your development environment and use the cloud for production.  
If you take that route then you would would set it up like this:
```javascript
const LOCAL_DB = "mongodb://127.0.0.1:27017/my_local_db";
mongoose.connect(process.env.MONGODB_URI || LOCAL_DB, { useNewUrlParser: true });
```
- 5) When you deploy your app to Heroku, Heroku will run the build command on the React app and move the finished version to the build folder.  
This conditional statement tells Heroku that your React files will be in the client/build folder and URL requests will go to the *client/build/index.html* file where your SPA React app is served from.
___
**Package.json**
The React app in development is not optimized. We need to run the npm build command for React to minify all your React code and put it into a folder called build.  
But actually we'll instruct Heroku to do that for you when you deploy.  
Add a script to the package.json file in the project root directory with property heroku-postbuild (Has a "+" before).  
Heroku will run that script after it builds your app.  
The script :
- cds into the client directory
- runs npm install to install the React packages
- and npm run build to build the optimized version in the build folder. 
Your finished package.json file should look something like the below.
```javascript
//package.json

{
  "name": "mern-blog",
  "version": "1.0.0",
  "description": "Web app built with Node.js, Express, MongoDB, and React",
  "main": "server.js",
  "dependencies": {
    "dotenv": "^8.0.0",
    "express": "^4.17.1",
    "mongoose": "^5.6.3"
  },
  "devDependencies": {
    "concurrently": "^4.1.1"
  },
  "scripts": {
  +  "start": "node server.js",
    "dev": "concurrently \"nodemon server.js\" \"cd client && npm run start\"",
  +  "heroku-postbuild": "cd client && npm install && npm run build"
  },
  "keywords": [],
  "author": "",
  "license": "MIT"
}
```
Also note the "start" script. We used that in development to start the Express server with npm start.  
But we ignored it with our npm run dev script, using nodemon instead.  
But for production this script will come in handy since we want Heroku to run our server file with node once it's built.

Once Heroku is done building the app it will look for a file called *Procfile* for instructions on how to start the app.  
So we could create a Procfile and add one line: 
```javascript
web: npm run start
```
If Heroku doesn't find a Procfile it will run the command npm start.  
So that's why we need the start script to run node server.js.
___
Git repository
We will use git to push our app to Heroku.

When we generated our React app with create-react-app, it generated a git repository and created a gitignore file in the client folder.  
We want one git repository in our root directory for both our API and our React client.  
So if you haven't already, delete the .git repository in the client folder with the following code inside the client:
```javascript
rm -rf .git
```
The gitignore file is fine where it is. Git will honor multiple gitignore files so we'll just add another one at the root directory.

Now in our project's root directory initate a new git repository and create a .gitignore file.
```javascript
$ git init
$ touch .gitignore
```
Add the *.env* file and the *node_modules* folders to our new gitignore file.
```javascript
// .gitignore

node_modules
.env
```
___
**Set up Heroku**
First create an account on their [website](https://signup.heroku.com/identity)
Then download and install the Heroku Command Line Interface on your computer [here](https://devcenter.heroku.com/articles/heroku-cli).

From the CLI, create a new Heroku App:
```javascript
heroku create appname
```
If your appname is already taken you'll have to pick another one. Or leave off the appname and let Heroku generate a super awesome one for you.  
If you want to connect your project to a real domain name you can configure Heroku to use that [here](https://devcenter.heroku.com/articles/custom-domains).

This will automatically set heroku as your git remote repository. Run the below command to confirm.  
It will list the project's remote git repositories (if any) and their urls.
```javascript
git remote -v
```
Set the MongoDB uri as an environmental variable (no quotes):
```javascript
heroku config:set MONGODB_URI=Your db cloud link goes here
```
___
**Deploy your app**
Create your initial git commit:
```javascript
$ git add -A
$ git commit -m "Initial commit"
```
Then push the code out to heroku:
```javascript
git push heroku master
```
It will take a few minutes to load up. When it's finished launch the app.  
The below command will open the app in your browser:
```javascript
heroku open
```
If everything went well you have a working MERN application up and running on Heroku!

I know, I know, the application doesn't look good, well, thats where you come in!
Style this project, This is important because its a big and impressive project, but without good styling it does not look like it.

**Good luck with the styling!**