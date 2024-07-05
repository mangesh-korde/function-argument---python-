#  1.Default Argument:
'''
    - Default Argument assign right to
      left (<----)
    - sufficient values are passed then
      default values are ignored....

'''

def add(a,b=10,c=12):
    d=a+b+c
    print("Addition=",d)


add(12,23,67)
add(12,89)
add(11)
