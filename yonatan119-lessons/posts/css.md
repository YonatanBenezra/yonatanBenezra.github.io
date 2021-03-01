---
layout: post
title: css
published: 2021-03-09T13:30:34+00:00
author: yonatan119
tags: css
---

# *css*

## Table Of Contents
- [Properties](#Properties)
  * [Selectors](#Selectors)
  * [Specificity](#Specificity)
  * [Display](#Display)

for this lesson we will still use our index.html and style.css
in case you do not have them please got to the files-setup lesson and go over it.

# *Properties*
Properties is what we use to define which styling to apply to our elements.
lets clear the "body" in our index.html and insert a simple div inside it, like this:

```html
  <div>
  </div>
```
now, open the index.html inside your browser
you can do this by writing

```javascript
start index.html
```

inside your terminal or clicking on ctrl/command+o in the browser and navigating to the index.html.

now we have our div but we cant see it, lets change this using our css.
inside your style.css enter this code:

```css
div {
  width: 100px;
  height: 100px;
  background-color: blue;
}
```
We can see a blue box on our page!

*notice* there is a semicolon (;) at the end of each row. this has to happen in css in order for the code to work.

what we did is tell the css to change the width, height and background color of all the div's on our page.
for the width and height we use the "px" measure (pixels)... we can use other measures such as, % (percentage), em, rem and more. try it out!
*in a further lesson we will cover this topic.*

and for the background color we set the color as "blue"... we can use other measures such as, hex and RGB.
try changing the background-color to a hex setting:

```css
#e74c3c
```

and now to a RGB setting:

```css
rgb(152, 224, 0)
```

we have many other properties such as:
background-image, border, border-radius, box-shadow, font-size, font-family, text-align and many more which you can find [here](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference).


# *CSS Selectors*

Selectors are a way for our css to understand what element we want to style.

we are going to learn a couple of ways to select the element we want to style.

the first way we have is using the element tag name, as we did above.
for example:

```css
div {
  color: yellow;
}
```

after entering this code into our style.css we will see all our div's text change to yellow.
so how do we select one specific element?


**Class and ID Selectors**

by giving the element a class or ID we can easily select a specific element.
for instance, if we have a header with the class "title":

<h1 class="title"></h1>

we can style this header using the class name like this:

```css
.title {
   font-family: italic;
}
```

the above code will change the font of all the elements with the class name "title"
*notice the "." before our class, if it was an ID it would be a "#"

*note* it is important to give each element a proper class name or id for easy styling.

in case we want to make sure only a specific element and only it will get a certain style we will use an ID selector

if this is our div's ID attribute:

```html
<div id="my-name">Yonatan.</div>
```
then this will be our CSS

```css
#my-name {
  color: red;
}
```

notice we are selecting the ID with a "#" and not with a "."

to sum this:
we will give classes to elements who are in a bigger group of styling, and ID for an element who we want to give specific styling.
each element can have both an ID attribute and a class. (it can even have more than one class)


**Pseudo Selectors**

using the psuedo selector we can give an html element a special state, for example, if we want our buttons to change color when a mouse hovers over it we can write this in our css:

```css
button:hover {
  background-color: orange;
  color: white;
  border: 1px solid black;
}
```


**Combining Selectors**

We can combine CSS selectors, lets try to color all of the "p" tags inside div's but not ones that are outside of div's. 

first lets write some html to meet the requirements:

```html
<div>
  <p>I am inside a div</p>
  <p>I am inside a div</p>
</div>
<p>I am outside of a div</p>
```

lets add the css with combined selectors:

```css
div p {
  color: orange
}
```

we can see only the p tags inside of a div were colored!

[here](https://www.w3schools.com/css/css_combinators.asp) we can find more options of combining selectors.

**Specificity**

what happens if we have this html:
```html
<div id="container" class="green-text-div">what color will I be?</div>
```

and this css:

```css
div {
color: blue;
}
.green-text-div {
  color: green
}
#container {
  color: orange
}
```

try it out before looking at the answer:
>the text will be orange

why?
because each selector has a level of specificity.
here is a list at the least specific:

1. Element Selectors (least specific)


2. Class and Attribute Selectors



3. ID Selectors


4. Chained selectors

5. Inline Stlyes

We can use a "style" attribute in html, like this

```html
<div style="background-color: orange;" id="about" class="about-container">
</div>
```

6. !important

this selector overrides all other styles.

7. position in the File

when two conflicting style rules have the same specificity, the one that's defined lower down in your CSS file will win.

This rule also applies across multiple files. If you link several CSS files to your HTML page the links further down the page will be more important.


*if one selector is in conflict with another, the one with the highest level of specificity will win. the best practice is using the least specific selectors first.


# *Display*

the difference between block and inline elements.

a block element such as div, h1...
will take up the entire width available to it unless specified differently

On the other hand, if we had an in-line element such as a "span" tag, even if we give it a width and height we wont see the "span" because an in-line element will be affected only by its content.

We can use the display property like this:

```css
span {
  height: 100px;
  width: 100px;
  background-color: orange;
  display: inline-block;
}
```

Now our span element is inline-block and will still take up exactly the space it needs, but our css values take effect

There are other display values you can explore [here](https://www.w3schools.com/cssref/pr_class_display.asp)