library(ggplot2)

ggplot(iris, aes(x = Sepal.Length, y = Petal.Length)) + geom_point() + geom_smooth(method = "lm", se = F) + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15))
ggsave("lr.eps")
