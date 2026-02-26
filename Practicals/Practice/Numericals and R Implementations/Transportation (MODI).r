#transportation problem
cost_mat = matrix(c(23, 27, 16, 18, 
                    12, 17, 20, 51, 
                    22, 28, 12, 32),nrow = 3,byrow = TRUE)

row_signs =  c('=','=','=')
row_rhs = c(30,40,53) # Supply
col_rhs = c(22,35,25,41) # Demand
col_signs = c('=','=','=','=')

modi_sol = lp.transport(cost.mat = cost_mat,
                               direction = 'min',
                               row.signs = row_signs,
                               row.rhs = row_rhs,
                               col.signs = col_signs,
                               col.rhs = col_rhs)


costs = matrix(c(23,27,16,18,
                 12,17,20,51,
                 22,28,12,32),nrow= 3, byrow= TRUE)

row_sign = c('=','=','=')
supply = c(30,40,53)
cols_sign = c('=','=','=','=')
demand = c(22,35,25,41)
model = lp.transport(costs,'min',row_sign,supply,cols_sign,demand)