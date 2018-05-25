rm(list = ls())
library(ggplot2)
setwd("C:\\Users\\nwfxy\\Dropbox\\ProgrammingProjects\\4d_Analytics")

ResultsData <- read.csv("Results.csv")[-1]

x <- as.vector(sapply(ResultsData$PrizeCode, FUN = function(e) {switch(as.character(e),"1" = 850,"2" = 400, "C" = 50, "S" = 50)}))
