
while True:
    name = input("Name:")
    tamil = int(input("enter the Tamil Mark:"))
    english = int(input("enter the english Mark:"))
    maths = int(input("enter the maths Mark:"))
    science = int(input("enter the Science Mark:"))
    social = int(input("enter the social mark:"))
    total = tamil + english + maths + science + social
    print("total:", total)
    average = total / 5.0
    print("average:", average)
if tamil >= 35 and english >= 35 and maths >= 35 and science >= 35 and social >= 35:
    if average > 90 and average < 100:
        print("Grade:A")
    elif average > 80 and average < 90:
        print("grade:B")
    elif average > 50 and average < 80:
        print("grade:C")
    elif average > 35 and average < 50:
        print("grade:D")
else:
    print("grade :fail")



