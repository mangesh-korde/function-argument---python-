#Q..using variable length argument print the addition of nos???

def addition(*b):
    print(b)
    sum=0
    for val in b:
        sum=sum+val
    print("Addition =",sum)

addition(11,22,33)
addition(11,22,33,44,55,66)
