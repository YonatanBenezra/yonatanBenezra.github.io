---
layout: post
title: Node.js Exercise
published: 2021-04-20T12:30:34+00:00
author: yonatan119
tags: node, js, javascript
---

Here you will have a couple of mini projects to exercise Node.js.
the big project will be after learning express.

**1**
Create three files: 
1. utils.js
2. handler.js
3. questions.js

Inside of utils.js, export all three of these variables using a single object:

```javascript
const MONEY = "money"
const LIFE = "life"
const FREEWILL = "freewill"
```

Inside of handler.js, write a single function called handleQuestion

This function receives a single parameter called question: an object with two keys
text - some string
type - a string with either "money", "life", or "freewill" as the value
If the question type is...

"money", the function should print "how does the social construction of money work?"
"life", the function should print "What does it mean to live a good life?"
"freewill", the function should print "Is free will real or just an illusion?"
This function should use the MONEY, LIFE, and FREEWILL properties from the utils module
In other words, you should not hard-code: if(question.type === "money")

Of course, this means you will have to require the utils module inside of handler

Finally, in questions.js, make the following code work:

```javascript
let question1 = {
    text: "How do I get more money?",
    type: //use the FINANCE type from the utils module
}

let question2 = {
    text: "How much money do I need?",
    type: //use the FINANCE type from the utils module
}

let question3 = {
    text: "To be free or not to be?",
    type: //use the FREEWILL type from the utils module
}

handleQuestion(question1) //should print "how does the social construction of money work?"
handleQuestion(question2) //should print "how does the social construction of money work?"
handleQuestion(question3) //should print "Is free will real or just an illusion?"
```

For this to work you'll need a couple of imports - but remember, you can only require a module that's been exported!

