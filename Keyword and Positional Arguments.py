# Keyword and Positional Arguments
'''def Details(id,name,mailid):
    id=10
    name="siri"
    mailid="siri.atluri@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="sita",mailid="sita@gmail.com")
Details(id=30,name="rama",mailid="rama@gmail.com")
Details(40,"sharanya","sharu@gmail.com")
Details("meghana@gmail.com",50,"maggi")
Details(mailid="honey@gmail.com",id=60,name="honey")'''
# Default Arguments
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",100)'''

'''def Grocery(item="rice",price=1500):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''
#A Non-default Argument Cannot Follow a Default Argument
'''def Grocery(item="ghee",price): 
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''

#task
'''def bakery(cake_name,price,qty):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %d kg/g" %qty)
bakery("dark chocolate",2000,1)'''

'''def bakery(cake_name="butter scotch",price=2500,qty=2):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %d kg/" %qty)
bakery()'''

'''def bakery(cake_name,price=3500,qty=3):
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %d kg/g" %qty)
bakery("black forest")'''
#non def arg follows def arg
'''def bakery(cake_name="red velvet",price=3500,qty): 
    print("cake is %s" %cake_name)
    print("price is %.2f" %price)
    print("quantity is %d kg/g" %qty)
bakery(3)'''

# * arguments(* is used to unpack the elements)
# Unpacking a List
'''a=[2,3,4,5,6,7]
print(a)
print(*a)'''
# Unpacking a Tuple
'''a=(2,3,4,5,6,7)
print(a)
print(*a)'''
# Unpacking a Set
'''a={2,3,4,5,6,7}
print(a)
print(*a)'''
# Unpacking Dictionary Keys
'''b={"name":"yashu","city":"vij"}
print(b)
print(*b)'''
# Unpacking a String
'''c="python"
print(c)
print(*c)'''
# Incorrect Multiple Assignment (Too Many Values)
'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(c)'''#error
# Correct Multiple Assignment
'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''
# Using * with Multiple Assignment
'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''
# Incorrect String Unpacking
'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''#error
# Correct String Unpacking
'''a,b,c="cod"
print(a)
print(b)
print(c)'''
# Using * to Unpack Characters from a String
'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''


    




















