---
layout: post
title: Callbacks Promises and Async
published: 2021-04-27T12:30:34+00:00
author: yonatanBenezra
tags: callbacks, promises, async
---
# Callbacks, Promises, and Async

- **Synchronous** operations in JavaScript entails having each step of an operation waits for the previous step to execute completely.   
This means no matter how long a previous process takes, subsquent process won't kick off until the previous is completed.   
- **Asynchronous** operations, on the other hand, defers operations.   
Any process that takes a lot of time to process is usually run alongside other synchronous operation and completes in the future.
___
**Asynchronous Operations**
Operations in JavaScript are traditionally synchronous and execute from top to bottom.   
For instance, a farming operation that logs farming process to the console:
```javascript
// JAVASCRIPT

console.log("Plant corn");
console.log("Water plant");
console.log("Add fertilizer");
```
If we run the code above, we have the following logged in the console:
```javascript
// BASH

Plant corn
Water plant
Add fertilizer
```
Now let's change that a bit so that watering the farm take longer than planting and fertilizing:
```javascript
// JAVASCRIPT

console.log("Plant maize");

setTimeout(function() {
  console.log("Water plant")
},3000);

console.log("Add fertilizer");
```
We get the following in the console:
```javascript
// BASH

    Plant Maize
    Add fertilizer
    Water plant
```

Why? The **setTimeout** function makes the operation asynchronous by deferring plant watering to occur after 3 seconds.   
The whole operation doesn’t pause for 3 seconds so it can log “Water plant”.    
Rather, the system goes ahead to apply fertilizers and then water plant after 3 seconds.
___
**Functions are First-Class Objects**
It's important to keep in mind before going through the rest of these lessons that JavaScript Functions are first-class objects in and as such can functions have the ability to:
- Be assigned to variables (and treated as a value)
- Have other functions in them
- Return other functions to be called later
___
**Callback Functions**
When a function simply accepts another function as an argument, this contained function is known as a callback function.   
Using callback functions is a core functional programming concept, and you can find them in most JavaScript code.   
Either in simple functions like **setInterval**, event listening or when making API calls.
Callback functions are written like so:
```javascript
setInterval(function() {
  console.log('hello!');
}, 1000);
```
setInterval accepts a callback function as its first parameter and also a time interval.   
Another example using .map();
```javascript
const list    = ['man', 'woman', 'child']

// create a new array
// loop over the array and map the data to new content
const newList = list.map(function(val) {
  return val + " kind";
});

// newList = ['man kind', 'woman kind', 'child kind']
```
In the example above, we used the **.map()** method to iterate through the array list, the method accepts a callback function which states how each element of the array will be manipulated.   
Callback functions can also accept arguments as well.
___
**Naming Callback functions**
Callback functions can be named or be anonymous functions.   
In our first examples, we used anonymous callback functions.   
Let’s look at a named callback function:
```javascript
function greeting(name) {
  console.log(`Hello ${name}, welcome to Presentense!`);
}
```
The above function is assigned a name **greeting** and has an argument of **name**. We're also using an ES6 template string. Let’s use this function as a callback function.
```javascript
function introduction(firstName, lastName, callback) {
  const fullName = `${firstName} ${lastName}`;

  callback(fullName);
}

introduction('Chris','Nwamba', greeting); // Hello Chris Nwamba, welcome to Presentense!
```
Notice the usage of the callback? The succeeding brackets, () after the function are not used when passing the function as a parameter.

*Note: The callback function is not run unless called by its containing function, it is called back, that is why the term is **call back function***

Multiple functions can be created independently and used as callback functions, these create multi-level functions.   
When this function tree created becomes too large, the code becomes incomprehensible sometimes and is not easily refactored.   
This is known as callback hell. Let’s see an example:
```javascript
// a bunch of functions are defined up here

// lets use our functions in callback hell
function setInfo(name) {
  address(myAddress) {
    officeAddress(myOfficeAddress) {
      telephoneNumber(myTelephoneNumber) {
        nextOfKin(myNextOfKin) {
          console.log('done'); //let's begin to close each function! 
        };
      };
    };
  };
}
```
We are assuming these functions have been previously defined elsewhere.   
You can see how confusing it is to pass each function as callbacks.   
Callback functions are useful for short asynchronous operations. When working with large sets, this is not considered best practice.   
Because of this challenge, Promises were introduced to simplify deferred activities.
___
**Promises**
I promise to do this whenever that is true. If it isn't true, then I won't.

This is a simple illustration of JavaScript Promises. Sounds like an IF statement? We’ll soon see a difference.

A promise is used to handle the asynchronous result of an operation.   
JavaScript is designed not to wait for an asynchrnous block of code to completely execute before other synchronous parts of the code can run.   
For instance, when making API requests to servers, we have no idea if these servers are offline or online, or how long it takes to process the server request.

With Promises, we can defer execution of a code block until an async request is completed. This way, other operations can keep running without interruption.

*Promises have three states:*

