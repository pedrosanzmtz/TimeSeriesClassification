library(forecast)
library(fpp2)
library(ggplot2)

set.seed(3)
y <- ts(rnorm(50))
autoplot(y) + labs(x = "Season", y = "Price", title = "") + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15))
ggsave("noise.eps")

Passengers <- ts(AirPassengers, start = c(1949, 1), frequency = 20)
autoplot(Passengers) + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15))
ggsave("trend.eps")


t <- window(qcement, start=2010)

ggseasonplot(t, year.labels=FALSE, continuous=TRUE) + labs(x = "Season", y = "Price", title = "") + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15)) + theme(legend.title = element_text(size=15), legend.text=element_text(size=15))
ggsave("seasonality.eps")

scurve <- function(x){
  y <- exp(x) / (1 + exp(x))
  return(y)
}
ggplot(data = data.frame(x = c(-3, 3)), aes(x)) + stat_function(fun = scurve, n = 100) + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15))

ggsave("movements.png")
