n=int(input("= "))
m=n
s = 0
p = 1
while n != 0:
    n1 = n % 10
    n= n // 10
    s = s + n1
    p = p * n1
t = s + p
if m % t == 0:
    print(True)
else:
    print(False)