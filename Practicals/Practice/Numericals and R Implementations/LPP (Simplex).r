#lpSOlve Simplex

library(lpSolve)
z = c(10,6,4)

mat = matrix(c(1,1,1,
               10,4,5,
               2,2,6),nrow = 3 , byrow = TRUE)
dir = c('<=','<=','<=')
rhs = c(100,600,300)
mySol =lp(direction = "max",
          objective.in = z,
          const.mat = mat,
          const.dir = dir,
          const.rhs = rhs)

mySol$solution