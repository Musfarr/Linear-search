 #linear search
a = [ 1 , 32, 54, 62, 74, 2, 3, 5]
hp = int(input("enter any number"))
n = len(a)

for i in range(n):
    s = a[i]

    if(s==hp):
        print("no found at :",i+1)
        break

    else:
        if s != hp:

            print("ntf")
