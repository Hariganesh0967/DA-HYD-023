'''
Control statements -->  control of Flow of execution of the program 
                         --> Conditional Statement --> if,elif,else....
                -->Repetition Statements(Loops) --> for,while (for with else)(while with else)
                -->Jumping Statement -->breaks,continue,pass
'''

#Loops --> Loops are helpful for repettion (Automative tasks)
#forn keyword will be helpful to iterate over a sequence / range 
#Syntax for (for keyword):
'''
for  <temp_var> in sequence/range:
      statement(s)....
      ......
'''
'''
#range(start,stop,step)
#by defualt range picks 0 as start value
for i in range(10):
    print(i)
'''
'''
#In above case we got 10 iteration
for i in range(1,10):
    #if i > 5:
        #print(f'Value of i is -->{i}')
    #Now i want to get only even numbers with above condition
    if i > 5 and i%2 == 0:
        print(f'Final Value of i is -->{i}')
'''
'''
#range (start,stop,step) -->here step --> interval..
for i in range(1,10,4):
    print(i)
    print("Done")'''
'''
for i in  range(10,0,-1):
    print(i)'''
'''    
#print -10 to -1
for i in range(-10,0,1):
    print(i)'''
'''
#[] --> we generally lists
names = ['hari','ganesh','poori']
print(len(names)) #len(obj) -->  returns the number of items in a container
for name in names:
    #print(name)
    #print(f'student Name is {name}')
    if name =="ganesh":
        print(f"student Name is {name}")'''

#Calculate the sum of first 10 numbers
#first understand your input --> range(11) -->10 numbers
#second understand your output --> sum (number)
#third we need to map logic
'''
result = 0 #terget variable
for i in range(11):
    #print(i)
    #print(f'result is {i=i'}
    result = result + i #result += i
    print(f'Now the result is {result}')
print(f'Sum of 10 numbers is {result}')'''

'''
result =0 #target variables
for i in range(21):
    if i%2 == 0:
       print(i)
       #print(f'result is {i+i}')
       result = result + i #result += i   
print(f'the result is {result}')'''

#Understand the loops usage with Fitness Streak example
#work_out -->,work_out_missed -->0

work_log = [0,1,1,1,1,1,0]
#result variables -->longest_streak
longest_streak = 0 #target variable
current_streak = 0
for day in work_log:
    if day == 1:
        #print(day)
        currnet_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = curreent_streak
    else:
        current_streak = 0 #streak breaks
print(f'Longest Streak is {longest_streak}')





