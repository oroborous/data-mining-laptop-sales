# Laptop Sales

Answers the question: How did the retail price of a laptop change over time, per the LaptopSales.csv data.

# R Code for Chart
`library(ggplot2)`

`df <- read.csv("C:/Users/moogi/PycharmProjects/data-mining-laptop-sales/overall/LaptopSalesCategorized.csv", header=FALSE, stringsAsFactors=TRUE)`

`names(df) <- c("month", "price", "power", "power.min", "power.max", "category", "ppd")`

`df$mf <- as.factor(df$month)`

`avg.price <- aggregate(df$price, list(df$month, df$category), FUN=mean)`

`names(avg.price) <- c("month", "category", "price")`

`p1 <- ggplot(data=avg.price, aes(x=month, y=price, group=category)) + geom_line() + labs(title="Retail Price of Laptops", x ="Month", y = "Retail price")`

`avg.ppd <- aggregate(df$ppd, list(df$month, df$category), FUN=mean)`

`names(avg.ppd) <- c("month", "category", "ppd")`

`p2 <- ggplot(data=avg.ppd, aes(x=month, y=ppd, group=category)) + geom_line() + labs(title="Customer Purchasing Power", x ="Month", y = "Power per dollar")`

`p3 <- ggplot(df, aes(x=mf, y=price, fill=category)) + geom_boxplot() + labs(title="Retail Price of a Laptop (2008)", x ="Month", y = "Retail price")`