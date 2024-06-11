View(Wholesale_customers_data)
str(Wholesale_customers_data)
library(dplyr)
library(tidyverse)

#finding if the continuous variables are normally distributed
wholesale<- Wholesale_customers_data
summary(wholesale,Fresh:Delicassen)

# finding all missing data in the data set
sum(is.na(wholesale))

#show the outliers in the continuous variable
#first call out the library ggplot2
library(ggplot2)
#identifying the outliers in column fresh
outliers_fresh <- boxplot.stats(wholesale$Fresh)$out  # outlier values in column fresh
outliers_fresh# it has 20 outliers

#identifying the outliers in column milk
outliers_milk <- boxplot.stats(wholesale$Milk)$out  # outlier values in column milk
outliers_milk# it has 28 outliers

#identifying the outliers in column grocery
outliers_grocery <- boxplot.stats(wholesale$Grocery)$out  # outlier values in column grocery
outliers_grocery#it has 24 outliers

#identifying the outliers in column frozen
outliers_frozen <- boxplot.stats(wholesale$Frozen)$out  # outlier values in column frozen
outliers_frozen#it has 42 outliers

#identifying the outliers in column detergents
outliers_detergents <- boxplot.stats(wholesale$Detergents_Paper)$out  # outlier values in column detergents
outliers_detergents#it has 30 outliers

#identifying the outliers in column delicassen
outliers_delicassen <- boxplot.stats(wholesale$Delicassen)$out  # outlier values in column delicassen
outliers_delicassen#it has 27 outliers 

###to find the min and max of each variable
sapply(wholesale,range)
#visualization of the outliers on a box plot
boxplot(wholesale$Fresh,main="boxplot for column fresh") 
boxplot(wholesale$Milk,main="boxplot for column milk") 
boxplot(wholesale$Grocery,main="boxplot for column grocery") 
boxplot(wholesale$Frozen,main="boxplot for column frozen") 
boxplot(wholesale$Detergents_Paper,main="boxplot for column detergents") 
boxplot(wholesale$Delicassen,main="boxplot for column delicassen") 

#trying to remove outliers using IQR
IQR(wholesale$Fresh)
summary(wholesale$Fresh)

#result is 13806
# get threshold values for outliers
Tmin <- 3128-(1.5*13806) 
Tmax <- 16934+(1.5*13806)
treshold<-38793

#Remove the 20 outliers
no_outliers=wholesale$Fresh[which(wholesale$Fresh > treshold)]
no_outliers#failed to remove outliers


Wholesale_new = remove_outlier(wholesale, c('Fresh', 'Milk', 'Grocery', 'Frozen','Detergent_paper','Delicassen'))







#turning the data set into a csv file
file_path<-"Esther.csv"
write.csv(wholesale, file = file_path, row.names = FALSE)
cat("Data frame saved to", file_path)


#importing a csv file
Assignment1_esther<-read.csv("C:/Users/Esther/OneDrive/Documents/COURSE WORK/Esther.csv")

#which retail channel do customers use the most
library(dplyr)
channel_1<-filter(wholesale, Channel==1)#298 customers use this channel
channel_2<-filter(wholesale, Channel==2)#142 customers use this channel
#therefore channel 1 receives the most customers

#which region as the lowest purchasing power
region_1<-filter(wholesale, Region==1)#has 77
region_2<-filter(wholesale, Region==2)#has 47
region_3<-filter(wholesale, Region==3)#has 316
#therefore region_2 has the lowest purchasing power

#the region that spends the most on milk
#first get 3rd Qu for milk
summary(wholesale$Milk)
# then use it to create a minimum
region_milk<-filter(wholesale, Milk>= 7190)


