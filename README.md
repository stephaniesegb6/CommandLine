# **Improve command Line in **window****

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://vodanh.glitch.me)

These are the commands line that will help programer work with **Command Prompt** and **Powershell** easier and effectively in **window**.

They are all write in language [Python](https://python.org/).

## Note 

- These command just for working in **Command Prompt** and **Powershell** of **window**.
- You **shouldn't** use in other operating systems.

## Installation

Intstall and extract the file in your folder if you don't have `git`.

Else use command 
```sh
git clone https://github.com/stephaniesegb6/CommandLine.git
```

To use the command global, you have to add the direction of bin folder to `PATH`

**Command Prompt**:

```sh
set Path=%Path%;%DIR%\bin\
```

**Powershell**:
```sh
$env:Path += ';%DIR%\bin\'
```

( `%DIR%` is the direction where you install )

## **Compile command**

----------------

Compile command help us to compile and run file `.exe` immediately. It reduces the commands you have to compile and run.

Up to now, `compile` just available for **C/C++** Language.

We have to install one of these compilers :
- For **C/C++** :
	- GNU G++14
	- GNU G++17
	- GNU G++20

To use the command :

```sh
compile [filename...]
```

## **Touch Command**

------------

Touch command like `touch` in terminal of **linux**, it will create an empty file. Although there are many ways to create a file in **Command Prompt** and **Powershell** of **window** but they're still not good. Therefore, this command will help us to create one or more file. 

To use command :

```sh
touch [filename...]
```

## **More**

-------

- My email address : binhbhgl5@gmail.com.
- My Facebook : [Nguyen Hoa Binh](https://www.facebook.com/geor.steven/).
- My website : https://vodanh.glitch.me.