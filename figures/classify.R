library(ggplot2)

ggplot(data=iris, aes(x=Sepal.Length, y=Sepal.Width, color=Species, shape=Species)) + geom_point(size=3) + theme(axis.title.x = element_text(size=25), axis.title.y = element_text(size=25), axis.text.x = element_text(size=35), axis.text.y = element_text(size=35), legend.text = element_text(size=20), legend.title = element_text(size=25)) + theme_bw() + scale_color_grey()
ggsave("classifyeps.eps")
