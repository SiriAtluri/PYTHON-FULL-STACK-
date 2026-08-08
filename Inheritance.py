#single inheritance
'''class RBI():#parent class
    cash=100000
    def available_cash(cls):
        #print("available_cash is",cls.cash)
        print("available_cash is",RBI.cash)
class SBI(RBI):#child-1
   pass
class HDFC(RBI):#child-2
   cash=50000
   def new_cash(cls):
       #print("new cash is",cls.cash+cls.cash)
       print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''
    
#multiple inheritance
# Parent class Father
'''class Father:
    def height(self):
        print("height is 5.5 inches")
class Mother:
    def weight(self):
          print("weight is 60kgs")
class kid():
    def dob(self):
        print("just born")
a=Father()
b=Mother()
c=kid()
a.height()
b.weight()
c.dob()'''

#multi-level inheritance
'''class Grandparent():
      def land(self):
        print("10 acres")
class parents(Grandparent):
      def house(self):
          print("100 sqft")
class child(parents):
      def car(self):
          print("BMW")
a=child()
a.land()
a.house()
a.car()'''

#hierarchical inheritance is where one parent class is inherited by multiple child classes
'''class employee():
      def company(self):
          print("codegnan it solutions")
class trainer(employee):
      def teaching(self):
          print("trainer teach the code")
class developer(employee):
      def code(self):
          print("developer develops the code")
a=trainer()
a.teaching()
a.company()
b=developer()
b.code()
b.company()'''

#hybrid inheritance means combing more than one type of inheritance for example hierarchical + multiple inheritance 
'''class Person():
    def Details(self):
        print("Siri")
class Trainer(Person):
    def Teaching(self):
        print("Trainer teaches the subject")
class Student(Person):
    def study(self):
        print("preparing for exam")
class Program_manager(Student,Trainer):
    def manager(self):
        print("manages the class")
a=Program_manager()
a.Details()
a.Teaching()
a.study()
a.manager()'''

#Super()
'''class parent():#super class
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):#sub class
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("siri",21)
print(dir(a))
print(a.name)
print(a.age)'''

          





     
