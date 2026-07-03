Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict{}
>>> a={"name":"siri","city":"vja"}
>>> print(a)
{'name': 'siri', 'city': 'vja'}
>>> type(a)
<class 'dict'>
>>> b={5,6,7,8,9,"name"}
>>> type(b)
<class 'set'>
>>> a={"name":"siri","mailid":"siriatluri2005@gmail.com","mobileno":8765499024}
>>> print(a)
{'name': 'siri', 'mailid': 'siriatluri2005@gmail.com', 'mobileno': 8765499024}
>>> a.keys()
dict_keys(['name', 'mailid', 'mobileno'])
>>> a.values()
dict_values(['siri', 'siriatluri2005@gmail.com', 8765499024])
>>> a.items()
dict_items([('name', 'siri'), ('mailid', 'siriatluri2005@gmail.com'), ('mobileno', 8765499024)])
>>> a={"course":"python","institute":"codegnan"}
>>> a.update({"name":"siri"})
>>> a
{'course': 'python', 'institute': 'codegnan', 'name': 'siri'}
>>> a.update({"year":2026},{"month":7})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.update({"year":2026},{"month":7})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"year":2026,"month":7})
>>> a
{'course': 'python', 'institute': 'codegnan', 'name': 'siri', 'year': 2026, 'month': 7}
>>> a={"year":2026,"month":"july"}
>>> a.setdefault("data",2)
2
>>> a
{'year': 2026, 'month': 'july', 'data': 2}
>>> a={"time":12,"hour":1,"min":3}
a.pop()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("time")
12
a
{'hour': 1, 'min': 3}
a.popitem()
('min', 3)
a
{'hour': 1}
a={"college":"sr university","branch":"cse"}
a.get("college")
'sr university'
a["branch"]
'cse'
a
{'college': 'sr university', 'branch': 'cse'}
a.get("cse")
a
{'college': 'sr university', 'branch': 'cse'}
a["cse"]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a["cse"]
KeyError: 'cse'
a={"hour":12,"min":3,"sec":60}
a.copy()
{'hour': 12, 'min': 3, 'sec': 60}
a
{'hour': 12, 'min': 3, 'sec': 60}
a.clear()
a
{}
b={}
b.update({"name":"siri"})
b
{'name': 'siri'}
a={"name":"siri","course":"python","year":2026}
len(a)
3
a.count("name")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
a={"name":"siri","city":"vja","name":"siri"}
print(a)
{'name': 'siri', 'city': 'vja'}
a={"name":"siri","city":"vja","name":"priya"}
print(a)
{'name': 'priya', 'city': 'vja'}
a={"name1":"siri","city":"vja","name2":"siri"}
print(a)
{'name1': 'siri', 'city': 'vja', 'name2': 'siri'}
a={"idnos":[10,20,30],"name":["meghana","sharanya","sai"],"marks":[60,70,80]}
print(a)
{'idnos': [10, 20, 30], 'name': ['meghana', 'sharanya', 'sai'], 'marks': [60, 70, 80]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'name', 'marks'])
a.values()
dict_values([[10, 20, 30], ['meghana', 'sharanya', 'sai'], [60, 70, 80]])
a.items()
dict_items([('idnos', [10, 20, 30]), ('name', ['meghana', 'sharanya', 'sai']), ('marks', [60, 70, 80])])
a=[9,1,5,2,8,4,6,3,7,0]
#[7,6,4,3,0,9,8,5,2,1]
a1=a[0:5]
a1
[9, 1, 5, 2, 8]
a2=a[5:10]
a2
[4, 6, 3, 7, 0]
a1.sort()
a1
[1, 2, 5, 8, 9]
a2.sort()
a2
[0, 3, 4, 6, 7]
a1.reverse()
a1
[9, 8, 5, 2, 1]
a2.reverse()
a2
[7, 6, 4, 3, 0]
c=a2+a1
c
[7,6,4,3,0,9,8,5,2,1]

