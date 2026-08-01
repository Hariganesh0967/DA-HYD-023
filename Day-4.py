'''#identity opertors ---> checks the identity of an object---v.id()
a=5
b=5
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)
print(5==5)




a=[1,3,5,6]
b=a
print(id(a))
print(id(b))
c=[1,3,5,6]
print(id(c))
#as we have lists(mutable collection) both c and a lists will have different
#ids whereas vaues are same
print(c is a)#output are sum
print(c==a)#ouput True
print(a is not c)


#bitwise opertors ---> we perform bitwise opertion over operands
# & (and),|(or),^(xor),shifting opertors(<<,>>)
# Number will be converted to binary format
print(5&3)#both 5 and 3 to be converted binary and bitwise and is performed
print(5|3)#bitwise OR
print(5^3)#bitwise XOR
print(5 and 3)#here and is logical operator checks for both existance
#returns 5 in above case
print(5 or 3)#returs 3 in this case

#leftshift operator <<,right shift operator>>
print(5<1)#False comparision
print(5<<1)#leftshift-->1 part
print(5>>1)#rigthshift-->1



print(15<<2)#convert is to binary and perform 2 times left shifting
print(15>>2)#same 2 times rigth shifting



#input formatting---> input(),int(input()),float(input())
#you knoe--->single input
#2 or 3 inputs ---> map()
#group of integers-->list(map(int,input().split(','))
names = input("enter the names:").split(',')
print(names)
name1,name2 = map(str,input("enter the friends names:").split(','))
print(name1,name2)
'''
#tokens ---> numeric datatypes --->operators -->flow of the program
#control block statements ---> they control the flow of the program
#when to execute,how to execute
#conditional statements--->if,else,elif (rely on condition to be executed)
#repetional statements(loops)--->for while
'''
syntax:
    if <condition>
    statement(s)...
    ....

#age = 15
age = int(input("enter the age"))
if age > 18:
    print('your age is ',age)

age = int(input("enter the age:"))
if age>=18 and age in[19,21,22]:
    print('your age is ',age)
print(age)


#else keyword--->if-else
else:
    statement(s)..
    if-else usage as below:
        if <condition>:
            statement(s)...
            ...
else:
    statement(s)....
    ....
'''
#vote elibility -->to check his/her voter eligibilty and give access..

age = int(input("enter the age:"))
if age>=18:
    print("you have voter eligibilty and agfe is",age)
    print("access granted")
else:
    age=18-age
    #print("you dont have eligibility as your age is",age)
    print("you need to wait for more",age,"years")
#same case let's use only nested ---> if,else
if age >0:
    if age >=18:
        print("you have voter eligibilty and agfe is",age)
        print("access granted")
else:
    print("you have entered -ve values/zero enter only +ve")


task i stuent markis and grade analayzer
90-100-->'A'
80-89-->'B'
70-79-->'C"
60-69-->'D'
-60-->fail
#also -ve cases should not be allowed and marks shouldnt be greater 100
