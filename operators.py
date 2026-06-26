Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arithemetic operator
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#assignment operators
a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
a+b
8
a+=b
a
8
print(a)
8
a-=4
a
4
a*=5
a
20
a//=2
a
10
a/=2
a
5.0
a**=3
a
125.0
a%=4
a
1.0
b+=a
b
6.0
print(b)
6.0
b-=4
b
2.0
b*=5
b
10.0
b//=2
b
5.0
b/=2
b
2.5
b**=3
b
15.625
b%=4
b
3.625
#comparision operator
a=4
b=9
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
b<=a
False
a>=b
False
a=6
b=6
a==b
True
#logical operator
a=3
b=6
a<b
True
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
>>> a<b or b>a
True
>>> a!=b or a==b
True
>>> a<=b or b<=a
True
>>> not True
False
>>> not False
True
>>> #identify operator (or) identity operator
>>> a=6
>>> type(a) is int:
...     
SyntaxError: invalid syntax
>>> type(a) is int
True
>>> if type(a) is int
SyntaxError: expected ':'
>>> a=4
>>> type(a) is int
True
>>> type(a) is not int
False
>>> b=6.7
>>> type(b) is float
True
>>> type(b) is str
False
>>> a=4+9j
>>> type(a) is complex
True
>>> a=True
>>> type(a) is not bool
False
>>> a=False
>>> type(a) is bool
True
>>> #logical operator
>>> a=3,4,5,6,7,8,9
>>> 8 in a
True
>>> 20 in a
False
>>> 20 not in a
True
