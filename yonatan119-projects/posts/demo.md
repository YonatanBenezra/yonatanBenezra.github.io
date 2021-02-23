---
layout: post
title: css-html
published: 2021-10-18T13:30:34+00:00
author: yonatan119
tags: css, html
---
## Table Of Contents
- [css & html](#css-&-html)
  * [Why was Goolo made and why you should use it]asd(#Why-was-Goolo-made-and-why-you-should-use-it)
  * [Running the project](#running-the-project)
  * [Screenshots](#screenshots)
    * [another way](#anotherway)
    + [Goolo Swiper](#Goolo-Swiper)
    + [Goolo Recommendations](#Goolo-Recommendations)
  * [Technologies](#technologies)
    + [Client-Side](#client-side)
    + [Server-Side](#server-side)
  * [Whats Next](#whats-next)
  * [Be a contribute](#be-a-contribute)
# *css & html*

This lesson is about HTML. In particular, we will:

Talk about the difference between HTML "nodes", "tags", and "elements".
Distinguish between "block" and "inline" elements.
Look at a few HTML attributes.
Look at some of the most common HTML tags.


**SETUP**

From your command line, create an index.html file, open it in your code editor (e.g VS Code, Notepad, PyCharm...), and add the following boilerplate to it:

```javascript
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body><!-- your HTML goes here -->
</body>

</html>
```
```javascript
function add(num1, num2) {
    return num1 + num2;
}
```
Test things out (a habit we need to form) by opening your index.html in your browser. Everything working as expected?



REMINDER
Remember, except for the boilerplate HTML - any HTML you write must be in the body tag - that is, between these two:

---
>\<body>
>
>\<!-- Your HTML goes here! -->
>
>\</body>

see this link:
[link](https://link.com)

this is a list
* item
    * nested item
        * another one

1. hey
2. hey

`<p> this is an inline code block </p>`

![logo]()

| Name| Email     
| - | - 
| John doe| John@gmail.com
| Jane doe| jane@gmail.com

* [x] task 1
* [o] task 2

<button name="button">Click me</button>

## collapsible markdown?

<details>
<summary>CLICK ME</summary>
<p>

#### yes, even hidden code blocks!

```javascript
console.log("hello world!")
```

</p>
</details>

<dl>
  <dt>This is a list</dt>
  <dd>With hanging indentation</dd>
</dl>

<div align="center">This is center aligned!</div>
<div align="left">Left aligned</div>
<div align="right">Right aligned</div>

<details>
  <summary>label</summary>
  ...goodies in here.
</details>

<img valign="middle" src="https://img.shields.io/badge/for-example-brightgreen.svg">

<samp>Monospaced text</samp>

<ins>Underlined text</ins>

<table><tr><td>Boxed text</td></tr></table>

[//]: # (This comment won't be rendered to the visitor!)

<img src="https://some-img-host.com/1234567/image.png" width=300 height="256" title="Github Logo" align=right>

## COLOR!

- ![#ff0000](https://placehold.it/12/ff0000?text=+) red!
- ![#9900c5](https://placehold.it/15/9900c5?text=+) purple!
- ![#157500](https://placehold.it/20/157500?text=+) green!

![](https://placehold.it/400x90/ff0000/000000?text=IMPORTANT!)

![](https://placehold.it/400x90/ff6600/000?text=WARNING!)

![](https://placehold.it/350x90/009955/fff?text=SUCCESS!)

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)
