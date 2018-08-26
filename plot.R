library(ggplot2)

cases <- c("grades", "inventories", "diseases")
labels <- c("H", "M", "W")
jumps_case <- list(2:5, 1:6, 1:6)
format <- ".eps"

for(i in 1:length(cases))
{
    case <- cases[i]
    jumps <- jumps_case[i]
    label <- labels[i]
    dir_case <- paste("results/", case, "_m_", sep="")
    csv_file <- paste("results/", case, ".csv", sep="")
    df <- read.csv(csv_file)
    all_image <- paste("results/", case, "_acc", format, sep="")
    ggplot(df, aes(x=model, y=acc, fill=slice)) + geom_bar(stat='identity', position=position_dodge()) + scale_fill_brewer(palette="YlGnBu") + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15), legend.text = element_text(size=15), legend.title = element_text(size=20))
    ggsave(all_image)
    for(i in jumps[[1]])
    {
        col <- paste(i, label, sep="")
        image_name <- paste(dir_case, i, label, format, sep="")
        sub_df <- df[df$slice == col, ]
        ggplot(sub_df, aes(x=model, y=acc, fill=model)) + geom_bar(stat='identity', position=position_dodge()) + scale_fill_brewer(palette="YlGnBu") + theme(axis.title.x = element_text(size=20), axis.title.y = element_text(size=20), axis.text.x = element_text(size=15), axis.text.y = element_text(size=15), legend.text = element_text(size=15), legend.title = element_text(size=20))
        ggsave(image_name)
    }
}
