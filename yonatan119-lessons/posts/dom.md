---
layout: post
title: Dom
published: 2021-03-23T12:30:34+00:00
author: yonatan119
tags: Dom
---

In the next lesson we are going to talk about the DOM and the virtual DOM
this will help us understand one of the reasons to use REACT.

there are 2 things you need to have a basic understanding in before reading this lesson

1. what is an api:
*API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.*

2. what is a node:
*A node is a basic unit of a data structure, such as a linked list or tree data structure. Nodes contain data and also may link to other nodes*





DOM

Just to get things straight - DOM stands for Document Object Model and is an abstraction of a structured text. For web developers, this text is an HTML code, and the DOM is simply called HTML DOM. Elements of HTML become nodes in the DOM.

So, while HTML is a text, the DOM is an in-memory representation of this text.

*Compare it to a process being an instance of a program. You can have multiple processes of the same one program, just like you can have multiple DOMs of the same HTML (e.g. the same page loaded on many tabs).*

The HTML DOM provides an interface (API) to traverse and modify the nodes.
It contains methods like getElementById or removeChild. We usually use JavaScript language to work with the DOM, because… Well, nobody knows why :).

So, whenever we want to dynamicly change the content of the web page, we modify the DOM.

Issues
The HTML DOM is always tree-structured - which is allowed by the structure of HTML document. This is cool because we can traverse trees fairly easily. Unfortunately, easily doesn’t mean quickly here.

The DOM trees are huge nowadays. Since we are more and more pushed towards dynamic web apps (Single Page Applications - SPAs), we need to modify the DOM tree incessantly and a lot. And this is a real performance and development pain.

Consider a DOM made of thousands of divs. Remember, we are modern web developers, our app is very SPA! We have lots of methods that handle events - clicks, submits, type-ins…

This has two problems:

It’s hard to manage. Imagine that you have to tweak an event handler. If you lost the context, you have to dive really deep into the code to even know what’s going on. Both time-consuming and bug-risky.

It’s inefficient. Do we really need to do all this findings manually? Maybe we can be smarter and tell in advance which nodes are to-be-updated?

React comes with a helping hand. The solution to problem 1 is declarativeness. Instead of low-level techniques like traversing the DOM tree manually, you simple declare how a component should look like. React does the low-level job for you - the HTML DOM API methods are called under the hood. React doesn’t want you to worry about it - eventually, the component will look like it should.

But this doesn’t solve the performance issue. And this is exactly where the Virtual DOM comes into action.

Virtual DOM
First of all - the Virtual DOM was not invented by React, but React uses it and provides it for free.

The Virtual DOM is an abstraction of the HTML DOM. It is lightweight and detached from the browser-specific implementation details. Since the DOM itself was already an abstraction, the virtual DOM is, in fact, an abstraction of an abstraction.

Perhaps it’s better to think of the virtual DOM as React’s local and simplified copy of the HTML DOM. It allows React to do its computations within this abstract world and skip the “real” DOM operations, often slow and browser-specific.

There’s no big difference between the “regular” DOM and the virtual DOM. This is why the JSX parts of the React code can look almost like pure HTML:

```jsx
const CommentBox = () => {
    return (
      <div className="commentBox">
        Hello, world! I am a CommentBox.
      </div>
    )
};
```

In most cases, when you have an HTML code and you want to make it a static React component, all you have to do is:

* [] Return the HTML code.
* [] Replace class attribute name to className - because class is a reserved word in JavaScript.

There are more differences which we will learn about in the future lessons.

You are a step close to start using REACT!
in the next lesson we will learn about the Server-side before we continue to react.

**Good luck!**