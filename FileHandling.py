#File Handling
#write()
'''a=open("siri.txt","w")
a.write("codegnan")
a.close()'''

'''a=open("siri.txt","w")
a.write("python full stack")
a.close()'''

#append()
'''a=open("siri.txt","w")
a.write("\tdata science")
a.close()'''

'''a=open("siri.txt","w")
a.write(input("data"))
a.close()'''

'''a=open("siri.txt","w")
b=input("data")
a.write(b)
a.close()'''

'''a=open("siri.txt","w")
b=input("data")
a.write(b)
a.close()'''

#read()
'''a=open("siri.txt")
print(a.read())  #it will display entire content
print(a.readline()) #it will display first line
print(a.readlines()) #it will display 
print(a.read(8)) # it will display no.of characters'''

#writelines()#it makes every object side by side
'''a=open("siri.txt","w")
b=["siri","sai","mithra","kalyani","prameela"]
a.writelines("\n".join(b))
a.close()'''

'''a=open("for loop.py")
print(a.read())'''

a=open("C:\\Users\\atlur\\OneDrive\\Desktop\\PFS-037\\Functions.py")
print(a.read())



