#Reading the data from SaleData
library(readxl)
library(dplyr)
df <- read_excel('SaleData.xlsx',sheet='Sales Data')
#head(df)
#print(head(df))


# Q1 Find least sales amount for each item
fun1<-function(df1)
  {
    ls<- df1 %>% group_by(Item) %>% slice(which.min(Sale_amt))
    return(ls)
  }
print(fun1(df))

# Q2 compute total sales at each year X region
fun2<-function(df){
  dff<-df %>% group_by(OrderDate,Region,Item) %>% summarise(total=sum(Sale_amt))
  return(dff)
}
print(fun2(df))
# Q3 append column with no of days difference from present date to each order date
fun3<-function(df1){
 df1<- mutate(df1,OrderDate=as.Date(OrderDate, format = "%m/%d/%y"))
  ls1<-mutate(df1,days_diff=Sys.Date()-OrderDate)
  return(ls1)
}
print(head(fun3(df)))
# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.

#install.packages("data.table")
library(data.table)

mgr_slsmn <- function(df){
  x1 <- unique(df$Manager)
  x2 <- sapply(x1,function(x) {unique((filter(df,df$Manager==x))$SalesMan)})
  data.table(Managers = x1,list_salesman = x2)
}
mgr_slsmn(df)
# Q5 For all regions find number of salesman and total sales

slsmn_units <- function(df){
  df %>%
    group_by(Region) %>%
    summarise(
      total_sales = sum(Sale_amt, na.rm = T),
      salesmen_count = length(unique(na.omit(SalesMan))))
}
slsmn_units(df)

# Q6 Find total sales as percentage for each manager
sales_pct <- function(df){
  d <- df %>%
    group_by(Manager) %>%
    summarise(total_sales = sum(Sale_amt)) %>%
    mutate(percent_sales=paste0(round(100*total_sales/sum(total_sales),2),'%'))
  d1 <- subset(d, select = -c(total_sales))
  return(d1)
}

sales_pct(df)


# Q7 get imdb rating for fifth movie of dataframe
df_imdb<-read.csv("imdb.csv")
#print(head(df2))
fun7<-function(df){
  ls7<-df_imdb[5,]["imdbRating"]
  return(ls7)  
  
}
  print(fun7(df_imdb))
# Q8 return titles of movies with shortest and longest run time
fun8<-function(df_imdb){
 ls8<-subset(df_imdb,duration==min(as.numeric(as.character(df_imdb$duration)),na.rm=TRUE) | duration==max(as.numeric(as.character(df_imdb$duration)),na.rm=TRUE))
  return(ls8)
}
print(fun8(df_imdb))
print("----------------------------================")
# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
fun9<-function(df_imdb){
  df_imdb$year<-as.numeric(as.character(df_imdb$year))
  df_imdb$imdbRating<-as.numeric(as.character(df_imdb$imdbRating))
  ls9<-arrange(df_imdb,year,desc(imdbRating))
  return(ls9)
}
print(head(fun9(df_imdb)))
print("===========================================================")
# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
fun10<-function(df_imdb){
  
}
# Q11 count the duplicate rows of diamonds DataFrame.
df<-read.csv("diamonds.csv",na.strings = "")
fun11<-function(df)
{
  r<-nrow(df[duplicated(df),])
  return(r)
  
}
print(fun11(df))

# Q12 droping those rows where any value in a row is missing in carat and cut columns
fun12<-function(df){
  ls12<-subset(df,(!is.na(carat)) & (!is.na(cut)))
  return(ls12)
}
fun12(df)
# Q13 subset only numeric columns
fun13<-function(df){
  df[5:10]<-sapply(df[5:10],function(x){as.numeric(as.character(x))})
  return(select_if(df, is.numeric))
}
print(str(fun13(df)))

# Q14 compute volume as (x*y*z) when depth > 60 else 8
fun14<-function(df){
  df[5:10]<-sapply(df[5:10],function(x){as.numeric(as.character(x))})
  voll<-(df$x*df$y*df$z)
  df$vol<-ifelse(df$depth > 60,voll,8)
  return(df)
}
print(fun14(df))
# Q15 impute missing price values with mean
fun15<-function(df){
  df[5:10]<-sapply(df[5:10],function(x){as.numeric(as.character(x))})
  value<-mean(df$price, na.rm=TRUE)
  df$price <- ifelse(is.na(df$price),value, df$price)
  return(df)
}
fun15(df)
#another way
df<-read.csv("diamonds.csv",na.strings = "")
fun15<-function(df){
  #f[5:10]<-sapply(df[5:10],function(x){as.numeric(as.character(x))})
  df$price[is.na(df$price)] <- mean(df['price'], na.rm = TRUE)
  return(df)
}
print(fun15(df))
#print(nrow(fun12(df)))