def rvr(name,age):
    print(name,"age is",age)
rvr("raghul",18)
rvr("hema",47)

def mpt(**data):
    print("mpt datas",data)
mpt(name="gokul",age=23,city="malayalapatti")

def total(marks):
        return sum(marks)
print("gokul marks",total([77,99,88,99,99]))
mpt(name="raghul",Class="12th")