- **Pending**: This is the initial state of the Promise before an operation begins
- **Fulfilled**: This means the specified operation was completed
- **Rejected**: The operation did not complete; an error value is usually thrown
___
**Creating a Promise**
The Promise object is created using the **new** keyword and contains the promise; this is an executor function which has a resolve and a reject callback.   
As the names imply, each of these callbacks returns a value with the reject callback returning an error object.
```javascript
// JAVASCRIPT

const promise = new Promise(function(resolve, reject) {
  // promise description
})
```
Let’s create a promise:
```javascript
// JAVASCRIPT
const weather = true
const date    = new Promise(function(resolve, reject) {
  if (weather) {
    const dateDetails = {
      name:     'Cubana Restaurant',
      location: '55th Street',
      table:    5
    };

    resolve(dateDetails)
  } else {
    reject(new Error('Bad weather, so no Date'))
  }
});
```
If *weather* is true, resolve the promise returning the data *dateDetails*,   
else return an error object with data *Bad weather, so no Date*.
___
**Using Promises**
Using a promise that has been created is relatively straightforward; we chain **.then()** and **.catch(**) to our Promise like so:
```javascript
// JAVASCRIPT

date
  .then(function(done) {
    // the content from the resolve() is here
  })
  .catch(function(error) {
    // the info from the reject() is here
  });
```
Using the promise we created above, let's take this a step further:
```javascript
// JAVASCRIPT

const myDate = function() {
  date
    .then(function(done) {
      console.log('We are going on a date!')
      console.log(done)
    })
    .catch(function(error) {
        console.log(error.message)
    })
}

myDate();
```
Since the weather value is true, we call **mydate()** and our console logs read:
```javascript
// JAVASCRIPT

We are going on a date!
{
  name: 'Cubana Restaurant',
  location: '55th Street'
  table: 5
}
```

*.then()* receives a function with an argument which is the resolve value of our promise.   
*.catch* returns the reject value of our promise.

*Note: Promises are asynchronous.   
Promises in functions are placed in a micro-task queue and run when other synchronous operations complete.*
___
**Chaining Promises**
Sometimes we may need to execute two or more asynchronous operations based on the result of preceding promises.   
In this case, promises are chained.   
Still using our created promise, let’s order an uber if we are going on a date.

So we create another promise:
```javascript
// JAVASCRIPT

const orderUber = function(dateDetails) {
  return new Promise(function(resolve, reject) {
    const message = `Get me an Uber ASAP to ${dateDetails.location}, we are going on a date!`;

    resolve(message)
  });
}
```
This promise can be shortened to:
```javascript
// JAVASCRIPT

const orderUber = function(dateDetails) {
  const message = `Get me an Uber ASAP to ${dateDetails.location}, we are going on a date!`;
  return Promise.resolve(message)
} 
```
We chain this promise to our earlier *date* operation like so:
```javascript
// JAVASCRIPT

const myDate = function() {
  date
    .then(orderUber)
    .then(function(done) {
      console.log(done);
    })
    .catch(function(error) {
      console.log(error.message)
    })
}

myDate();
```
Since our weather is *true*, the output to our console is:
```javascript
// JAVASCRIPT

Get me an Uber ASAP to 55th Street, we are going on a date!
```
Once the *orderUber* promise is chained with *.then*, subsequent *.then* utilizes data from the previous one.
___
**Async and Await**
An async function is a modification to the syntax used in writing promises.   
It only makes writing promises easier.

An async function returns a promise -- if the function returns a value, the promise will be resolved with the value, but if the async function throws an error, the promise is rejected with that value. Let’s see an async function:
```javascript
// JAVASCRIPT

async function myRide() {
  return '2017 Dodge Charger';
}
```
and a different function that does the same thing but in promise format:
```javascript
// JAVASCRIPT

function yourRide() {
  return Promise.resolve('2017 Dodge Charger');
}
```
From the above statements, *myRide()* and *yourRide()* are equal and will both resolve to "2017 Dodge Charger". Also when a promise is rejected, an async function is represented like this:
```javascript
// JAVASCRIPT

function foo() {
  return Promise.reject(25)
}

// is equal to
async function() {
  throw 25;
}
```
___
**Await**
Await is only used with an **async function**.   
The await keyword is used in an async function to ensure that all promises returned in the async function are synchronized, meaning, they wait for each other.   
Await eliminates the use of callbacks in *.then()* and *.catch()*.   
In using async and await, async is prepended when returning a promise, await is prepended when calling a promise. try and catch are also used to get the rejection value of an async function. Let's see this with our date example:
```javascript
// JAVASCRIPT

async function myDate() {
  try {

    let dateDetails = await date;
    let message     = await orderUber(dateDetails);
    console.log(message);

  } catch(error) {
    console.log(error.message);
  }
}
```
Lastly we call our async function:
```javascript
// JAVASCRIPT

(async () => { 
  await myDate();
})();
```
This is an arrow function syntax.
___
**Conclusion**
Understanding the concepts of Callbacks, Promises, and Async/Await can be rather confusing, but so far we have seen how they work when carrying out asynchronous operations in JavaScript.
They come in handy a lot when making API requests and event handling. You can learn more about using [promises here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) and [async functions here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).
___