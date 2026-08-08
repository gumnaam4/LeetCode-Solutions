a=[0]*4
b=False
for i in range(4):
    a[i]=int(input("Enter the number: "))
t=int(input("target: "))
for i in range(4):
    if t==a[i]:
        print(i)
        b=True
if b==False:
    for i in range(4):
        if a[i]>t:
            print(i)
            break
        else:
            p=i
    print(p+1)

        