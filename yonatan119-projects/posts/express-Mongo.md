---
layout: post
title: Node.js Express MongoDB
published: 2021-04-03T13:30:34+00:00
author: yonatan119
tags: node, js, javascript, express, mongodb
---

# **Getting Started:**
- Make sure you have Node.js installed
- Create a new directory called "ProductsApp".
- Inside the newly created directory, execute the following command in the terminal:
```javascript
npm init
```
We already learned what this does, but lets go back to it.
"npm init" results in creating a package.json file.  
The package.json file is used to manage the locally installed npm packages.  
It also includes the meta data about the project such as name and version number.
___
**Installing our packages**
Lets install the packages we need for this project, you guessed it.
- ExpressJS
- mongoose
- body-parser: package that can be used to handle JSON requests.  
We can install the above mentioned packages via typing the following command in the command line. Just make sure that you are in the project directory before executing the below command.
```javascript
npm install --save express body-parser mongoose
```
___
**Initializing the Server:**
Create a new file named **app.js** directly inside the ProductsApp directory
Open the newly created file named **app.js** and require all the dependencies we previously installed (ExpressJS and body-parser ) -we will talk about mongoose later-
```javascript
// app.js
const express = require('express');
const bodyParser = require('body-parser');
// initialize our express app
const app = express();
```
Next step would be dedicating a port number and telling our express app to listen to that port.
```javascript
let port = 1234;
app.listen(port, () => {
    console.log('Server is up and running on port numner ' + port);
});
```
Now, we should be able to test our server using the following command in the terminal
```javascript
node app.js
```
Now we made sure that we are having a server that is up and running. However, this server does nothing! Let’s work on that and make our app more complex.
___
**Organizing our application:**
We will be working with a design pattern called MVC. Its a neat way of separating parts of our app and grouping them based on their functionality and role.
- M stands for models, this will include all the code for our database models (which in this case will be Products).
- V stands for the views or the layout. We will not cover the views in this tutorial as we are designing an API.
- C stands for controllers which is the logic of how the app handles the incoming requests and outgoing responses.  
There will be one more thing, called Routes, Routes are our guide, they tell the client (browser/mobile app) to go to which Controller once a specific url/path is requested.
Inside the ProductsApp directory, I will create the following four subdirectories(files)
- controllers
- models
- routes
- views
**App structure**
Now we have a server that is ready to handle our requests and some directories that would have our code.
**Model**
Let’s start by defining our model. Create a new file in the models directory and name it **product.model.js**
```javascript
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

let ProductSchema = new Schema({
    name: {type: String, required: true, max: 100},
    price: {type: Number, required: true},
});
// Export the model
module.exports = mongoose.model('Product', ProductSchema);
```
First we started with requiring mongoose (An npm package to make using mongo easier) and then we define the schema for our model.  
Last thing is exporting the model so it can be used by other files in our project.
M model - Check.
___
**Routes:**
Let’s start imagining how the urls will be like and design our routes.  
Inside the routes directory, create a **product.route.js** file. This is the file that will include the routes of the products. Some developers prefer to have all the routes in a single file (**routes.js**) for example, but when your app grows this is less useful.  
so let’s structure it the right way from the beginning.
```javascript
const express = require('express');
const router = express.Router();

// Require the controllers WHICH WE DID NOT CREATE YET!!
const product_controller = require('../controllers/product.controller');


// a simple test url to check that all of our files are communicating correctly.
router.get('/test', product_controller.test);
module.exports = router;
```
___
**Controllers:**
Next step is to implement the controllers we referenced in the routes.
go to our controllers directory and create a new js file named **product.controller.js** which will be the placeholder for our controllers.

```javascript
const Product = require('../models/product.model');

exports.test = function (req, res) {
    res.send('Greetings from the Test controller!');
};
```
Last step before trying out our first route is to add the route class to the **app.js**
```javascript
//app.js
const express = require('express');
const bodyParser = require('body-parser');
const product = require('./routes/product.route'); // Imports routes for the products
const app = express();
app.use('/products', product);
let port = 1234;
app.listen(port, () => {
    console.log(`Server is up and running on port number ${port}`);
});
```

