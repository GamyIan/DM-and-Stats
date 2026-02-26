library(e1071)
library(dplyr)

data = iris
summary(data)


model = naiveBayes(Species ~ ., data, laplace=1)
model

t = slice(data, seq(1,150,by=25))
t

t_label = t[,5]
t = t[,-5]
t

sol = predict(model, t)
table(sol,t_label)


fullSol = predict(model,data[,-5])
table(fullSol, data[,5])


new_flower = data.frame(
  Sepal.Length = 5.0,
  Sepal.Width  = 4.0,
  Petal.Length = 2.0,
  Petal.Width  = 0.1
)


