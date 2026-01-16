library(lpSolve)

cost = matrix(c(15,13,14,17,11,12,15,13,18,12,10,11,15,17,14,16), nrow=4, byrow=TRUE)
cost

sol = lp.assign(cost)
sol$solution
sol