Now head to your browser and try the following link: http://localhost:1234/products/test
to validate that our test route is working.
Now we have our very first route working. Let’s get the rest working.
___
**Postman:**
We learned about postman in the databases lesson but lets go more into it.
Postman is a very powerful HTTP client that is used for testing, documenting and the development of APIs.  
We will be using Postman here to test our endpoints that we will be implementing through out the rest of this project.  
But first, let’s get familiar with Postman using our ‘/test’ route.
- in case you didn't install postman in the previous lesson [do it now](https://www.getpostman.com/).
- Open the app, make sure it’s a GET request and type the following url ‘localhost:1234/products/test’. Just make sure that your server is still running on the port number 1234. You should be able to see ‘Greetings from Test controller’ when going on the ‘Preview’ mode in Postman.
![](https://miro.medium.com/max/1500/1*G3GtxTFaTCGB_tCrdBNwVA.png)
___
**The Database:**
Our database will be hosted remotely on mLab.  
mLab offers a nice free tier that we can use to test our application.  
Let’s set it up.
- Head to mLab’s website.
https://mlab.com/
![](https://miro.medium.com/max/1050/1*fKof5SZbsAxjt7QdUhcEPg.png)
- Click on ‘Create New’ from the above image.
![](https://miro.medium.com/max/1050/1*gTg6df7dkbtS4zm9_02K_w.png)
- Select the Sandbox Plan Type and click on ‘Continue’.
- Type in the database name, something like "productsproject".
- Once everything is ready, just click on ‘Submit Order’
- Next step would be creating a user to be able to access the database. Simply click on ‘Add database user.
- Last step would be entering the data from the database user you are creating. In this tutorial, for the username we will be using "someuser" and for the password we will be using "abcd1234".  
Now we have a database in the cloud that is ready to be accessed.
___
**Connecting our app to the remote Database:**
We need to inform our app that it should be communicating with the database we have just created on mLab.
Remember the "mongoose" package we installed before? Now is the right time to use it.
All we have to do is head to our **app.js** file and paste the following code in it.  
*Just remember to update the dev_db_url variable with the connection string of your remote database on mLab. Remote database string consists of your database username and password, separated by a ‘:’ and then the URL to your database instance on mLab and then the database name.*
```javascript
// Set up mongoose connection
const mongoose = require('mongoose');
let dev_db_url = 'mongodb://someuser:abcd1234@ds123619.mlab.com:23619/productsproject';
let mongoDB = process.env.MONGODB_URI || dev_db_url;
mongoose.connect(mongoDB);
mongoose.Promise = global.Promise;
let db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
```
___
**Body Parser**
Last configuration thing we need for our **app.js** is using bodyParser.  
Body Parser is an npm package that is used to parse the incoming request bodies in a middleware.
In you **app.js** file, add the following couple of lines.
```javascript
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
```
Here is how our full **app.js** file looks like
```javascript
// app.js

const express = require('express');
const bodyParser = require('body-parser');

const product = require('./routes/product.route'); // Imports routes for the products
const app = express();

// Set up mongoose connection
const mongoose = require('mongoose');
let dev_db_url = 'mongodb://someuser:abcd1234@ds123619.mlab.com:23619/productsproject';
const mongoDB = process.env.MONGODB_URI || dev_db_url;
mongoose.connect(mongoDB);
mongoose.Promise = global.Promise;
const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));
app.use('/products', product);

let port = 1234;

app.listen(port, () => {
    console.log('Server is up and running on port numner ' + port);
});
```
By now our **app.js** file is finalized and you are aware of the usage of each and every line of code in the file.
___
**Implementing the endpoints**

**CREATE**
*The first task in our CRUD task is to create a new product.*   
Let’s start by defining our route first.  
Head to routes and start designing the expected path that the browser would hit and the controller that would be responsible for handling that request.
```javascript
// routes/products.route.js
...
router.post('/create', product_controller.product_create);
```
Now let’s write the product_create controller in our controller file. Head to *controllers/product.controller.js* and paste the following code.
```javascript
// controllers/products.js
exports.product_create = function (req, res) {
    let product = new Product(
        {
            name: req.body.name,
            price: req.body.price
        }
    );

    product.save(function (err) {
        if (err) {
            return next(err);
        }
        res.send('Product Created successfully')
    })
};
```
The function simply creates a new product using the data coming from a POST request and saves it to our database.
Our last step would be validating that we can easily create a new product.  
Let’s open Postman and send a POST request to the following url *"localhost:1234/products/create"* and specify the POST data:
- name: apple
- price: 15 
Also make sure that you choose x-www-form-urlencoded in the Body tab in Postman as specified in the image.
![](https://miro.medium.com/max/1500/1*-5zfiZ1ACxtWwITStWGc4A.png)
We can see that the response is ‘Product Created successfully, this means that the router and the controller are working correctly.  
To double check that an ‘Apple’ product was created, let’s check our database so head to mLab and go to the collections in your database.  
We can see that a new collection was created named ‘products’ and has one document.
___
**Read**
The second task in our CRUD app is to read an existing product, let’s do the route.
```javascript
// routes/products.route.js
...
router.get('/:id', product_controller.product_details);
Now let’s write the product_details controller in our controller file. Head to controllers/product.controller.js and paste the following code.
// controllers/products.controller.js
exports.product_details = function (req, res) {
    Product.findById(req.params.id, function (err, product) {
        if (err) return next(err);
        res.send(product);
    })
};
```
This function simply reads an existing product from the product id being sent in the request. 

Now let’s head to Postman and try-out our new endpoint. Call the following url *"localhost:1234/products/PRODUCT_ID"*.  

PRODUCT_ID is the id of the object we’ve created in the previous endpoint and you should get this from your database.
We got a response containing all the info of that specific product, you can see that it is called "apple" and it’s price is "15".
___
**Update**
The third task in our CRUD app is to update an existing product, let’s create the route.
```javascript
// routes/products.route.js
...
router.put('/:id/update', product_controller.product_update);
```
Now let’s write the *product_details* controller in our controller file, head to *controllers/product.**controller.js*** and paste the following code.
```javascript
// controllers/products.controller.js
...
exports.product_update = function (req, res) {
    Product.findByIdAndUpdate(req.params.id, {$set: req.body}, function (err, product) {
        if (err) return next(err);
        res.send('Product udpated.');
    });
};
```
The function simply finds an existing product using its id that was sent in the request.

Now let’s head to Postman and try-out our new endpoint. Call the following URL *"localhost:1234/products/**PRODUCT_ID**/update"*

PRODUCT_ID is the id of the object we’ve created in the previous endpoint and you should get this from your database.
Lets update the product name to ‘apple2’ and afterwards we can see a response saying ‘Product updated.’
We can also check the database to see if the database document was updated successfully or not.  
___
**Delete**
The last task in our CRUD app is to delete an existing product. Let’s do the route.
```javascript
// routes/products.route.js
...
router.delete('/:id/delete', product_controller.product_delete);
```
Now let’s write the product_delete controller in our controller file. Head to *controllers/**products.js*** and paste the following code.
```javascript
// controllers/products.controller.js
exports.product_delete = function (req, res) {
    Product.findByIdAndRemove(req.params.id, function (err) {
        if (err) return next(err);
        res.send('Deleted successfully!');
    })
};
```
The function simply deletes an existing product.

Now let’s head to Postman and try-out our new endpoint. Call the following URL *"localhost:1234/products/**PRODUCT_ID**/delete"*

PRODUCT_ID is the id of the object we’ve created in the previous endpoint. You should get this from your database.

We get a success message stating ‘Deleted successfully’ in the body of our response.
___
Done 🎉 🎉
By now, we are done with creating a full API which does the four operations (CRUD)

***We did this project together, but do not be afraid if this was easy for you, which makes sense since we did it together. We are only setting grounds for building MERN applications once we learn REACT, in the next lesson. cant wait!*** 