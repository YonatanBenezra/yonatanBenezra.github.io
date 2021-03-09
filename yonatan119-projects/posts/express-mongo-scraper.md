---
layout: post
title: Scraper optional project
published: 2021-04-20T14:30:34+00:00
author: yonatan119
tags: node, js, javascript, express, mongodb
---

# **Scraper**
*The next project will help us understand some more express and mongo.*

In this project we will GET and POST all the data of clothing from ZARA.
How?
- Finding Zara's API.
- create and connect a Database (MongoDB).
- parse the data we receive from Zara's API.
- Save the data to our DB.
___

How our repo should look:
- Mongodb
  - mongodb.connect.js
- httpRequest.js
- index.js

Packages you could use:
- needle
- mongodb
- 
___
**Finding Zara's API**
This project you will be mainly on your own, if you are having trouble, don't worry. one of our lessons will be on this project.
First of all, what we need to do is find the API Zara is fetching its data from.
lets go to Zara.com, open up our inspect tool and start looking.  
the first place we should look for is on the network tab.
if nothing is showing, refresh the page by clicking Ctrl+Shift+r(hard refresh).
we can see here alot of images and all kinds of requests. travel around the site and find the api for fetching clothes!
*hint: the site fetches only what is needed so try looking on pages with clothes*.
If you think you found it, send a GET request on Postman to see if you get back an object with clothes.
Did you find it? amazing!
lets open a Database!
___
**create and connect a Database (MongoDB)**
You know how to do this!
we did it together on the project "Express-mongoDB".  
if your being lazy, just go back to the lesson or use the database you created there.
___
**parse the data we receive from Zara's API.**
https://www.npmjs.com/package/needle.
Use this.
___
**Save the data to our DB.**
Use collectionName.insertMany(result...)

This is not an easy project so don't feel bad if it doesn't work easily.
If you need help, send a message.
* **Good Luck**
*There is a hint down here if you need one*



```javascript
//index.js

const needle = require("needle");
const mongodb = require("./mongodb/mongodb.connect")

const options = {
    header: {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
    }
}

async function main() {
    const mongoClient = await mongodb();
    const zaraDB = mongoClient.db("zara");
        const menAccessories = zaraDB.collection("men-accessories");

const result = await needle(
        "get",
        `https://www.zara.com/il/he/man-accessories-l537.html?v1=1720496&ajax=true`,
        options
    );
    await menAccessories.insertMany(resultA.body.productGroups[0].elements)
}
```