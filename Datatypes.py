Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=10
>>> type(a)
<class 'int'>
>>> b=4.5
>>> type(b)
<class 'float'>
>>> c='code'
>>> type(c)
<class 'str'>
>>> d="codegnan"
>>> type(d)
<class 'str'>
>>> e='''course'''
>>> type(e)
<class 'str'>
>>> f=5+9j
>>> type(f)
<class 'complex'>
>>> g=4j
>>> type(g)
<class 'complex'>
>>> y=6+9i
SyntaxError: invalid decimal literal
>>> type(4+9j)
<class 'complex'>
>>> type(3j+6)
<class 'complex'>
>>> type(7j)
<class 'complex'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> c="true"
>>> type(c)
<class 'str'>
#datatype conversions
#int
int(6)
6
int(4.5)
4
int("python")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(3+9j)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(3+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#string
str(5)
'5'
str(77)
'77'
str(777)
'777'
str(4.5)
'4.5'
str(7.8)
'7.8'
str('code')
'code'
str("python")
'python'
str('''codegnan''')
'codegnan'
str(4+9j)
'(4+9j)'
str(3j+6)
'(6+3j)'
str(7j)
'7j'
str(True)
'True'
str(False)
'False'
#float
float(4.5)
4.5
float(7.8)
7.8
float('code')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    float('code')
ValueError: could not convert string to float: 'code'
float("python")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float('''codegnan''')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    float('''codegnan''')
ValueError: could not convert string to float: 'codegnan'
float(4+9j)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    float(4+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(3j+6)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    float(3j+6)
TypeError: float() argument must be a string or a real number, not 'complex'
float(7j)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
float(TRUE)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(TRUE)
NameError: name 'TRUE' is not defined. Did you mean: 'True'?
float(FALSE)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    float(FALSE)
NameError: name 'FALSE' is not defined. Did you mean: 'False'?
#complex
complex(5)
(5+0j)
complex(77)
(77+0j)
complex(999)
(999+0j)
complex(4.5)
(4.5+0j)
complex(7.8)
(7.8+0j)
complex('code')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    complex('code')
ValueError: complex() arg is a malformed string
complex("python")
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    complex("python")
ValueError: complex() arg is a malformed string
complex('''codegnan''')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    complex('''codegnan''')
ValueError: complex() arg is a malformed string
complex(4+9j)
(4+9j)
complex(3j+6)
(6+3j)
complex(7j)
7j
complex(True)
(1+0j)
complex(False)
0j
complex(TRUE)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    complex(TRUE)
NameError: name 'TRUE' is not defined. Did you mean: 'True'?
complex(FALSE)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    complex(FALSE)
NameError: name 'FALSE' is not defined. Did you mean: 'False'?
bool(5)
True
bool(77)
True
bool(999)
True
bool(4.5)
True
bool(7.8)
True
bool('code')
True
bool("python")
True
bool('''codegnan''')
True
bool(4+9j)
True
bool(3j+6)
True
bool(7j)
True
bool(True)
True
bool(False)
False
bool(1)
True
bool(0)
False
