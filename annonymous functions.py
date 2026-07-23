#write a function to calculate 2*x+5 where x=5
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input("value"))
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

'''a=lambda x,y:x*y
print(a(3,5))'''

'''x=int(input())
y=int(input())
z=lambda x,y:x*y
print(z(x,y))'''

'''a="codegnan"
#CODEGNAN
b=lambda a:a.upper()
print(b(a))'''

'''a=lambda a:a.upper()
print(a("codegnan"))'''

'''a="python course"
#Python Course
b=lambda a:a.title()
print(b(a))'''

'''a=lambda a:a.title()
print(a("python course"))'''

#firstname+lastname=fullname
'''fname,lname=[x for x in input("enter the names").split(",")]
fullname=lambda fname,lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

#filter()
a=[10,30,50,100,127,39,45,67,200]
'''if a%2==0:
   print(a)'''

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))

b=[]
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

'''a=[[],(),set(),{}," ",None,5,8.9,"python",5+9j,True,False]
b=list(filter(None,a))
print(b)'''





    







