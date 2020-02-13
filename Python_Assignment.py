#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
# Q1 Find least sales amount for each item
# has been solved as an example
df = pd.read_excel('SaleData.xlsx',sheet='Sales Data')
df.head()
def least_sales(df):
    ls = df.groupby(["Item"])["Sale_amt"].min().reset_index()
    return ls
print(least_sales(df))


# In[2]:


# Q2 compute total sales at each year X region
#def sales_year_region(df):
    # write code to return pandas dataframe
df.groupby(['OrderDate','Region','Item'])['Sale_amt'].sum()


# In[3]:


# Q3 append column with no of days difference from present date to each order date
from datetime import date
today = date.today()
def days_diff(df):
    df['OrderDate'] = pd.to_datetime(df['OrderDate']).dt.date
#df.dtypes
    df['days_diff']=today-df['OrderDate']
    return df
print(days_diff(df))


# In[4]:


# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
def mgr_slsmn(df):
    d=df.groupby(['Manager'])['SalesMan'].apply(list).reset_index(name='SalesMans')
    return d
print(mgr_slsmn(df))


# In[5]:


# Q5 For all regions find number of salesman and number of units
def slsmn_units(df):
    return df.groupby(['Region'])['SalesMan','Units'].count()
print(slsmn_units(df)) 


# In[7]:


# Q6 Find total sales as percentage for each manager
def sales_pct(df):
    d = df.groupby(["Manager"])
    d = d[["Sale_amt"]].sum()
    d1=d.apply(lambda x: 100*x/x.sum()).reset_index()
    return d1
print(sales_pct(df))


# In[8]:


import numpy as np
import pandas as pd
df=pd.read_csv("imdb.csv",escapechar="\\")
#df.head()
#type(re)
# Q7 get imdb rating for fifth movie of dataframe
def dupl_rows(df):
    re=df.loc[5]['imdbRating']
    #re.astype(int)
    return re
re7=dupl_rows(df)
print(re7)


# In[10]:


# Q8 return titles of movies with shortest and longest run time
#def movies(df):
def movies(df):
    df_new=df.drop(df.index[[728,1336,4022,7008,7702,8883,12908,14640]])
    df_new['duration']=df_new['duration'].astype(float)
    return df_new.title[(df_new['duration']==df_new['duration'].min()) | (df_new['duration']==df_new['duration'].max())]
print(movies(df))


# In[11]:


# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
def sort_df(df):
    return df.sort_values(['year','duration'],ascending=[True,False])
print(sort_df(df))


# In[47]:


#q10
#10. Subset the dataframe with movies having the following prameters.
#revenue(gross) more than 2 million spent(budget) 
#less than 1 million duration between 30 mintues to 180 minutes 
df=pd.read_csv("movie_metadata.csv")
def subset_data(df):
    return(df[(df.gross > 2000000) & (df.budget < 1000000) & (df.duration>30) & (df.duration < 180)])
print(subset_data(df))


# In[21]:


# Q11 count the duplicate rows of diamonds DataFrame.
df=pd.read_csv("diamonds.csv")
df.head()
def dupl_rows(df):
    return df[df.duplicated()].shape[0]
print(dupl_rows(df))


# In[23]:


# Q12 droping those rows where any value in a row is missing in carat and cut columns
def drop_row(df):
    df_new= df.dropna(subset=['carat','cut'])
    return df_new
print(drop_row(df))


# In[24]:


# Q13 subset only numeric columns
def sub_numeric(df):
    return list(df.select_dtypes(['int64','float64']).columns)
print(sub_numeric(df))


# In[25]:


# Q14 compute volume as (x*y*z) when depth > 60 else 8
def volume(df):
    df=df.drop([21,432])
    df['z']=df['z'].astype(float)
    vol=df['x']*df['y']*df['z']
    df['volume']=np.where(df['depth'] > 60,vol,8)
    return df

print(volume(df))


# In[28]:


# Q15 impute missing price values with mean

def impute(df):
    df_new=df.iloc[:,4:10]
    df_new=df_new.drop([21,432])
    df_new['z']=df_new['z'].astype(float)
    dff=df.fillna(df.mean())
    return dff
print(impute(df))


# In[29]:


#q1 Generate a report that tracks the various Genere combinations for each type year on year. 
#The result data frame should contain type, Genere_combo, year, avg_rating, min_rating, max_rating, total_run_time_mins 
import sys
df=pd.read_csv("imdb.csv",escapechar="\\")
def bonus1(df):
    df1=df.iloc[:,17:45].copy()
    my_list = [] 
    for i in range(len(df.index)):
        li=df1.loc[:,df1.loc[i] == 1].columns.tolist()
        my_list.append(li)
    df['generelist']=my_list
    df["generelist"]= df["generelist"].astype(str) 
    df2=df.groupby(['type','generelist','year']).agg({'imdbRating':['mean','min','max'],'duration':'count'})
    return(df2)
