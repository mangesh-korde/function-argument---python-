#4.Keyword Argument..
'''
   - In that we can change the positon of values while calling
     the function.
   -  In this we give parameter name when calling the function.
      so it can identify and give proper output..

'''
def show(rno,name,per):
    print("Roll No=",rno)
    print("Name=",name)
    print("percentage=",per)

show(11,"om",55.34)
show(name="sai",per=67.12,rno=1)
