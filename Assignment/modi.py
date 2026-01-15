import pandas as pd

class TransportationMatrix:
    def __init__(self, cost: pd.DataFrame, supply: pd.Series, demand:pd.Series):
        self.cost = cost
        self.supply = supply
        self.demand = demand
        
        self.mat = cost.copy()
        self.mat["Supply"] = supply
        self.mat.loc["Demand"] = demand
        self.mat.loc["Demand","Supply"] = demand.sum()
    
    @classmethod
    def from_mat(cls, mat: pd.DataFrame) -> "TransportationMatrix":
        mat = mat.copy()
        cost = mat.iloc[:-1, :-1]
        supply = mat.iloc[:-1, -1]
        demand = mat.iloc[-1, :-1]
        return cls(cost, supply, demand)
        
    def display(self) -> None:
        print(self.mat)
        


class Solution(TransportationMatrix):
    def __init__(self, cost: pd.DataFrame, supply: pd.Series, demand:pd.Series, allocation: pd.DataFrame):
        super().__init__(cost, supply,demand)
        self.allocation = allocation
        self.total_cost = int((self.cost*allocation).to_numpy().sum())
    
    @classmethod
    def from_mat(cls, mat: pd.DataFrame, allocation: pd.DataFrame) -> "Solution":
        base = TransportationMatrix.from_mat(mat)
        return cls(base.cost, base.supply, base.demand, allocation)
        
    
    def display(self) -> None:
        print("Cost Matrix: ")
        print(self.cost)
        print("\nAllocation: ")
        print(self.allocation)
        print(f"\nTotal Cost: {self.total_cost}")


def balance(matrix: TransportationMatrix) -> TransportationMatrix:
    demand = matrix.demand
    supply = matrix.supply
    cost = matrix.cost
    
    total_demand = demand.sum()
    total_supply = supply.sum()
    
    if (total_demand>total_supply):
        # Need to create dummy thicc row
        row = f"S{len(cost.index)+1}"
        cost.loc[row] = 0
        supply.loc[row] = total_demand - total_supply
    elif (total_supply > total_demand):
        # Need to create dummy thicc column
        col = f"D{len(cost.columns)+1}"
        cost[col] = 0
        demand.loc[col] = total_supply - total_demand
    
    mat = TransportationMatrix(cost,supply,demand)
    return mat
    
def nw_corner(matrix: TransportationMatrix) -> Solution:
    cost = matrix.cost # Only the costs
    supply = matrix.supply # Extracting supply
    demand = matrix.demand # Extracting Demand
    
    # Empty allocation table
    alloc = pd.DataFrame(
        0,
        index=cost.index,
        columns=cost.columns,
        dtype=int
    )
    
    # Now Gotta loop over costs diagonally
    i=j=0
    rows = list(cost.index)
    cols = list(cost.columns)
    
    while i<len(rows) and j<len(cols):
        row = rows[i]
        col = cols[j]
        sup = supply[row]
        dem = demand[col]
        
        # Allocating Supply and Demands
        if (sup>dem): # If Supply more
            supply[row]=sup-dem
            demand[col]=0
            alloc.loc[row,col]=dem
            j+=1 # Move Right
        elif (dem>sup): # If Demand more
            demand[col]=dem-sup
            supply[row]=0
            alloc.loc[row,col]=sup
            i+=1 # Move Down
        else: # If both equal then move downright (South-West)
            supply[row]=0
            demand[col]=0
            alloc.loc[row,col]=dem
            i+=1
            j+=1
    
    sol = Solution.from_mat(matrix.mat, alloc)
    return sol
    

def modi(matrix: TransportationMatrix) -> Solution:
    mat = balance(matrix)
    sol = nw_corner(mat)
    return sol  # Will impletment actual logic later just testing nw corner for now.



# Sample Data
cost = pd.DataFrame(
        [[5, 1, 8, 7, 5],
         [3, 9, 6, 7, 8],
         [4, 2, 7, 6, 5],
         [7, 11, 10, 4, 9]],
        index=["S1", "S2", "S3","S4"],
        columns=["D1", "D2", "D3", "D4", "D5"],
        dtype=int
    )

supply = pd.Series([15,25,42,35], index = cost.index, dtype = int) # Using unbalanced demand and supply on purpose to test dummy column creation
demand = pd.Series([30,20,15,10,20], index = cost.columns, dtype = int) 

mat = TransportationMatrix(cost,supply,demand)

solution = modi(mat)

solution.display()