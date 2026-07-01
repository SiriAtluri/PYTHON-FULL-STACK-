Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("k")
2
a.count(" ")
3
#find a string
a="code"
a[1]
'o'
a.find("d")
2
a.find("e")
3
b="hello"
b.find("l")
2
b[2:4]
'll'
#escape sequences
#\n-> new line
#\t-> tab space
a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
b="name-siri\nmobile-7382425609\tmailid-siriatluri2005@gmail.com\nclg-sr university"
print(b)
name-siri
mobile-7382425609	mailid-siriatluri2005@gmail.com
clg-sr university
#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a
'wait until you succeed'
b="wait wait until you succeed"
b.replace("wait","work")
'work work until you succeed'
b.replace("wait","work",1)
'work wait until you succeed'
#upper()
a="hello"
a.upper()
'HELLO'
#lower()
b="PYTHON"
b.lower()
'python'
c="codegnan"
c.upper(0)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    c.upper(0)
TypeError: str.upper() takes no arguments (1 given)
c[0].upper()
'C'
c.capitalize()
'Codegnan'
a="python course"
a.title()
'Python Course'
c="i am in class"
c.title()
'I Am In Class'
a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="python course"
b.isalpha()
False
c="pythoncourse"
c.isalpha()
True
d=1234
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="1234"
d.isdigit()
True
d.isalnum()
True
e="siri1234"
e.isalnum()
True
="siri@1234"
SyntaxError: invalid syntax
f="siri@1234"
f.isalnum()
False
a="hello python"
a.startswith("h")
True
a.endswith("n")
True
#strip()
#lstrip(),rstrip()
a="       siri        "
a.strip()
'siri'
a.lstrip()
'siri        '
a.rstrip()
'       siri'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am in vijyawada"
b.split()
['i', 'am', 'in', 'vijyawada']
c="codegnan"
c.split()
['codegnan']
#join()
a="vja hyd vzg"
"".join(a)
'vja hyd vzg'
b="vja","hyd","vzg"
"".join(b)
'vjahydvzg'
" ".join(b)
'vja hyd vzg'
"k".join(b)
'vjakhydkvzg'
#concatenation
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
fname="siri"
lname="a"
print(fname+lname)
siria
print(fname+" "+lname)
siri a
print(fname.title()+" "+lname.title())
Siri A
print((fname+" "+lname).title())
Siri A
#formatting
a=4
b=8
print(a+b)
12
print("the sum is",a+b)
the sum is 12
x="vja"
print("city is",x)
city is vja
#format method
a="motu"
b="patlu"
print("hello",a+b)
hello motupatlu
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>>print("hello {} {}".format(a,b))
hello matu patlu
>>> print("hello {} hello {}".format(a,b))   
hello motu  hello patlu
>>> #fstring     
>>> a="sita" 
>>> b="ram"
>>> print(f"hello {a}{b}")    
hello sitaram
>>> print(f"hello {a} {b}")    
hello sita ram
>>> print(f"hello {a} hello {b}")     
hello sita hello ram
>>> a=4   
>>> b=5   
>>> c=a*b   
>>> print("the product is {}".format(c))   
the product is 20
>>> print(f"the product is {c}")     
the product is 20
>>> print("the product is {}".format(a*b))    
the product is 20
>>> print(f"the product is {a*b}")     
the product is 20
