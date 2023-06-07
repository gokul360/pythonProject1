def add():
    a=int(input("enter a values:"))
    b=int(input("enter b values:"))
    c=a+b
    print("addition:",c)

add()
add()
add()

def sub(a,b):
    c=a-b
    print("difference:",c)

sub(5,2)
sub(3,2)
sub(8,7)

def mul():
    a=int(input("enter the values of A:"))
    b=int(input("enter the values of B:"))
    c=a*b
    return c
x=mul()
print("multiplication result",x)

def div(a,b):
    c=a/b
    return c
y=div(100,4)
print("div result",y)
def mca(*students):
    print(students)

mca("gokul","raghul","rvr")
add()
div(8,9)

