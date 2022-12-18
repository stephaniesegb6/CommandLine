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
set Path=%Path%;[direction]\bin\
```

**Powershell**:
```sh
$env:Path += ';[direction]\bin\'
```

## **Compile command**

----------------

Compile command help us to compile and run file `.exe` immediately. It reduces the commands you have to compile and run.

Up to now, supported language is **C/C++**.

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

### **More for Commpetitive Programmer**

Touch command also support for competitive programming such that you can create new file with your template.

This feature is just available for **C/C++** language.

Command :

```sh
touch [filename...] [--option]
```

- `--cpp` for **C/C++** language.

To config the template, go to `[direction]/bin/templateTouch/` and edit file config of the language which you use according to your template.

For example the template of **C/C++** language will in file `./cpp.txt`:

```c++
/*./bin/templateTouch/cpp.txt*/
#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

const int inf = 1e9 + 7;

int main(){
	return 0;
}
```

## **Compare Command**
------------------

I found `diff` command or `Compare-Object` in **Powershell** is too long and isn't suitable for competitive programming. Therefore I create this command to compare and show the differences between two files (difference at which line,...). If you use **Command Prompt**, you can use `fc` command instead.

To use command :

```sh
cf [filename1] [filename2]
```

Result :

```sh
Two files are different:
[filename1]:
	[line]| [str1]
[filename2]:
	[line]| [str2]
```

## **Time Counting Command**

This command counts how long it will take your program to run.

Command :

```sh
timer [filename]
```

## **More**

-------

- My email address : binhbhgl5@gmail.com.
- My Facebook : [Nguyen Hoa Binh](https://www.facebook.com/geor.steven/).
- My website : https://vodanh.glitch.me.
