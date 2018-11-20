# install, load package
library(NeuralNetTools)
 
# create model
library(neuralnet)
AND <- c(rep(0, 7), 1)
OR <- c(0, rep(1, 7))
binary_data <- data.frame(expand.grid(c(0, 1), c(0, 1), c(0, 1)), AND, OR)
mod <- neuralnet(AND + OR ~ Var1 + Var2 + Var3, binary_data,
                 hidden = c(5, 3, 2), rep = 10, err.fct = 'ce', linear.output = FALSE)
 
# plotnet
par(mar = numeric(4), family = 'serif')
cairo_ps("whatever.eps")
plotnet(mod, alpha = 0.6)
dev.off()
