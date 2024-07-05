# 3. Variable length Argument..
'''
    - variable length argument means flexible in length.
    - star(*) or asterisk sign is used for it.
    - In this, values are stored in tuple format.

'''
def add(*a):
    print(a)
    print(type(a))

add(12,1)
add(45,12,66)
add(78,32,56,11,90,3)
