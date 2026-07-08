#conditions
#if-condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print("true")'''

'''a=10
b=20
if a>b:
    print("true")'''

'''a=5
b=7
if a<=b:
    print("less")'''

'''a=12
b=15
if a>=b:
    print("true")'''

'''a=30
b=40
if a!=b:
    print("true")'''

'''a=10
b=10
if a==b:
    print("true")'''

'''a="python"
if a=="python":
    print("match")'''

'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''

'''a=int(input("a value"))
if a<50:
    print("less")'''

#if condition using logical operators
#and,or,not

'''a=3
b=6
if a<b and b>a:
    print("true")'''

'''a=4
b=7
if a<=b and b>=a:
    print("true")'''

'''a=9
b=12
if a!=b and b==a:
    print("true")'''

'''a=2
b=4
if a<b or b>a:
    print("true")'''

'''a=14
b=16
if a<=b or b>=a:
    print("true")'''

'''a=3
b=6
if a!=b or b==a:
    print("true")'''

'''a=5
b=7
if not a<b:
    print("true")'''

'''a=3
b=6
if not a>b:
    print("true")'''

'''a=3
b=6
if not a<b and b>a:
    print("true")'''

'''a=3
b=6
if not a<b or b>a:
    print("true")'''

#if-conditions by using identify operators
#is, is not

'''a=4
if type(a) is int:
    print("is is int")'''
'''a=4
if type(a) is not int:
    print("is is int")'''

'''a=5.3
if type(a) is float:
    print("is float")'''

'''a=5.3
if type(a) is not float:
    print("is float")'''

'''a="siri"
if type(a) is str:
    print("is string")'''

'''a="siri"
if type(a) is not str:
    print("is not string")'''

'''a=2+4j
if type (a) is complex:
    print("is complex")'''

'''a=2+4j
if type (a) is not complex:
    print("is complex")'''

'''a=True
if type(a) is bool:
    print("is boolean")'''

'''a=True
if type(a) is not bool:
    print("is boolean")'''
#using run-time

'''a=int(input("value: "))
if type(a) is int:
   print("is interger")'''

'''a=float(input("value: "))
if type(a) is float:
   print("is float")'''

'''a=str(intput("value: "))
if type(a) is str:
    print("is string")'''

'''a=complex(input("value: "))
if type(a) is complex:
    print("is complex")'''

'''a=bool(input("value: "))
if type(a) is boolean:
    print("is boolean")'''

#if-condtions by using membership operators

'''a=2,3,4,5,6,7,8
if 8 in a:
    print("true")'''

'''a=2,3,4,5,6,7,8
if 20 not in a:
    print("true")'''

'''a=int(input())
if 30 in a:
    print("true")'''#error

'''a=2,3,4,5,6,7,8,9,10
b=int(input("value"))
if b in a:
    print("true")'''

#if-else conditions by using comparision operators
'''a=4
b=8
if a<b:
    print("less")
else:
    print("false")'''

'''a=4
b=8
if a>b:
    print("less")
else:
    print("false")'''

'''a=4
b=8
if a<=b:
    print("less")
else:
    print("false")'''

'''a=4
b=8
if a>=b:
    print("less")
else:
    print("false")'''

'''a=4
b=8
if a == b:
    print("equal")
else:
    print("false")'''

'''a=4
b=8
if a != b:
    print("not equal")
else:
    print("false")'''

#if-else conditions by using logical operator

'''a=3
b=6
if a<b and b>a:
    print("true")
else:
    print("false")'''


'''a=4
b=7
if a<=b and b>=a:
    print("true")
else:
    print("false")'''

'''a=9
b=12
if a!=b and b==a:
    print("true")
else:
    print("false")'''

'''a=2
b=4
if a<b or b>a:
    print("true")
else:
    print("false")'''

'''a=14
b=16
if a<=b or b>=a:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if a!=b or b==a:
    print("true")
else:
    print("false")'''

'''a=5
b=7
if not a<b:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if not a>b:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if not a<b and b>a:
    print("true")
else:
    print("false")'''

'''a=3
b=6
if not a<b or b>a:
    print("true")
else:
    print("false")'''

#if-else conditions by using identify operator

'''a=4
if type(a) is int:
    print("is int")
else:
    print("not int")'''

'''a=4
if type(a) is not int:
    print("is not int")
else:
    print("is int")'''

'''a=5.3
if type(a) is float:
    print("is float")
else:
    print("not float")'''

'''a="siri"
if type(a) is str:
    print("is string")
else:
    print("not string")'''

'''a="siri"
if type(a) is not str:
    print("is not string")
else:
    print("is string")'''

'''a=2+4j
if type(a) is complex:
    print("is complex")
else:
    print("not complex")'''

'''a=2+4j
if type(a) is not complex:
    print("is not complex")
else:
    print("is complex")'''

'''a=True
if type(a) is bool:
    print("is boolean")
else:
    print("not boolean")'''

'''a = True
if type(a) is not bool:
    print("is not boolean")
else:
    print("is boolean")'''

