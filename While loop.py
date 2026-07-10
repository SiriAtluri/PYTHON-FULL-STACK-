#While loop

'''a=10
while a>1:
    print(a)'''

'''a=10
while a<1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a>3:
    print(a)
    a=a-1'''

'''a=20
while a>3:
    a=a-1
    print(a)'''

'''a=20
while a>3:
    a=a-1
print(a)'''

'''a=40
while a>5:
    a=a-1
print(a)'''

#increment and Decrement using assignment operator

'''a=30
while a>1:
    print(a)
    a+=1'''

'''a=10
while a>2:
    print(a)
    a-=1'''

'''a=30
while a>1:
    print(a)
    a-=1'''

'''a=1
while a<25:
    print(a)
    a+=1'''
#real time examples using for loop 
#Voting using for loop
'''while True:
    age=int(input("enter the age:"))
    if age>=18:
            print("eligible for vote")
    else:
        print("not eligible for vote")'''

#Bakery  using for loop
'''while True:
    cake=int(input("enter the price:"))
    if cake==1200:
        print("redvelvet cake")
    elif cake==1000:
        print("almond cake")
    elif cake==800:
        print("chocolate cake")
    elif cake==600:
        print("butter scotch cake")
    else:
        print("cake is not available")'''

#leap year or not using for loop
'''while True:
    year=int(input("enter the year"))
    if year%4==0:
        print("it is leap year")
    else:
        print("it is not leap year")'''

#range()
#start-stop-step

'''for i in range(20):
    print(i)'''

'''for i in range(13,35):
    print(i)'''

#task1
#0,3,6,9,12,15,18,21,24,27
'''for i in range(0,30,3):
 print(i)'''

'''for i in range(0,30,3):
 print(i,end=",")'''

#task2
#5,10,15,20,25,30,35,40,45
'''for i in range(5,50,5):
  print(i)'''

'''for i in range(5,50,5):
 print(i,end=",")'''

#task3
#2,4,6,8,10,12,14,16,18
'''for i in range(2,20,2):
    print(i)'''

'''for i in range(5,50,5):
 print(i,end=",")'''

#grade code
'''while True:
    marks=int(input("enter the marks"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-C")
    elif marks in range(50,71):
        print("Grade-D")
    else:
        print("Fail,study well...")'''

#using for loop()
'''while True:
    marks=int(input("enter the marks"))
    for marks in range(91,101):
        print("Grade-A")'''













