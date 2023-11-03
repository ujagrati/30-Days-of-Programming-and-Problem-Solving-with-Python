print("Choose a operator \n"
"1.add \n"
"2.subtract \n"
"3.divide \n"
"4.multiply \n"
) 


def add(x,y):
    return (x+y)
def subtract(x,y):
    return (x-y)
def divide(x,y):
    return (x/y)
def multiply(x,y):
    return (x*y)



select = int(input("Select a operator 1,2,3,4:"))

x= int(input("Enter number 1"))
y= int(input("Enter number 2"))

if select == 1:
    print(x,"+",y,"=",add(x,y))
elif select == 2:
    print(x,"-",y,"=",subtract(x,y))
elif select == 3:
    print(x,"/",y,"=",divide(x,y))
elif select == 4:
    print(x,"*",y,"=",multiply(x,y))
else:
    print("Invalid input")