#if-else conditions by using membership operator

'''a=2,3,4,5,6,7,8 
if 8 in a:
    print("true")
else:
    print("false")'''

'''a=2,3,4,5,6,7,8
if 20 not in a:
    print("true")
else:
    print("false")'''

'''a=2,3,4,5,6,7,8,9,10
b=int(input("value: "))
if b in a:
    print("true")
else:
    print("false")'''

#if-elif-else
#if-elif-else using a comparison operator
'''a=4
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")'''

'''a=4
b=6
if a==b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")'''

'''a=4
b=6
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("true")'''

'''a=4
b=6
if a==b:
   print("less")
elif b<a:
    print("greater")
else:
    print("true")'''

#if-elif-else using logical operator  

'''a=10
b=15
if a<b and b>a:
    print("less")
elif a!=b or a==b:
    print("equal")
elif not b>a:
    print("false")
else:
    print("false")'''

'''a=4
b=6
if a<b and b>a:
    print("true")
elif a>b and b<a:
    print("false")'''

'''a=4
b=6
if a>=b and b<=a:
    print("less")
elif a<=b and b>=a:
    print("greater")
else:
    print("true")'''

'''a=4
b=6
if a==b and a!=b:
    print("less")
elif a>=b and b<=a:
    print("greater")
else:
    print("true")'''

'''a=4
b=6
if a<b or b>a:
    print("true")
elif a>b or b<a:
    print("false")'''

'''a=4
b=6
if a<=b or b>=a:
    print("less")
elif a>=b or a!=b:
    print("high")
else:
    print("true")'''

'''a=4
b=6
if a==b or a>=b:
    print("true")
elif a<=b or b<=a:
    print("false")
else:
    print("less")'''

'''a=4
b=6
if not a>b:
    print("less")
elif not a<b:
    print("more")'''

'''a=4
b=6
if not a<=b and b>=a:
    print("less")
elif not a>=b or b<=a:
    print("more")
else:
    print("high")'''

#identify
'''a=5
if type(a) is int:
    print("it is int")
elif type(a) is not int:
    print("false")'''

'''a=5
if type(a) is int:
    print("true")
elif type(a) is not int:
    print("false")'''

'''a=5.6
if type(a) is float:
    print("true")
elif type(a) is not float:
    print("false")
else:
    print("less")'''


'''a="hi"
if type(a) is str:
    print("true")
elif type(a) is not int:
    print("false")
else:
    print("less")'''   


'''a=4+8j
if type(a) is complex:
    print("true")
elif type(a) is not complex:
    print("false")
else:
    print("less")'''


'''a=True
if type(a) is bool:
    print("true")
elif type(a) is not bool:
    print("false")
else:
    print("less")'''

#membership
'''a=1,2,3,4,5,6,7,8   
b = int(input())
if 8 in a:
    print("true")
elif 8 not in a:
    print("false")'''

'''a=1,2,3,4,5,6,7,8
if b in a:
    print("true")
elif b not in a:
    print("false")
else:
    print("less")'''

#multiple-if conditions using comparision operators
'''a=20
b=40
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''
 
'''a=20
b=40
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=20
b=40
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")'''

'''a=20
b=40
if a==b:
    print("less")
if b>a:
    print("greater")
if a>=b:
    print("not equal")
else:
    print("true")'''

#multiple-if conditions using logical operators
'''a=40;b=90
if a<b and b>a:
    print("true")
if b>a and a<b:
    print("false")
if a==b or a!=b:
    print("else")'''
    
'''a=40;b=50
if a<=b and a>=b:
    print("less")
if a<=b and b>=a:
    print("true")
if a==b or b>=a:
    print("false")'''

'''a=80;b=90
if a<=b and b>=a:
    print("true")
if b>=a and a<=b:
    print("false")
if not a>=b or a<=b:
    print("high")
else:
    print("less")'''

#multiple-if conditions using membership and identify operators
'''a=1,2,3,4,5,6,7
if 8 in a:
    print("true")
if 6 in a:
    print("true")
if 7 in a:
    print("true")
if 8 not in a:
    print("false")'''


'''if 8 in a:
    print("true")
elif 7 in a:
    print("true")
elif 8 in a:
    print("true")
elif 2 in a:
    print("true")
else:
    print("false")'''

#nested if conditions
'''a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=4
b=9
if a>b:
    print("less")
    if b>a:
        print("greater")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")'''

'''a=13
b=15
if a==b:
    print("true")
    if b>a:
        print("greater")
else:
    print("false")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("greater")
    else:
        print("false")
else:
    print("not true")'''

'''a=20
b=25
if a!=b:
    print("true")
    if b==a:
        print("greater")
    elif a<b:
        print("less")
    else:
        print("false")'''

'''a=int(input())
b=int(input())
if a!=b:
    print("true")
    if b==a:
        print("equal")
    elif b>a:
        print("greater")
    else:
        print("false")
else:
    print("program ends")'''












    




    
    
    



    
