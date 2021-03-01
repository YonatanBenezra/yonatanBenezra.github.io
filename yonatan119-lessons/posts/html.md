---
layout: post
title: html
published: 2021-03-09T13:00:34+00:00
author: yonatan119
tags: html
---

# *html*

*Nodes and elements*

everything inside of HTML is a node, for example: comments, text and elements.

An element is made up of an "opening tag" and a "closing tag". for example: a "paragraph" tag will use the "p" element.

```javascript
<p>here will be the text inside of this paragraph.</p>
```
so we have an opening tag of a "p" element, text which is a node and a closing tag.

How many elements are in the code below? What are their tags?

```javascript
<div>
  <h2>I am a header</h2>
  <p>its cosy here inside of a div</p>
</div>
```

Highlight over the colored text below for the answer:

> There are 3 elements: A "div", and inside of it an "h1" element and next to it a "p" element.

*Structure*

Thanks to HTML elements, we can control the layout of a webpage.

lets try it out!
copy this block of code inside your html file and see how it looks.

```javascript
<h1>h1 is the largest sized headin</h1>
<p>this is a "p" element, mostly it will contain long text</p>

<h2>this is an h2</h2>
<p>this is a sub-heading about the sizes of headings. the largest heading element is h1, as the number of the heading is bigger, the size of the font is smaller</p>

<h3>for instance, this is an h3</h3>
<p>cool.</p>
```

*block elements*
 the elements we used above are block elements, which means they
 take up the entire width of their parent element
 each of these elements is a child of the body element.
 the width of the body element is the whole page, so the width of all its children are the whole page too!

*inline elements*

inline elements only take up as much space as they need.
lets see an example of an inline element.

copy this text to your body and pay attention to the width of the span element

```javascript
<p>I take up all the width of my parent<span>I take up space only as much as needed because im an inline element.</span></p>
```

# *attributes*

we can give each element a specific attribute, like an id:

```javascript
<p id="title">presentense</p>
```

We added an ID attribute to a "p" element inside of the opening tag, which lets us identify each element. this doesn't not change anything about the element, but some attributes can change the functionality or affect or the element, some even require certain attributes.

another common identifier attribute is class.
the difference about the two is:
the same Class can be given to more then one element, and each element can be given more than one class.
something that can not happen with the ID attribute.
(there can not be more than one element with the same and each element)

To give an element more than one class, just separate them with a space, like so:

```javascript
<p class="paragraph element">my classes are "paragraph" and "element"</p>
```

lets talk about some other tags.

*img tag*

the img (image) tag is one of those elements who require a certain attribute,
to show an image we need to enter the image link inside of a "src" attribute like this: 

<img src="https://pbs.twimg.com/profile_images/821849411991044096/lQFa_Vly.jpg"/>

notice anything strange?
this element does not have a closing tag!
most of the elements don't really need a closing tag, so thats cool.

*a tag*

An a tag is used for linking.
it needs an "href" attribute with the link url.
we can use the a tag for linking 
 To do so, we use an href attribute like the following:

```javascript
<a href="http://www.google.com">Click Here for Google!</a>
```

lets use this "a" tag to scroll between sections on the page.

first: we will copy this code to our body at the top of the page

```javascript
<div id="top">Top</div>
```

then enter a "div" tag with enough text to fill the page and on the bottom copy this code:

```javascript
<a href="#top">To Top</a>
```

once we click on the "a" tag it will send us to the "div" with an id of "top".

make sure the page has somewhere to scroll, if it is too small this excersice wont work.

# *important notes*

1. to call a class we write the class name with a dot beforehand.
2. to call an id we write the class name with a "#" beforehand.

we will use these mostly in css or with inner site "a" tags. 


# *HTML tags list*

For now, the most useful tags will be:
- [div](#div)
  * [h1-h6](#h1-h6)
  * [p](#p)
  * [ul/ol&li](#ul/ol&li)
  * [input](#input)
  * [button](#button)


# div

The div tag is a block element,
it will help us organize elements on the page and style them later on with CSS.

we can nest any element within a div, go ahead and try!

```javascript
<div>

 <div>nested div</div>

 <span>nested span</span>

 <p>nested p</p>

</div> 
```

nesting elements will help us better style our our elements!

# *headers*

The h tag is a block element.

they let us display text in different sizes in an easy way.

# *p*

The p tag is a block element,
They should not contain any other element nested in them or anything besides text.

# *lists*

ul: unordered list
ol: ordered list
li: list item

we nest the li tag inside either an ol tag or a ul tag.

like this:

<ol>

	<li>Presentense</li>

	<li>Haratzif</li>

	<li>ARDC</li>

</ol>


# *input*

We use inputs to input data that we can later use.

there are two important attributes that we will talk about.

1. placeholder - a text which will display before the user types inside.

2. type - the type of input allowed for the use, it can be text, number...

# *button*

the button tag will render a pre-styled button that will all the user to interact with our page.
for example:

```javascript
<button>buy</button>
```

this does not do anything right now because we didn't add any logic.