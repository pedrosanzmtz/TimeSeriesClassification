library(ggplot2)

df <- read.csv('results/grades.csv')
#png('results/gradesall.eps')
ggplot(df, aes(x=model, y=accuracy, fill=slice)) + geom_bar(stat='identity', position=position_dodge()) + theme_minimal() + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15), legend.text = element_text(size=15), legend.title = element_text(size=20))
ggsave("results/gradesall.eps")

d <- df[df$slice == 'M_T2', ]

png('results/grades_m_t2.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()


d <- df[df$slice == 'M_T3', ]

png('results/grades_m_t3.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()


d <- df[df$slice == 'M_T4', ]

png('results/grades_m_t4.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()


d <- df[df$slice == 'M_T5', ]

png('results/grades_m_t5.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()

#######################################################3

df <- read.csv('results/inventories.csv')

#png('results/inventoriesall.png')
ggplot(df, aes(x=model, y=accuracy, fill=slice)) + geom_bar(stat='identity', position=position_dodge()) + theme_minimal() + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15), legend.text = element_text(size=15), legend.title = element_text(size=20))
ggsave("results/inventoriesall.eps")


d <- df[df$slice == '1M', ]

png('results/intentories_m_1M.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()


d <- df[df$slice == '2M', ]

png('results/intentories_m_2M.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()


d <- df[df$slice == '3M', ]

png('results/intentories_m_3M.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()


d <- df[df$slice == '4M', ]

png('results/intentories_m_4M.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()


d <- df[df$slice == '5M', ]

png('results/intentories_m_5M.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()


d <- df[df$slice == '6M', ]

png('results/intentories_m_6M.png')
ggplot(d, aes(x=model, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()



# df <- read.csv('results/inventories.csv')

# png('inventories.png')
# ggplot(df, aes(x=slice, y=accuracy, fill=model)) + geom_bar(stat='identity', position=position_dodge()) +theme_minimal()