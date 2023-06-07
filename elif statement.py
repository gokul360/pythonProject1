""""
0 --no fine
1-5---RS 5 fine
5-10----rs 10 fine
10-20---RS 20 fine
20 days above Member =ship cancel
"""
days = int(input("ENTER THE DAYS:"))
if days == 0:
    print("Good Customer")
elif (days >= 1 and days <= 5):
    print(days * 5, "..please pay fine in 2 days.Otherwise your membership has Cancel")
elif (days>=5 and days<=10):
        print(days * 10, "...please pay fine in 2 days.Otherwise your membership has Cancel")
elif (days >= 10 and days <= 20):
    print("Rs",days * 20, "...please pay fine in 2 days.Otherwise your membership has Cancel")
else:
    print(" membership has Cancel")
