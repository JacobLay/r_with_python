# Importing the dataset
args <- commandArgs(TRUE)
dataset <- read.csv(args[1])

# Fitting Linear Regression to the dataset
model = lm(formula = y ~ x,
               data = dataset)

 #Summary analysis of the model              
summary(model)

#Visualizing the Linear Regression results
png(file="r_orig.png")
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$x, y = dataset$y),
             colour = 'red') +
  ggtitle('y vs x') +
  xlab('x') +
  ylab('y')
dev.off()

png(file="r_lm.png")
ggplot() +
  geom_point(aes(x = dataset$x, y = dataset$y),
             colour = 'red') +
  ggtitle('y vs x') +
  xlab('x') +
  ylab('y') +
    geom_line(aes(x = dataset$x, y = predict(model, newdata = dataset)),
            colour = 'blue')
dev.off()


