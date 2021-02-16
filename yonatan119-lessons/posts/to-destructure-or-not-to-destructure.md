---
layout: post
title: To destructure or not to destructure
published: 2018-01-10T12:00:32+00:00
author: Kevin (typekev) Gonzalez
tags: programming, work, javascript, react
---
# To destructure or not to destructure

A topic came up at work recently, and it all revolved around this simple line.

```javascript
const { myAwesomeProp } = this.props;
```

We are currently building a banking application in [_React_](http://reactjs.org/). And since I've been enjoying ES6, I've gotten into the habit of destructing everything. If I can make my code look organized, I feel proud. So when I see `this.props.aCoolProp` sprawled all over my screen I cry a little inside. Why? Because to me, assigning properties of an object to variables of the same name is incredibly neat. Destructuring encourages me to think about my naming patterns and allows me to clearly see what I am doing when reading through my code.

Or so I thought.

## The issue of readability and data origin

I noticed a pattern with [my colleague Fred](https://www.linkedin.com/in/fr%C3%A9d%C3%A9ric-colin-163b7251/), specifically within his code, he seemed to avoid destructing like the plague! Naturally this was driving me crazy. You see, Fred is a very talented guy, surely I thought, he must know how to destructure! So I asked him about it. And boy did he have an opinion on it. In Fred's opinion, destructing makes things _**more**_ difficult to read! To him, seeing `this.props` and `this.state` makes it easier to identify where the variable originates from.

And that made sense. If you have a prefix, it would make it easier to know whether this was a property from a parent or a local variable. At the cost of lengthier statements.

So that was fine, but my problem still persisted. How can you prefix everything. If you have fifty variables, you would have this.props written fifty times. Which negates the benefit. So where do you draw the line?

When should you use destructuring, and when should you not. Or when should we rename a property?

## What we found useful

We found that for smaller functions, we prefer to destructure but for long functions, i.e. exceeding 20 or so lines, we found it useful not to destructure all the time as we would lose track of the source of the variables.

However, we could not come up with a rule we could follow all the time and we still somehow felt dissatisfied with the available native methods. We needed a tool to safely extract JavaScript objects in an easy to read manner. To reconcile both sides, Fred decided to build [a neat library to destructure intelligently.](https://www.npmjs.com/package/revampjs) The library lets you group extracted variables within a new object, and defaults to `undefined` for any variable not found in the source object, even when the value is nested.

And did I mention it works with immutable data?

It works like this:

```javascript
const sourceObject = {
  a: 42,
  b: "hello",
  c: "world",
  d: "!",
  e: { f: "nested value" }
};
```

We've used Fred's tool in a few projects and it's actually fairly practical. If you've also had this issue, you can learn more about [revampjs here.](https://www.npmjs.com/package/revampjs)
