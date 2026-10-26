'''Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
M = 'master'
type(M)
<class 'str'>
M
'master'
id(M)
2961461370704
M+='Master'
id(M)
2961458521584

list=[1,2,3,4]
list
[1, 2, 3, 4]
list.add(5)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list.add(5)
AttributeError: 'list' object has no attribute 'add'
list.insert(5)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    list.insert(5)
TypeError: insert expected 2 arguments, got 1
list.insert(4,5)
list
[1, 2, 3, 4, 5]
type(list)
<class 'list'>
tup=(6,7,8,9)
tup
(6, 7, 8, 9)
tup.count
<built-in method count of tuple object at 0x000002B1872777E0>
tup.index
<built-in method index of tuple object at 0x000002B1872777E0>
tup.index(1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tup.index(1)
ValueError: tuple.index(x): x not in tuple
list.append(6,7,8,9)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    list.append(6,7,8,9)
TypeError: list.append() takes exactly one argument (4 given)
list.append(6)
list
[1, 2, 3, 4, 5, 6]
list.append(7)
list
[1, 2, 3, 4, 5, 6, 7]










set= {1,2,3,4,5}
set
{1, 2, 3, 4, 5}
set.pop
<built-in method pop of set object at 0x000002B1873A4660>
set
{1, 2, 3, 4, 5}
set.pop(5)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    set.pop(5)
TypeError: set.pop() takes no arguments (1 given)
set.pop()
1
set
{2, 3, 4, 5}
set.remove(5)
set
{2, 3, 4}
set2={3,4,5,6}
set2
{3, 4, 5, 6}
set.difference(set2)
{2}
set2.difference(set)
{5, 6}
set.difference_update(set2)
set
{2}
set.add(3,4)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    set.add(3,4)
TypeError: set.add() takes exactly one argument (2 given)
>>> set.add(3)
>>> set.add(4)
>>> set
{2, 3, 4}
>>> set2
{3, 4, 5, 6}
>>> set.intersection(set2)
{3, 4}
>>> set2.intersection(set)
{3, 4}
>>> set.issubset(set2)
False
>>> set2.issubset(set)
False
>>> dict = {"Anime": "One Piece", "Main":"Luffy", "Team":10}
>>> dict
{'Anime': 'One Piece', 'Main': 'Luffy', 'Team': 10}
>>> dict(anime)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(anime)
NameError: name 'anime' is not defined
>>> dict(Anime)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    dict(Anime)
NameError: name 'Anime' is not defined
>>> team
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    team
NameError: name 'team' is not defined
>>> Team
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    Team
NameError: name 'Team' is not defined
>>> dict.values
<built-in method values of dict object at 0x000002B1873C7AC0>
>>> dict.values(Anime)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    dict.values(Anime)
NameError: name 'Anime' is not defined
