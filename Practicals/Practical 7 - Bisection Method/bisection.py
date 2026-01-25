from random import randint
from tabulate import tabulate

class Soln:
    def calcResult(self) -> float:
        result=0
        deg = self.degree
        for coeff in self.coeffs:
            result += coeff*(self.root**deg)
            deg-=1
        
        return result  
    
    def isPositive(self):
        res = self.result
        if(res>0):
            return True
        elif(res<0):
            return False
        else:
            return None
    
    def isSolved(self, tolerance: float) -> bool:
        return abs(self.result)<=tolerance
    
    def __init__(self,coeffs: list, root:float, tolerance=0.001):
        self.coeffs=coeffs
        self.root = root
        self.degree = len(coeffs)-1
        self.result = self.calcResult()
        self.tolerance = tolerance
    
    def display(self) -> None:
        print("Equation:")
        terms = []
        deg = self.degree

        for coeff in self.coeffs:
            if coeff==0:
                deg-=1
                continue # If 0 then ignore term
            
            # Getting the sign
            sign = "-" if coeff<0 else "+"
            c = abs(coeff)

            # Variable part
            if deg == 0: # If constant
                term = str(c)
            elif deg == 1: # If degree is 1 then just print x
                term = "x" if c == 1 else f"{c}x"
            else:
                term = f"x^{deg}" if c == 1 else f"{c}x^{deg}" # If coefficient is 1 the no need to print it

            terms.append((sign, term)) # Add to a list
            deg-=1

        # Printing equation
        eq = ""
        for i, (sign, term) in enumerate(terms):
            if i == 0: # For the first term if sign is + then ignore the '+'
                eq += term if sign == "+" else f"-{term}"
            else:
                eq += f" {sign} {term}"

        print(eq)
        print(f"Root: {self.root}")
        print(f"Is Positive: {self.isPositive()}")
        print(f"Is Solved: {self.isSolved(self.tolerance)}")
        

# coeff=[-2,5,-1,2]
# tol=0.001

degree = int(input("Enter degree: "))
coeff = []
for i in range(degree,-1,-1):
   coeff.append(int(input(f"Enter coefficient of x^{i}: ")))

tol = float(input("Enter tolerance: "))

negRoot = randint(-10,10)
posRoot = randint(-10,10)

while Soln(coeff,negRoot).isPositive():
    if Soln(coeff,negRoot,tol).isSolved(tol):
        print(f"Root Found: {negRoot}")
        exit(0)
    while not Soln(coeff,posRoot).isPositive():
        if Soln(coeff,posRoot).isSolved(tol):
            print(f"Root Found: {posRoot}")
            exit(0)
        posRoot=randint(-10,10)
    negRoot=randint(-10,10)

posSoln = Soln(coeff,posRoot)
negSoln = Soln(coeff,negRoot)

midRoot = (negRoot + posRoot)/2.0
answer = Soln(coeff,midRoot)

headers = ["Iteration","negRoot","posRoot","mid","f(mid)"]
tableData = [[1,negRoot,posRoot,midRoot,answer.result]]
i=1
while not answer.isSolved(tol):
    midRoot = (negRoot + posRoot)/2.0
    fneg = Soln(coeff,negRoot).result
    answer = Soln(coeff,midRoot)
    if fneg*answer.result < 0:
        posRoot = midRoot
    else:
        negRoot = midRoot
    i+=1
    tableData.append([i,negRoot,posRoot,midRoot,answer.result])
    
print(tabulate(tableData,headers=headers))
print()
answer.display()

