#oops
#syntax
'''class classname():
    #attributes
    name="siri"
    age="21"
    place="vja"
    def fname(method_name):
        print("statements.........")
a=classname()
a.fname()'''

#class declaration
'''class details():
      name="siri"
      age="21"
      place="vja"
      def display(self):
          print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''

#object instantiation
'''class details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.data("siri",21,"vja")
a.display()
b=details()
a.data("sharanya",22,"vja")
a.display()'''

#object initialization
'''class Details():
      #creating a constructor
      def __init__(self,name,age,place):
          self.name=name
          self.age=age
          self.place=place
      def display(self):
          print(self.name,self.age,self.place)
a=Details("siri",21,"vja")
print(dir(a))
a.display()'''

#using runtime- method1
'''class Details():
      #creating a constructor
      def __init__(self,name,age,place):
          self.name=name
          self.age=age
          self.place=place
      def display(self):
          print(self.name,self.age,self.place)
a=Details(input("name"),int(input("age")),input("place"))
print(dir(a))
a.display()'''

#using runtime-method2
'''class Details():
      #creating a constructor
      def __init__(self):
          self.name=input("name")
          self.age=int(input("age"))
          self.place=input("place")
      def display(self):
          print(self.name,self.age,self.place)
a=Details()
a.display()'''

#diff b/w _ and __
#using 1 employee user
'''class employee():
    def __init__ (self):
        self.name="siri"
        self._mailid="siriatluri2005@gmail.com"
        self.__salary=10000#private variable
a=employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._employee__salary)'''

#using 3 employee users
'''class employee1():
    def __init__ (self):
        self.name="siri"
        self._mailid="siri2005@gmail.com"
        self.__salary=10000#private variable

class employee2():
    def __init__ (self):
        self.name="sharanya"
        self._mailid="sharu@gmail.com"
        self.__salary=20000#private variable

class employee3():
    def __init__ (self):
        self.name="mithra"
        self._mailid="mithra@gmail.com"
        self.__salary=30000#private variable
a=employee1()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._employee1__salary)
b=employee2()
print(dir(b))
print(b.name)
print(b._mailid)
print(b._employee2__salary)
c=employee3()
print(dir(c))
print(c.name)
print(c._mailid)
print(c._employee3__salary)'''


          
                
        
