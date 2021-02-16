---
layout: post
title: The semantics of writing CSS class names in HTML
published: 2018-05-11T16:26:39+00:00
author: Kevin (typekev) Gonzalez
tags: programming, classnames, css, html, naming, react, styled-components
---

# The semantics of writing CSS class names in HTML

So I'm a really big fan of [`styled-components`](https://www.styled-components.com/). I know, I know, _classic_ React guy. Trying to shove everything into my JavaScript. I need to learn how to stay in my lane, I know. Look, that's not what this is about.

This is about Semantics.

I noticed something new while working on my project. You see, I was looking through my code using Google Chrome's inspector tool, like I always do, trying to pin point why my animation wasn't working. You know, normal dev stuff. And that's when I noticed it.

`<div class="TextContainer__TextContainer-evEmKn hpLTip"/>`

Now, I had not been working with the latest version of the aforementioned library for some time, which is usual, I don't make it a pattern to update packages 9 months into a project. But now that I started some new projects, I am hopping on the `latest` train left and right.

So when I saw the semantic class naming going on here I was pretty excited.

You see, I am a bit fanatic about semantic naming. Functions, classes, parameters, you name it. _I name it_, diligently.

And that got me thinking, what does it mean to semantically create class names? What should be the standard. I love the approach taken by Styled Components. But I also adamantly support Foundation by Zurb. Foundation uses a logical naming scheme based on what the element will function as, this library is assigning names based on my components, which I name _semantically, based on what they are._ These are slightly different concepts.

So then, what makes names semantic anyway.

> "Semantic classes don’t convey their styles"
>
> - [MaintainableCSS](https://maintainablecss.com/chapters/semantics/)

Class names should be easily understood. For instance, when I read JavaScript, I **cannot** stand seeing `const mapDataFunction = data => data.map( subdata => <div>{subdata}</div> )`.

It's madness.

Rather, I want to know, _what_ the data is, and _what_ it is being mapped to!

So today I learned, the what, is very important in semantics.

Keep it up, [`styled-components`](https://www.styled-components.com/).
