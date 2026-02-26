def balance (cost, supply, demand):
    difference = sum(demand) - sum(supply)
    if difference==0:
        pass
    elif difference > 0: # Demand is more
        cost.append([0]*len(demand))
        supply.append(difference)
    else: # Supply is more
        for row in cost:
            row.append(0)
        demand.append(abs(difference))
    
        
    return cost,supply,demand


def nw_corner(cost: list[list], supply: list, demand: list):
    cost,s,d = balance(cost,supply,demand)
    
    m = len(s) # Rows
    n = len(d) # Columns
    
    alloc = [[0]*n for _ in range(m)] # [0]*n gives [0,0,0,...] 0 repeats n times that is done for m rows
    
    # i and j are our iterators
    i=0
    j=0
    while i<m and j<n:
        x = min(s[i],d[j])
        alloc[i][j] = x
        s[i]-=x
        d[j]-=x
        
        if s[i] == d[j] == 0:
            i+=1
            j+=1
        elif s[i] == 0:
            i+=1
        else: # d[j]==0
            j+=1
            
    total_cost = 0
    for r in range(m):
        for c in range(n):
            total_cost += alloc[r][c]*cost[r][c]
    
    return alloc, total_cost

cost = [
    [20,25,28,31],
    [32,28,32,41],
    [18,35,24,32]
]

supply = [200,180,160]
demand = [150,40,180,170]

allocs,total_cost = nw_corner(cost,supply,demand)
print(f"Allocation: \n{allocs}")
print(f"Total Cost: {total_cost}")

            
    
    
    