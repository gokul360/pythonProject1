for i in range(10):
    for j in range(i):
        print("^",end="")
    print("")
print("_______________________________________________")
for i in range(64,70,2):
    for j in range(64,71,2):
        print(chr(j),end="")
    print(j)