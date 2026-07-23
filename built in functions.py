#built-in functions
#print(dir())
#print(dir("__builtins__"))
#fromkeys()
'''a="codegnan"
print(a)
print(list(a))
print(tuple(a))

print(set(a))
#print(dict(a))
b=dict.fromkeys(a)
print(b)

c=dict.fromkeys(a,"siri")
print(c)

c["d"]="python"
print(c)'''

#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''


'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multuple collections
#into on collection

'''a=[10,20,30,40,50]
names=["siri","sharanya","mithra","devi","meghana"]
print(a+names)'''

'''b=zip(a,names)
print(b)'''

'''c=list(zip(a,names))
print(c)'''

'''c=tuple(zip(a,names))
print(c)'''

'''c=set(zip(a,names))
print(c)'''

'''c=dict(zip(a,names))
print(c)'''

#enumerate()->we cann give counter to the collection
names=["nikitha","taruni","siri","kalyani","prameela"]

'''for i in range(len(names)):
    print(i,names[i])'''

'''b=list(enumerate(names))
print(b)'''

'''b=list(enumerate(names,10))
print(b)'''

'''b=dict(enumerate(names,100))
print(b)'''

#ASCII (American Standard Code for Information Interchange)
#chr()
#ord()

'''print(chr(65))

print(chr(90))

print(chr(92))'''

'''print(ord("a"))

print(ord("z"))

print(ord("y"))'''

#Print capital letters A-Z
'''for i in range(65,91):  
    print(chr(i),end=" ")'''

#Print small letters a-z
'''for i in range(97, 123):  
    print(chr(i), end=" ")'''

#ASCII codes for names
'''a=input("enter the name")
for i in a:
    print(i,"-",ord(i))'''

#BMI Calculator
'''while True:
    weight=float(input("Enter your weight in kg: "))
    height=float(input("Enter your height in meters: "))
    bmi=weight/(height**2)
    if bmi<=18.5:
        print("Category:Under weight")
    elif bmi<=18.5 and bmi<24.5:
        print("Category:Healthy weight")
    elif bmi>24.5 and bmi<=29.5:
        print("Category:Over weight")
    elif bmi>30.5:   
        print("Category:Obesity")'''


    








