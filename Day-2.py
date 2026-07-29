'''
Tokens --> Variables,Punctuators

Variables -->Named memory location,its a placholder for data
#Rules are to followed 

#Multiassignment of variables

name,age,place ='codeganan',7,'hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='------>')

#a,b =2,4,5 #valueerror as too many values to unpack
#Reassigning variables

name = "Hariganesh"
a,b = 45,1.5
print(a,b)
a,b = b,a #Swapping
print(a,b,sep=',')

#a,b = b,c #Nameerror as c is not defined
#print(a,b)

#Deleting the variables -->del
#del a
#print(a)
del a,b
print(a,b)

#Punctuator --> [](Lists),()(tuples),{}(dict,sets)
name = "hari";age =7;course = 'Data analysis'
print(name,age,course)
print(name)
print(age)
print(course)

#Datatypes --> Numric (int,float,complex),boolean,none,
            #-->Sequences -->Lists,Tuple,Sets,Strings,
                #        Frozensets,mapping(dict)

#Numeric type -->int,float,complex

#int datatype -->quantity,age..
age = 7
print(age)
print(type(age)) #type --> returns the datatype of object

print(type(234))

#quantity  = 03 #it is not allowed
#print(quantity)

#float datatype -->temp,salary,price
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))

#complex -->combination of real and imag
i2 = 4
data = 5 +i2
print(data)

data = 5+2j # j is img representation
print(data)
print(type(data))

#Boolean --> True / Flase

valid = True
print(type(valid))

error = False
print(type(error))

#TypeCasting --> Converting one type to another type
#Python by default fillows Implict type  ( we need to mention the datatype)

#We wiil goo for Explicit Convertion

#Every built-in datattype is a built-in function
#int,float,complex,bool

#Typecasting --> int -->float,complex,bool


age=25
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age) #return True for existing data
print(d)
e = bool(0)
print(e)

#float --> Typecasting
mark =5.5
print(type(mark))
d = int(mark)
print(d)
print(type(d))
e = complex(mark)
print(e)
print(type(e))
f = bool(mark)
print(f)
print(type(f))


#Complex -->Typecasting --> int,float,bool
data = 3+5j
print(type(data))
# complex is con not change int /,float format
d = bool(data)
print(d)
print(type(d))

e = int(float(bool(45)))
print(e)

e = bool(int(float(25)))
print(e)
'''
f = 35+1.5+2j+False
print(f)





      














