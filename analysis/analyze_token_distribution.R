# Title     : analyze token distribtion
# Objective : analyze the distribution of the tokens
# Created by: michael
# Created on: 03.12.17
library(ggplot2)
library(ineq)

data <- read.csv("../data/qtum.csv")
print(data)

plot <- ggplot(data, aes(x = X, y = tokens)) + geom_line() + scale_y_log10() + scale_x_log10()

show(plot)

Lc.p <- Lc(as.vector(data[["tokens"]]))
plot(Lc.p)

gini_coeff <- ineq(as.vector(data[["tokens"]]), type = "Gini")
print(gini_coeff)
