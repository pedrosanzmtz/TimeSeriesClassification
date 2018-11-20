library(ggplot2)

df <- economics

df$Year <- as.numeric(format(as.Date(df$date, format="%Y-%m-%d"), "%Y"))

df1 <- df[!rev(duplicated(rev(df$Year))),]

df1$Value <- 1:nrow(df1)
df1$Pop <- df1$pop
df$pop <- NULL

ggplot(data = df1, aes(x = Value, y = Pop)) + labs(x = "Year", y = "Price", title="") + geom_point(color = "black", size=2) + geom_smooth(method = lm, se = FALSE, color = "black") + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15))
ggsave("arima.eps")

ggplot(data = df1, aes(x = Year, y = Pop)) + labs(x = "Year", y = "Price", title="") + geom_point(color = "black", size=2) + geom_line(color = "black", size=1) + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15))
ggsave("ordinary.eps")
