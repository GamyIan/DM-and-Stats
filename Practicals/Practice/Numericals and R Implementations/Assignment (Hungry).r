#Assignment problem

library(lpSolve)

Cost_Matrix = matrix(c(18,26,17,11,
                       13,28,14,26,
                       38,19,18,15,
                       19,26,24,10),nrow = 4,byrow = T)

Ass_sol = lp.assign(cost.mat = Cost_Matrix,direction = 'min')

Ass_sol
Ass_sol$solution
