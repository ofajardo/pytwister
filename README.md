# pytwister
Python with a twist of R syntax


Are you an R programmer and trying python and don't like the syntax?

Are you tired of fighting against indentation? do you miss curly braces?
Do you miss the <- operator to do variable assignment?

Then try pytwister and put a twist of R in your python scripts!

**Disclaimer: The package works! but it is meant only as a joke and not
to be used on anything serious.**

## Installation

Clone or download the repo and do:

```
pip install .
``` 

## Usage

Start your python script with the comment ```# coding=pytwister``` 
(it has to be in the first or second line). Then write your script with
normal python or pytwister R syntax and then execute it. 

For example, write an example.py script that contains:

```python
# coding=pytwister

a <- 1
print(a)
```

and execute it:

```
python example.py
```

this will print:

```
1
```

## R syntax supported:

* **any python code is still valid**

* **"<-" assign operator:** it will be replaced by a python "=". There should
be no space between < and - . If you would like to do a less than 
comparator to a negative  number, do < - (notice the space between < and
-),for example 5 < -6 , or use parenthesis like 5 < (-6).

example: 

```
a <- 1
```

* **braces:** you can use braces instead of indentation. 

example:

```
for x in range(5){
    print(x)
}
```

In order to disambiguate to the braces to build dictionaries, the opening
brace should always be in the same line as the statement and before the
newline, otherwise it will be interpreted as dictionary. The closing
brace should be alone in its own line. 

* **"function_name <- function(args)":** this will be replace by "def
function_name(args)". 

example: 

```
myfun <- function(a,b){
  return a+b
}
```

## Limitations

It works only when running scripts, does not work from the interactive
console.

## Compatibilty

Only python 3 is supported.

## How does it work?

Pytwister uses support for specifying source code encodings as described 
in PEP 263. The functionality was originally provided so that python 
developers could write code in non-ascii languages (eg. chinese variable
names). Pytwister creates a custom encoding called pytwister which 
converts the R syntax elements into regular python before the file is 
compiled. Once the pytwister codec is registered, any file starting with 
&#35;coding: pytwister is run through the pytwister parser before compilation.

This package is inspired by [interpy](https://github.com/syrusakbary/interpy)
and [pyxl](https://github.com/gvanrossum/pyxl3)

## Motivation

Functional languages such as Lisp have macros that capture non executed
(quoted) code for the user to modify it. In this way new syntactic 
elements can be introduced into the language. 

I just wanted to explore to what extend python supports this kind of
metaprogramming, as it clearly does not support macros. 

There are several alternatives to get what lisp macros can do. For example
dplyr like pipes have been introduced with a combination of decorators
and custom definition of operators in classes (see [dfply](https://github.com/kieferk/dfply)).
Compiled code can be modified using decorators 
(see [python-goto](https://github.com/snoack/python-goto).

These methods however are limited to valid python code. If non-valid 
python syntatic elements should be added, the only option is to parse
the script and replace with valid python syntax before compile. This 
package is an example on this. Other interesting examples that use different
mechanisms are [bython](https://github.com/mathialo/bython) and of course
[hy](https://github.com/hylang/hy) the later implementing a full lisp interpreter on top of the python
virtual machine.

