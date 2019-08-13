n = 5; k = 3

f1,f2 = 1,1

for i in range(2,n):
    f1,f2 = f2, k*f1+f2

print(f2)
