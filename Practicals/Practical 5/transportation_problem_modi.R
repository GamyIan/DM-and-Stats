library(lpSolve)
mat = matrix(c(19,30,50,10,70,30,40,60,40,8,70,20),nrow=3,byrow=TRUE)
mat
row_rhs = c(7,9,18)
col_rhs = c(5,8,7,14)
row_signs = c('=','=','=')
col_signs = c('=','=','=','=')

model = lp.transport(cost.mat=mat,
             direction='min',
             row.signs = row_signs,
             col.signs = col_signs,
             row.rhs = row_rhs,
             col.rhs = col_rhs)

model$solution
