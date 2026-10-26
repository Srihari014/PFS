Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=2=
SyntaxError: cannot assign to literal
b=20

============================================================================ RESTART: Shell ===========================================================================
a=50
b=25
a+b
75
a-b
25
a*b
1250
a/b
2.0
a//b
2
a%b
0
a/b
2.0
5**3
125
'''Arithmetical operators -> + - * / // % **  '''
'Arithmetical operators -> + - * / // % **  '
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
'''comparison operators-> < > <= >= == !='''
'comparison operators-> < > <= >= == !='
c=30
c = c+20
c
50
c=c-20
c
30
c += 20
c -= 20
c
30
c /= 3
c
10.0
c *= 3
c
30.0
c //= 3
c
10.0
c
10.0
c %= 10
c
0.0
c+=30
c
30.0
c **= 2
c
900.0
'''Assignment operators -> = += -= /= //= %= **='''
'Assignment operators -> = += -= /= //= %= **='

# and or not

a%2 == 0 and a>=50
True
b%3==0 or b >20
True
b%3 == 0 or not b>20
False
b%5 == 0 or not b>20
True

# Menbership operators
# set list tuple dict
s='coding'
i in s
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    i in s
NameError: name 'i' is not defined
>>> 'i' in s
True
>>> 'p' in s
False
>>> 'a' not in s
True
>>> l = ['The', 'art', 'of', 'code']
>>> 'python' in l
False
>>> 'dode' in l
False
>>> 'code' in l
True
>>> 'art' not in l
False
>>> t = (10,20,30)
>>> 10 in t
True
>>> 30 not in t
False
>>> d={1:10, 2:20, 3:30, 4:'code'}
>>> 'code' in d
False
>>> l = [1,2,3,4,5]
>>> m=[6,7,8,9,10]
>>> id(l)
2225549689984
>>> id(m)
2225557123904
>>> l is m
False
>>> l = m
>>> l is m
True
>>> m
[6, 7, 8, 9, 10]
>>> l
[6, 7, 8, 9, 10]
>>> id(l)
2225557123904
>>> id(m)
2225557123904
