Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
str(a)
'10'
type(a)
<class 'int'>
type(str(a))
<class 'str'>
float(a)
10.0
complex(a)
(10+0j)
bool
<class 'bool'>
bool(a)
True
char(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    char(a)
NameError: name 'char' is not defined. Did you mean: 'chr'?

chr(a)
'\n'
list(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
list = [10,20,30,40,50]
type(list)
<class 'list'>
set(list)
{40, 10, 50, 20, 30}
set(list)
{40, 10, 50, 20, 30}
tuple(list)
(10, 20, 30, 40, 50)
type(tuple(list))
<class 'tuple'>
dict(list)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(list)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
set = (60,70,80,90)
type(set)
<class 'tuple'>
set = {60,70,80,90)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
set = {60,70,80,90}
type(set)
<class 'set'>
tuple(set)
(80, 90, 60, 70)
list(set)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(set)
TypeError: 'list' object is not callable
set1=(60,70,80,60,70}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
set1={60,70,80,60,70}
tuple=(1,2,3,4,5,2,3,4)

type(tuple)
<class 'tuple'>
set(tuple)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    set(tuple)
TypeError: 'set' object is not callable
dt={1:10, 2:20, 3:30}
dt(1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    dt(1)
TypeError: 'dict' object is not callable
set(dt)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    set(dt)
TypeError: 'set' object is not callable
list(dt)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list(dt)
TypeError: 'list' object is not callable
dict(dt)
{1: 10, 2: 20, 3: 30}
dict.dt(1)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dict.dt(1)
AttributeError: type object 'dict' has no attribute 'dt'
complex(set)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    complex(set)
TypeError: complex() first argument must be a string or a number, not 'set'
complex(list)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    complex(list)
TypeError: complex() first argument must be a string or a number, not 'list'
bool = True
bool(0)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    bool(0)
TypeError: 'bool' object is not callable
b=20
bool(0)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    bool(0)
TypeError: 'bool' object is not callable
bool(bool)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    bool(bool)
TypeError: 'bool' object is not callable
A=True
bool(A)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    bool(A)
TypeError: 'bool' object is not callable
c=5+6j
int(c)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
type(c)
<class 'complex'>
str(c)
'(5+6j)'
bool(c)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    bool(c)
TypeError: 'bool' object is not callable
>>> is bool(c)
SyntaxError: invalid syntax
>>> set(s)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    set(s)
NameError: name 's' is not defined
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    set(c)
TypeError: 'set' object is not callable
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
>>> d=coding
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d=coding
NameError: name 'coding' is not defined
>>> d='coding'
>>> type(d)
<class 'str'>
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'coding'
>>> list(d)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list(d)
TypeError: 'list' object is not callable
>>> int(bool)
1
>>> float(bool)
1.0
>>> complex(bool)
(1+0j)
>>> str(bool)
'True'
