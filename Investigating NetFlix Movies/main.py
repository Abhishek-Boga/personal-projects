# Author: Abhishek Venkataprasad Boga
# Date: 2024-12-24
# Description: This code is used to investigate the Netflix movies data

import pandas as pd
import matplotlib.pyplot as plt

# Reading the CSV file into a DataFrame: df
df=pd.read_csv('netflix_data.csv')
print(f'DF Shape: {df.shape}')
print(f'Rows: {df.shape[0]}, Columns: {df.shape[1]}')
# filter df based on year and type
df_type=df[df['type']=='Movie']
# print(df_type.head(6))
# print(df_type.shape)

df_duration=df_type[(df_type.loc[:,'release_year']>=1990) & (df_type['release_year']<2000)] # Series comparision
# print(df_duration.head(6))
# print(df_duration.shape)
plt.hist(df_duration.loc[:,['duration']]) # Dataframe (can also be a series)
plt.title('Distribution of Movies release in 1990s decade')
plt.xlabel('Duration (hrs)')
plt.ylabel('Movies (count)')
plt.show()

duration=100 # approx (95-111) duration -> 47 movies

# filter df_duration based on genre 
df_genre=df_duration[df_duration.iloc[:,-1]=='Action']
# print(df_genre.head(6))
# print(df_genre.shape)

# looping the df_genre to count the movies that have duration<90
count=0
for lable,row in df_genre.iterrows():
    if row['duration']<90:
        count=count+1
    else:
        count=count
        
short_movie_count=count
print(short_movie_count)    

# to check which movies have duration<90
df_duration=df_genre[df_genre['duration']<90]
print(df_duration)
