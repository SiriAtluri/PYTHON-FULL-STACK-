#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[4,5,6,7,8]
check(*b)
c={5,6,7,8,9,10}
check(*c)
d={"name":"siri","age":23,"place":"vja"}
check(*d)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"python",4+9j,True,False)'''

#**(kwargs)-keyword variable length arguments
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["siri","maggi","netra"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''

'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check2()
details={"names":["siri","maggi","netra"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''

# Both * and ** usage
'''def final(*a,**b):
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5,6,3.5,7.8)
final(*data)
details={"year":[2026,2027,2028],
         "month":["june","july","aug"]}
final(**details)
final(*data,**details)'''

#railway Ticket

'''def railway_ticket():
    ticket=1000
    gender=input("enter the gender")
    age=int(input("enter the age"))
    if gender=="m":
       if age>=60:
          print("senior citizen")
          ticket=ticket-30/100*ticket
          print(ticket)
    elif age<60:
         print("normal citizen")
         print(ticket)
    elif gender=="f":
         if age>=60:
            print("senior citizen")
            ticket=ticket-50/100*ticket
            print(ticket)
    elif age<60:
         print("normal citizen")
         ticket=ticket-30/100*ticket
         print(ticket)
railway_ticket()'''




        

                
            
        




