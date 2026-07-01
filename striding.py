Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
a="cloud computing"
a[::5]
'c u'
a[::4]
'cdmi'
a[::8]
'cm'
>>> a[2:]
'oud computing'
>>> a[:9]
'cloud com'
>>> a[3:11]
'ud compu'
>>> a[::2]
'codcmuig'
>>> a[::6]
'cci'
>>> a="machine learning"
>>> a[5:15:4]
'nei'
>>> a[2:12:3]
'cnlr'
>>> a[0:10:1]
'machine le'
>>> a[1:9:2]
'ahn '
>>> a[3:14:2]
'hn eri'
>>> a="python course"
>>> a[-1:-10:-2]
'ero o'
>>> a[-3:-13:-4]
'r t'
>>> a[-5:-11:-3]
'on'
>>> #do's and dont's
>>> #postive
>>> a="python course"
>>> a[8:6:2]
''
>>> a[6:8:2]
' '
>>> a[6:11:2]
' or'
>>> a[-7:-4:-2]
''
>>> a[-4:-7:-2]
'uc'
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
