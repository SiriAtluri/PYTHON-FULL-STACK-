#exception handling
#except:exceptions are raised in try block it will be handle by this block
#else:optional(no exceptions)
#finally:always it will display
'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends.........")'''

#regex (regular expressions)
'''a="codegnan is in vijayawada"
print(a)'''

'''a="codegnan\nis\tin\nvijayawada"
print(a)'''

#rstring
'''a=r"codegnan\nis\tin\nvja"
print(a)'''

#compile(),search(),findall(),split(),sub()
#sequence characters
'''\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D->it matches non-digit
\s->it represents white spaces
\S->it represents non-white spaces'''

#compile()
'''import re
a="mat cat cap maths money cash code cup dog donkey mug"
b=re.compile(r"m\w\w\w\w")
print(b)'''

#search()
'''c=b.search(a)
print(c)

b=re.search(r"m\w+",a)
print(b)'''

#findall()
'''c=re.findall(r"d\w+",a)
print(c)'''

#split()
'''d=re.split(r"m",a)
print(d)

e=re.split(r"\s",a)
print(e/e)'''

#sub()
'''f=re.sub("m","a",a)
print(f)'''

'''a="year 2026 month 7 date 29"
b=re.findall(r"\d+",a)
print(b)'''

'''e="code dog donkey"
f=re.findall(r"\bd\w+",e)
print(*f)'''





