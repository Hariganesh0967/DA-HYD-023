'''
student marks and grade analayzer (if-else)
90 - 100 -->'A'
80 - 89 -->'B"
70 - 79 -->'c'
60 - 69 -->'D'
<60 --> Fail
#also -ve case should not be allowed and marks shouldnt be greater 100
'''
'''
marks = int(input("Enter the marks (1-100):"))
if marks > 0 and marks <=100:
    if marks >= 90 and marks <= 100:
        print("User has secured Grade A")
    if marks >= 80 and marks <= 89:
        print("(User has secured Grade B")
    if marks >= 70 and marks <= 79:
         print("(User has secured Grade C")
    if marks >= 60 and marks <= 69:
        print("(User has secured Grade D")
    if marks < 60:
        print("User has failed,study again")
else:
    print("Enter only +ve values greater than 0 and less than 100")
 '''
#elif keyword --> if-else-else
'''
if<condition1>:
   statement(s).....
   ......
elif<condition2>
     statement.....
    .....
elif<condition3>.....
     statement.....
    .....   
else:
     statement(s)...
     ......
'''
'''
marks = int(input("Enter the student marks:"))
if marks >=100:
    print("Entered values should be greater than 1 less than 100")
elif marks >= 90 and marks <= 100:
        print("User has secured Grade A")
elif marks >= 80 and marks <= 89:
        print("(User has secured Grade B")
elif marks >= 70 and marks <= 79:
         print("(User has secured Grade C")
elif marks >= 60 and marks <= 69:
        print("(User has secured Grade D")
elif marks < 60:
        print("User has failed,study again")
else:
    print("No negative valuse")

#Task --> same usecase  try with if-elif-else usege the other way
'''
'''
#Voter Eligibiliity checkcase -->make sure to satisfy all possible cindition:
#>=18 and 100 -->Access
#<18 --> no of years eligibility should tell
#negative values --> not acceptable

age = int(input("Enter the age:"))
if age>=18 and age <=100:
    print('------ User has VOte Eligibility -----')
    print('------ Access Granted ------')
elif age<18 and age>0:
    print('------ User still need to get Vote Eligibility -----')
    print('------ User need to wait for more',(18-age),'year(s)-----')
else:
    print('------ Only +ve values and less than 100 Acceptable----')

 #perfer if-elif-else....
'''
'''
#Output -->print()    
#Output fromatting --> old stlye formating (using commas)
#% usage (%f,%d),.format() usage,fstring notation
a,b= 7,9
print(a)
print(b)
print(a,b)
name = "Codegnan";batch = "Data analysis"
print(name,batch)#by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep=' ----->')
#end='\n','\t --->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("hyderabad")
'''

name='Codegnan';age=7;batch='DA-023';place='Hyderabad'
#Usage of commas
print(batch,'is in',name)#variables and msg to be sepetrated by comma
print(name,'is in',place,'age is',age,'years')
#Old style formatting --> %d -->integer,%s-->string,%f-->float
Salary = 24235.256
print("His Salary is %d"%(Salary))
print("His Salary is %f"%(Salary))
print("His Salary is %.1f"%(Salary)) #%.1f ---> rounding to 1 decimal

#.format() usage
print("{}is in {}".format(name,place)) #order matters
#fstring usage (more recommended)
print(f'{name}is in {place}')
print(f'{ganesh} is in {hyderabad}')
      
