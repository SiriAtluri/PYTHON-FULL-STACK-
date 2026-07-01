Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
#slicing
#postive
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a="work until you succeed"
>>> a[5:10]
'until'
>>> a[11:14]
'you'
>>> a[0:4]
'work'
>>> a[15:24]
'succeed'
>>> b="codegnan it solution"
>>> b[9:11]
'it'
>>> b[12:20]
'solution'
>>> b[0:8]
'codegnan'
>>> #negative
>>> a="vijayawada is a royal city"
>>> a[-10:-5]
'royal'
>>> a[-26:-16]
'vijayawada'
>>> a[-4:-1]
'cit'
>>> a[-4:]
'city'
>>> b="vizay is city of destiny"
>>> b=[-15:-11]
SyntaxError: invalid syntax
>>> b[-15:-11]
'city'
>>> b[-24:-19]
'vizay'
>>> b[-7:]
'destiny'
