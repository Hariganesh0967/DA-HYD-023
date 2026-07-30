#Numric datatype --> int, float,complex along with boolean

#Input formatting --> Accepting input from the user -->input()

#Accepting integer inout form user
#by default input() accepts any input -->str
#int(input()) --> will accept only integers
'''
age =int(input('Enter the age:'))
print(age)
print(type(age))
'''
'''
#float(input()) --> accepts integer,float values
age =float(input('Enter the age:'))
print(age)
print(type(age))
'''
'''
#Accepting string input from user

name =input("Enter the name :")
print(name)
print(type(name))
'''
'''
#Acceepting group of values

marks = int(input('Enter the marks:')).split()
print(marks)

a =  input().slpit # by default split() has  space
print(a)'''
'''
#space separated values
a = input().split() # now you enter space in output
print(a)

#comma separated values
a = input("Enter the values:").split(',')
print(a)'''
'''
#List of integers
marks = list(map(int,input("Enter the values:").split(',')))
print(marks)'''
'''
#Now we want to accept 2 values from user
age,salary= map(int,input("Enter the values:").split(','))
print(age)
print(salary)

#Single input -->int(input())
#two input -->a,b = list(map(int,input().split(',')))
#any number result as list -->a =list(map(int,input().split(',')))
'''
'''
age,salary= map(float,input("Enter the values:").split(','))
print(age)'''
'''
#float of integers
marks = list(map(float,input("Enter the values:").split(',')))
print(marks)'''
'''
#group of float values
age,salary =map(float,input("Enter the values:").split(','))
print(age)
print(salary)'''
'''
#Accepting input from user --> int,float -> input format

#Opeators --> Operators perform operations between values (operation)
#7 types --> Arthmetic,Assignment,Comparision (Relationship)
#Membership,Identity,Logical,Bitwise

#Arthmetic Operator -->Arthmetic operations
#+,-,*,/
print(5+2)
print(5-3)
print(5*3)
print(5/3)#float value
#floor Division (Integer division)-->returns quotient
print(5//3)
#Modulus -->divisible rules ->returns remainder
print(5%3)
#Power (exponential)
print(5**3)
'''
'''#Task-->Accept interger input as length,breadth -->find the area of rectangular
#Area = length*breadth
length,breadth =map(int,input("Enter the value:").split(','))
area = length*breadth
print(area)'''
'''
#Assingment operators -->assign the values
# =, +=, -=
a =45
print(a)
#update value of the a
a = a + 5 #a+=5
print(a)
b =35
b += a #b = b + a
print(b)
b -= 5
print(b)

#Task : *=,/=,//=,%=,**= workout'''

'''
#Comparision Operators --> we compare the values --> boolean
# ==(eqaul to),!= (not eqaul to), >(greathan),<(less than )
# <= (less than or equal to),>= (greater than or equals to)

age = 21
print(age == 21) #returns Boolean output
print(age !=22)
print(age < 21)
print(age <= 21)
print(age > 22)
print(age >= 22)

print(-5 < -1)'''
'''
#Membership Operators --> in,not in--> boolean
# it checks for the existance of an object in a collection

marks = [26,24,27,28]
print(35 in marks)
#print(35 in 355)#Typeerror

print( 25 not in marks)
print('code' in 'codegnan')
print('$' in 'abc$fds')'''
'''
#Logical Operators --> logical decision making --> and,or,not
#and --> alla conditions to be satisified
#or --> any one condition to be satisified

a = (21 in [21,23,24]) and 45 < 55
print(a)
b = 45 > 55 or 21 <= 23
print(b)
c = not (True)
print(c)'''
'''
#Identity Operators --> check for identity of an object --> id()

a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)'''

a = [1,3,4,5]
print(id(a))
c = a
print(id(c))
print(c is a)
b = [1,2,3,4,5]
print(id(b))



     




    










