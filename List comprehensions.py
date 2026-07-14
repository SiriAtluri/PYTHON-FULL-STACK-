#list compehension 
a=["codegnan","python","course"]
#["CODEGNAN","PYTHON","COURSE"]
#print(a.upper())
 
'''b=str(a)
 print(b.upper()))'''
 
'''for i in a:
     print(i.upper(),end=",")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''  

#syntax
#a=[expression for var in collection/range]
'''a=[i.upper() for i in a]
print(a)'''

b=["vja","hyd","vzg"]
#["Vja","Hyd","Vzg"]
'''b=[i.title() for i in a]
print(b)'''

b=[1,2,3,4,5,6,8,12,13]
#[1,4,9,25,36,64,144,169]
'''a=[i*i for i in a]
print(a)'''

'''b=[pow(i,2) for i in a]
print(a)'''

'''a=[i**2 for i in b]
print(a)'''

#if-usage in list comprehension
'''a=[i for i in range(16)]
print(a)'''

'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''a=[i for i in range(16) if i%2!=0]
print(a)'''

'''a=[i for i in range(21) if i%2==0*i]
print(a)'''

a=["apple","banana","grapes","mange","kiwi","dragon","berry"]
'''b=[i for i in a if "a" in i]
print(b)'''

'''b=[i for i in a if "a"  not in i]
print(b)'''

#no-elif usage in list comphension 
#if-else usage 
'''a=[i**2 if i%2==0 else i*5 for i in range(31)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
'''c=a+b
print(c)'''

'''c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

'''c=[a[i]+b[i] for i in range(len(a))]
print(c)'''




