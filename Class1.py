#EX1-printing contents 
print("barathan")
print(8)
print("m.a.v.vidyashram")

#EX2 - Assigning variables
fname="Barathan"
sname="rakesh"
age=8
school_name="m.a.v.vidyashram"
mark1=79.9
mark2=79.8
mark3=79.7
mark4=79.6
mark5=79.5
print(fname)
print(sname)
print(age)
print(school_name)
print(mark1)
print(mark2)
print(mark3)
print(mark4)
print(mark5)
print(fname+sname)
print(fname+" "+sname)
print(fname,sname)

#EX3 - printing types of variables 
print(type(fname))
print(type(sname))
print(type(age))
print(type(mark1))

#EX4 - using predefined functions & methods
print(len(fname)) #len() can only be applied to strings
#print(len(age))
#print(len(mark1))
'''
Traceback (most recent call last):
  File "<main.py>", line 35, in <module>
TypeError: object of type 'float' has no len()
'''

print(fname.capitalize())
print(sname.capitalize())
#print(age.capitalize())

print(fname.upper())
#print(age.upper())

print(fname+" "+sname.title())
name = fname + " " + sname.title()
print(name)
print(type(name))
name1 = fname,sname
print(name1)
print(type(name1))

fruits = "apple"
print(fruits)
print(type(fruits))

fruits = ('apple','mango','papaya')
print(fruits)
print(type(fruits))

print(fname)
fname = 'Sathiya'
print(fname)