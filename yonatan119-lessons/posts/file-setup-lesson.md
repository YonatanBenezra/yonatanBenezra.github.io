---
layout: post
title: File Setup Basics
published: 2021-10-18T13:30:34+00:00
author: yonatan119
tags: css, html
---


# *css & html setup*

What we will learn:

1. How to navigate through your computer and create new files directly from the command-line.

2. The boilerplate used to create our websites

Steps:

* [1] **Command Line Navigation**
As developers we tend to use the command line quite a bit so it is quicker to use it for easy commands as well, such as creating folders, or repositories, and opening them. 


Go ahead and open your command-line now:
 On Mac this is called Terminal or iTerm.
 On Windows it's called Command Prompt.


Congratulations! your in your "home folder"
 Let's see what's inside.
  If you're using windows type in:

`dir`

If you're using a mac, type in:

`ls`

Great, now we want to navigate to other folders.
to do that type in the folder name after writing cd.
like this:

`cd ~folderName`

if we want to enter our desktop we will write:

`cd desktop`

to go back we will write two dots in the foldername space, like this:

`cd ..`

* [2] Creating folders and files

Let's create a coding folder which will hold all of our projects.

lets enter our desktop once more by writing:

`cd desktop`

create a new folder called "code" by writing:

`mkdir code`


This will create a new folder called "code".

Now, lets enter our "code" folder by writing:

`cd code`

then, create a "lesson1" folder using mkdir:

`mkdir lesson1`


Great!
Lets start our first project!

to do this we will create two files: index.html and style.css.
(Windows):

```javascript
touch index.html
touch style.css
```
(Mac):

```javascript
nul index.html
nul style.css
```

* [3] Downloading our code editor

[Vs-code](https://visualstudio.microsoft.com/downloads/)

We want to download the Visual Studio Code.
click on the purple link box, install the VS Code that fits your computer and afterwards come back to this lesson :)


* [4] HTML Setup

Most of our projects will have an HTML file named index.html.
 The index file is the main file that gets run in our browser and it's where we connect all our other files (if we have them). Go ahead and copy/paste the following code inside of our index.html file:

```javascript
<!DOCTYPE html>
<html>

  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Page Title</title></head>
                    
  <body>
                    
  </body>
                    
</html>
```

This is our "HTML boilerplate". Boilerplate code is what we call code that we use to set-up our projects.

The html wraps our whole HTML document and inside of it we have our head and our body.

The head is for "logistics", like the title of our page and linking in other files.

The body is for the actual content of our page. Go ahead and add the following code inside of the body:

```javascript
<h1>Hello Presentense!</h1>
```

Lastly, open your HTML file in Google Chrome.
1. open Google Chrome.
2. Click (Windows) Ctrl+o, (Mac) Command+o
3. enter your lesson1 folder and choose your index.html file



* [5]: CSS Magic
Remember what we said about the logistic part inside our *html*?
The header!
lets use this to attach our css to the index.html!
to do this we will *link* our css inside the header.

like this:

```javascript
<head>
  <link rel="stylesheet" type="text/css" href="style.css" />
  <title></title>
</head>
```
We used the `<link>` tag which in it we entered two more tags.
1. `type`
2. `href`

the `type` tag helps our html understand what we is linking
the `href` tag helps our html understand what is the name of our linked file

Since both index.html and style.css are in the same folder, we can just write style.css.

Lets start the magic!

inside your `style.css`

write this:

```javascript
h1 {
    color: blue;
}
```

And now lets see you!