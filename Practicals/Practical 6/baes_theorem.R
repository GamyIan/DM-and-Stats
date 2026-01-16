library(e1071)
library(dplyr)

data=iris
summary(data)

data

model = naiveBayes(Species~. , data=data, laplace=1)
model
# t = data.frame(Sepal.Length=5.9, Sepal.Width=3.0, Petal.Length=5.1, Petal.Width=1.8)
# t = data[1:150:25,-5]
t = slice(data, seq(1, 150, by = 25))
t_label = t[,5]
t = t[,-5]
sol=predict(model, t)
table(sol,t_label)

