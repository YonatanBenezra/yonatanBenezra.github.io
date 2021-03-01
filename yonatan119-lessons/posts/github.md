---
layout: post
title: html
published: 2021-3-09T13:30:34+00:00
author: yonatan119
tags: html
---

We will go over these subjects in the following lesson:

* **git/hub**
* **Pre Install**
* **Installing Git**
* **Creating a Local Repository**
* **Github**
* **Cloning**
* **Cheat Sheet**

# Pre Install
We will use a code editor to ease our work with 

Lets install it

Windows users:

 install at: https://notepad-plus-plus.org/download/v7.5.9.html 

Or just google “Notepad++” and take the latest version.

Mac users:

 install Atom editor: https://atom.io/ 

What is Git?
it is a version-control.
basicly it is a way to save our lines of code in one place on our local computer.
We use Github to save our code on the web.
there is alot more to it, you can read about it [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)

In this lesson we’re going to:

* *Install Git and create our first local repository*
* *Create a repo on Github.*
* *Upload our local repo files to Github.*
* *Make changes.*


# Installing Git

Download it from [here](https://git-scm.com/downloads) and install it using the default settings. If you are having problems feel free to reach out in our whatsapp group!


**Important Installation Instructions**

start the installation and wait until you get to the page of selecting the text editor:

Make sure to select Notepad++ or atom as Git’s default editor.

Setup
First, let’s open the cmd.

Windows Users

In the search panel type: 

```javascript
git bash
```
Mac

In the search panel type:

```javascript
Terminal
```

After we opened our editor, lets start using it!
*note* every line automatically starts with a dollar sign, this is necessary but is automatic in this editor

To make sure git is installed correctly, let's type:

```javascript
git --version
```

If you see a git version, that means it is installed correctly.

To setup Git we need to configure our username and email so lets run the following commands.

```javascript
git config --global user.name "Your username"
git config --global user.email "your_email@gmaill.com"
```

Congratulations!
Our next step is to create a local repository

# *Creating a Local Repository*

A repository or Repo is where our code lives, both on our computer and on a host computer (Github, which we will use later on).

We will start by creating the local repository, that is located on our computer.

lets enter our css-html project directory.
type in your editor:

```javascript
ls
```

see which folders you have in the current directory and enter the folder which contains your project.
for example, to reach my project folder I will write this:

```javascript
ls
cd desktop
cd code
cd week1
cd css-html project
```

Now we want Git to keep track of all the files inside our directory
*note* A repository is just a storage space where Git can keep track of all files inside it.

To make this happen we need to write the following code, make sure you are in the directory which contains your projects folders.

```javascript
git init
```

You should see a message that says something like "Initialized empty Git repository in..."
This means Git is now keeping track of the folders, we need to do this step only once for each directory.

Now we can add files, update them and update the remote repository.

# *Github*

I think we are ready to move our Git project who lives locally to github.com.
this way other developers can see it, contribute to it, fork it, clone it and most importantly, it will serve as a backup if needed.

*Creating a repository on github*
* V Go to github.com and log in to your account.
* V Go to your profile and click the "Repositories" tab.
* V Click the big green button that says "New".
* V give your project a name.
* V If your creativity needs helps, name the project:
* V "Css-Html"
* V Lastly, click "create repository".

The instuctions on the next screen can be a little confusing so stick to this lesson and I promise it will work out.

Inside your editor
*note* make sure its in the projects directory.
write this command:

```javascript
git status
```

this will show you the status of all changed files in this directory.

we need to do a couple more steps:

1. add our changed files to our git.
2. save these changes (commit) with an explanation 
3. add a remote origin to github
4. push our local git changes to our github.

Step 1:
when you typed the command "git status" you probably saw some red lines, each line is a changed file, adding those files to our git will turn the lines to green!
lets do this by writing this command in our editor:

```javascript
git add .
```

we are adding to git everything that has changed, you can add only a certain file by switching the "." to a file name like this:

```javascript
git add index.html
```

step 2:
After adding the changes on step 1 we would like to commit to the changes with an explanation of what we are commiting we do it using the commit command like this:

```javascript
git commit -m "Initial commit"
```

this commits all the changes we added on step 1.

Step 3:
to connect between our local git to our github repo we need to go back to our repo in github, copy the URL at the top, head back to your command line, make sure you are in your project folder and run the command below. Just swap "YOUR_URL" for the URL you just copied.

```javascript
git remote add origin YOUR_URL
```

This command just added a reference to a "remote repository" to our local repository.

Step 4:
Our final step, after connecting between our local repo and our github repo we need to push all the changes we commited with this line of code:

```javascript
git push origin master
```

The command is telling Git to "push our project to the origin repo's master branch".
We'll talk more about branches in the future.
Now if you go back to Github and refresh your repo's page, you will see your files!

Congratulations!!

lets change something in our code and see how we update it in our github.

first things first, go to your html.index and change one word in it.
afterwards enter the command:

```javascript
git status
```

again, you can see a red line who represents the file changes (index.html).

now, these are very *important steps*
you enter 3 commands that we learnt

```javascript
git add .
```

```javascript
git commit -m "YOUR_EXPLANATION"
```

```javascript
git push origin master
```

Check your Github...
Amazing.


# *Cloning*

Click this [link](https://github.com/yonatan119/Fork) to navigate to the repo.

To fork this repo you need to:

Click the button in the top right that says "fork"...

Then select your profile.

GitHub has now made a copy of our repository on you your profile.

Now click "Clone or download" and copy the URL that is displayed.

Now, open your terminal and navigate to wherever you're storing your code - for example code/week1/.

Type

```javascript
 git clone <PasteURLHere> 
```

(of course you need to replace "PasteURLHere" with the URL you just copied):

Run the command (press enter). This will create a new folder on your computer. called Fork.

cd into that folder like normal and open it in vsCode (or the editor of your choice) to start working with it!

When you clone a github repo it will also set up a remote called "origin" so there is no need to do the whole git remote add origin ... thing.

By the way, you do not always have to fork repositories. If you're working on an existing repository and contributing to it, it's enough to just clone it so you have local access to it. Then you make your changes, and push it back to the original repo.

Generally we will only fork repos if we want to create something entirely new based off something existing.


# *Cheat Sheet*

Create empty directory:
`mkdir <name>` 

Navigate to directory:
`cd <path>`

Create a git repo in the current folder:
`git init`

Add a remote repository called origin with a link to your github repo:
`git remote add origin <link to remote repo>`

*Git Commit and Push*

First we have to add:
`git add .`

Commit:
`git commit –m "commit message"`

Git push:
`git push origin master`

*Basic Commands*

Git pull:
`git pull origin master`

Working directory status:
`git status`

See list of commits:
`git log`
