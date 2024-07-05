# 2.Required Argument:-
'''
   - it is a type of error occurs when we can not pass
     sufficient value at the time of calling function..

'''

def add(a,b,c):
    d=a+b+c
    print("Addition=",d)

add(12,67)  # Error- Missing 1 required positional argument
add(120)    # Error-  Missing 2 required positional argument
add()       # Error- Misisng  3 required positional argument