print(bonus1(df))   


# In[30]:


#bonus2
df=pd.read_csv("imdb.csv",escapechar="\\")
#Is there a realation between the length of a movie title and the ratings ? 
def corelation(df):
    df["length_title"]=df["title"].str.len()
    correlation=df['length_title'].corr(df['imdbRating'],method='pearson')
    return correlation
print(corelation(df))

# Generate a report that captures the trend of the number of letters in movies titles over years.
#We expect a cross tab between the year of the video release and the quantile that length fall under. 
#The results should contain year, min_length, max_length, num_videos_less_than25Percentile, num_videos_25_50Percentile 
def bonus2(df):
    df["length_title"]=df["title"].str.len()
    df['Quantiles'] = pd.qcut(df['length_title'],q=4,labels=['25%', '25-50%', '50-75%', '75-100%'])
    dff=df.groupby('year').agg({'length_title':['min','max'],'Quantiles':'count'})
    #print(dff.head())
    dff1=pd.crosstab(df.year, df.Quantiles)
    df_final=pd.concat([dff, dff1], axis=1)
    return df_final
print(bonus2(df))


# In[31]:


#Q3#df is dataframe with volume column
#In diamonds data set Using the volumne calculated above, create bins that have equal population within them.
#Generate a report that contains cross tab between bins and cut. 
#Represent the number under each cell as a percentage of total
df=pd.read_csv("diamonds.csv")
def bonus3(df):
    df=df.drop([21,432])
    df['z']=df['z'].astype(float)
    vol=df['x']*df['y']*df['z']
    df['volume']=np.where(df['depth'] > 60,vol,8)
    df['bins'] = pd.qcut(df['volume'],q=5)
    df1=pd.crosstab(df.bins, df.cut,normalize='all')*100
    return df1

print(bonus3(df))


# In[32]:


#bonusq4
movie=pd.read_csv("movie_metadata.csv")
def bonus4(movie):
    movie["genres"] = movie["genres"].str.split("|",expand = False)
    for genres in set.union(*movie.genres.apply(set)):
        movie[genres] = movie.apply(lambda _: int(_.genres.count(genres)), axis=1)
    q1 = [2007, 2008, 2009]
    q2 = [2010, 2011, 2012]
    q3 = [2013, 2014, 2015]
    q4 = [2016]
    a = [q1,q2,q3,q4]
    b = ['q1','q2','q3','q4']
    for i in a:
        movie.loc[movie['title_year'].isin(i),'quarter_year'] = b[a.index(i)]

    df = movie[movie['quarter_year'].isin(b)]
    a = 0.1
    df1 = (df.groupby('quarter_year',group_keys=False)
           .apply(lambda x: x.nlargest(int(len(x) * a), 'gross')))  
    lst = df1.iloc[:,29:].columns.tolist()
    df2 = df1.groupby('quarter_year')[lst].sum()
    df2['avg_imdb'] = df1.groupby('quarter_year')['imdb_score'].mean()
    return(df2)
print(bonus4(movie))


# In[33]:


#Q5
#Bucket the movies into deciles using the duration. 
#Generate the report that tracks various features like nomiations, wins, count, top 3 geners in each decile.
df=pd.read_csv("imdb.csv",escapechar="\\")
def bonus5(df):
    df['duration']=df['duration'].fillna((df['duration'].mean()))
    df['decile'] = pd.qcut(df['duration'],10)
    df1=df.groupby('decile').agg({'nrOfNominations':'sum','nrOfWins':'sum'})
    df2=df.iloc[:,16:44]
    df2['duration']=df['duration']
    lis=df2.columns.tolist()[0:28]
    df2['decile']=pd.qcut(df['duration'],10)
    dfg=df2.groupby('decile')[lis].sum().T
    rslt = pd.DataFrame(np.zeros((0,3)), columns=['top1','top2','top3'])
    for i in dfg.columns:
        df1row = pd.DataFrame(dfg.nlargest(3, i).index.tolist(), index=['top1','top2','top3']).T
        rslt = pd.concat([rslt, df1row], axis=0).reset_index(drop=True)
    li=list(map(list, rslt.values))
    df1['top3geners']=li
    return df1
print(bonus5(df))

