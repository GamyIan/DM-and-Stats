n=4
x = [5,7,10,12]
y = [19,25,32,39]
inp=14

sum=0
for i in range(n):
    temp=1
    for j in range(n):
        if i!=j:
            temp*=(inp-x[j])/(x[i]-x[j])
    sum+=temp*y[i]
    
print(f"y({inp}) = {sum}")
    
