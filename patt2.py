n=int(input("enter number:"))
for i in range(n+1,0,-1):
    for j in range(0,i-1):
        print("*", end=' ')
    print(" ")
