---
layout: post
title: Databases and postman
published: 2021-03-23T16:30:34+00:00
author: yonatan119
tags: mongodb, mongoose
---
# **Databases**
A database is a place to store data persistently and ideally in a secure way that is easy to access.

**relational vs. non-relational databases.**

Traditional databases (such as SQL) are known as relational, and they work with columns and rows - much like Excel does.   
Each cell holds some value - these values can be strings, numbers, booleans, dates - and that's it.  
To make it easier to understand, *relational databases cannot hold complex data like objects and arrays in JavaScript - only simple data.*

![](https://www.researchgate.net/profile/David-Moratal/publication/216554589/figure/fig1/AS:305735847170052@1449904514842/Client-Server-architecture-As-Figure-1-shows-databases-are-located-in-a-server-which.png).

On the other hand, we have non-relational databases such as MongoDB.
Non-relational databases generally store their data in more JSON-like format in which each "object" is generally known as a document and it represents some entity.  
The main difference between relational and non-relational database is the structure.  
That is why we can also call relational databases Structured and non-relational databases non-structured.
Important differences and notes:
**Structured DB**
- New entities must enter the database according to the columns available according to the defined order. 
**Non-Structured DB**
- each document doesn't have to have the same keys as other documents (though generally it should), and in non-relational DBs, we can store any type of data we want because documents have no structure.  
**All Databases**
- When we talk about adding data to our database, we say that we are inserting data.
- When we retrieve data back out of the DB, this is known as querying the data - from the word "query", which means a "question".

---

**Database Concept & Architecture**  
When you think of a database, you should think of it as entirely separate from your application.  
Your application will, of course, eventually retrieves data from the DB, but the data does not belong to the application meaning any application could access this data, if you choose to allow it.  
We could have several servers and clients, but all of them are fetching their data from the same DB.
*Often times there is one database which stores the single source of truth of our data.*  
The client accesses the DB through the server without any direct connection, In other words, the client has no idea that the DB exists. It only talks to the server, and the server will do the work of storing, retrieving, updating, and deleting data.
This is true for both relational and non-relational DBs.

---

**Installing Mongo**
Windows:

Go to [mongo's website](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/#download-mdb-edition) and follow the download instructions
* Important notes for the download:
  - Do not install MongoD as a Service
  - You will be prompted to install MongoDB Compass; this is optional
* Before running the server for the first time, we must create the directory to which the MongoDB server will write its data.
  - By default, this folder is C:\data\db
As such, go to your C:\ drive, and create a data folder.
  - Inside of data, create a db folder.
- We can now run Mongo commands from the directory where we installed MongoDB, but we would like to be able to run these commands from anywhere.  
  - If you know what it means to add the mongo path to your computer's global variables, then go ahead and do so.
  - Otherwise, see [this video](https://www.youtube.com/watch?t=141&v=ll2tY6KH8Tk&feature=youtu.be) for instructions on how to do that.
  - If you are windows 10 users see this video (Watch until 4:45 where he starts talking about mongo service)
    - Notice that the first thing we see in the video is where our Mongo files were saved.
    - Also notice that once he finishes explaining "adding the path", he talks about creating the data\db directory which we've already done.


Mac:

Since Apple updated Mac OS to Catalina, there are few steps to do. follow this article to install MongoDB correctly. note that this article is for users that have Catalina version, if you have prior version of Mac OS, use the following instruction:

- The easiest way to install MongoDB on a Mac is through Homebrew. If you don't already have Homebrew installed on your Mac by now, enter the below code into a terminal window (without the "$"): 
- $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
then after Homebrew is finished installing: 
- $ brew update
- $ brew install mongodb
Before running the server for the first time, we must create the directory to which MongoDB server will write its data. By default, this folder is \data\db on Mac. You need to create this directory as with the correct permissions so type: mkdir -p /data/db. Create those folders now.
- Ensure that user account running MongoDB has the proper directory permissions by running these commands: 
- sudo chown -R `id -un` /data/db and write your password down

**Running Mongo**
Open up a new terminal and run the following command:

```javascript
mongod
```

This splurts out a lot of text but at the end of the day starts a server running on your computer.  
You should see something like this:
```javascript
...
2019-04-06T09:13:55.130+0300 I FTDC     [initandlisten] Initializing full-time diagnostic data capture with directory '/data/db/diagnostic.data'
2019-04-06T09:13:55.132+0300 I NETWORK  [initandlisten] waiting for connections on port 27017
```

This means our MongoDB is up and running, and waiting for us to connect to it.

To connect and start writing DB operations, open a new terminal (or new tab), and run the following command:
```javascript
mongo
```
You should now be in the mongo shell, and see something like this:

```javascript
---

> 
```
Here we can write Mongo commands.
Later on we will learn about Mongoose which allows us to use mongo with less trouble, so we will not get into mongo commands but if you want to learn further go into this link [about mongo](https://www.bmc.com/blogs/mongodb-commands/)

---
**Postman**


Postman is a very useful tool for anyone working with servers.
Postman allows us to make GET, POST, PUT, DELETE requests to our heart's content, without having to set up a client at all. In fact, Postman is the client.  
So for starters, go ahead and [download Postman](https://www.getpostman.com/apps), then install it on your computer.   
Now, after you finished installing and logging in, lets say you're making a GET request to our favorite user api - we can make this request via Postman. Just enter this URL into the input, press send, and you should soon enough see the result.  
It knows to make a GET request because of the GET on the side - but we can change that, it's a drop-down!  
We  will use Postman from now on when building our servers, so brace yourself.
___
**I think we read enough without practice so lets start our first node.js express mongodb project!**