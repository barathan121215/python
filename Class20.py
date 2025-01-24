#Class: 20
#Date: 2025-01-18
#Topic: Project2
var="central processing unit"
varsplit=var.split()
print(varsplit)
result=""
for i in varsplit:
    #print(i) 
    result=result+i[0].upper()
print(result)
print("\n")
var="central processing unit"
varsplit=var.split()
print(varsplit)
result=""
'''
for i in varsplit:
    #print(i) 
    result=result+i[len(i)-1].upper()
print(result)
print("\n")
var="central processing unit"
varsplit=var.split()
print(varsplit)
result=""
for i in varsplit:
    #print(i) 
    result=result+i[-1].upper()
print(result)


central
1234567
0123456

processing
1234567890
0123456789
'''
import time
print("hello world")
# time.sleep(5)
print("python is my favorite coding language")

import datetime
current_date=datetime.datetime.now()
print(current_date.year)
print(current_date.hour)
'''
str='central'
for i in str:
    print(i)


str=['central','pr','xx']
for i in str:
    print(i)
'''    