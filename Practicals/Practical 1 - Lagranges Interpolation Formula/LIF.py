
x=[]
y=[]

# If using set values
n=5
x=[3,7,10,12,15]
y=[12,32,47,57,72] 
inp=9

#If Taking Input
#n = int(input("Number of Elements: "))
#for i in range(n):
    #x.append(int(input(f"Enter x{i+1}: ")))
    #y.append(int(input(f"Enter y{i+1}: ")))
 
#inp = int(input("Enter x value to find y: "))

sum=0
for i in range(n):
    temp=1
    for j in range(n):
        if not i==j:
            temp*=(inp - x[j])/(x[i]-x[j])  
    sum+=temp*y[i]

print(f"y({inp}) = {sum}")