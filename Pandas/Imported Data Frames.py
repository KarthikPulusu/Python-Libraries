import pandas as pd
import numpy as np
print("Importing data Files:")
df=pd.read_csv('filmtv_movies.csv')
'''print(df.head(10))
print(df.tail(10))
print("shape is",df.shape)
print("Columns are:\n",df.columns)
print("Data types are:\n",df.dtypes)
print(df.describe())

print("\n\nAccessing and Filtering:")
print("***Title of all rows:\n",df.loc[:,'title'])
# Selecting a range of rows and multiple columns by labels
subset=df.loc[10:20,['title','year','genre']]
print(subset)
print("# Conditional selection using a boolean array")
drama=df.loc[df['genre']=='Drama']
print(drama)
print("With Avg Votes greater than 7.0")
multiple_cond=df.loc[(df['genre']=="Drama")&(df['avg_vote']>7.0)]
print(multiple_cond)

print("***Selecting a singe row")
single_row=df.iloc[0]
print(single_row)
print("***Selecting a specific row and columns")
specific_data=df.iloc[10,[1,2,3,4]]
print(specific_data)
print("***Getting multiple row and columns")
multi_slice=df.iloc[10:15,0:4]
print(multi_slice)
print("#Accessing a specific single value using row label using and column name")
print(df.at[0,'title'])
print("#Filtering bases on criteria")
print(df[df['year']>2000])
print("Movies with high public vote and a specific genre")
print(df[(df["public_vote"]>8)&(df['genre']=="Drama")])
print(df.loc[(df['genre']=="Drama" )&(df['public_vote']>8)])
print("#Movies with a specific Country:")
us_movies=df[df['country']=='United States']
print(us_movies)

print("***Updatin rows and columns")
print(df.drop(labels='title',axis=1))
print("Assigning a data Value")
df.at[0,'year']=1983
print(df.head(2))
print("Adding a new column:")
df['new_column']='default value'
print(df)
df.drop(labels='new_column',axis=1,inplace=True)
print(df.head(5))
print(df.columns)
df.loc[df['year']<2000,'Classic']=True
print(df.head())
print("Add two columns and value based on condition")
df.loc[df['avg_vote']>6,['Top_rated','must_watch']]=True
print(df.head())

df['length_category']=df['duration'].apply(lambda x:"Long" if x>92 else "short")
print(df['length_category'])

pd.set_option('display.max_rows',20)
pd.set_option('display.max_columns',25)
print(df.head())
df.to_csv('output.csv',index=False)

printf("***#Converting series to Data Frames")
Data={
    "A":[1,2,3],
    "B":[4,5,6],
    "C":[7,8,9]}
Data_df=pd.DataFrame(Data)
print(Data_df)
print(Data_df.iloc[1])

print("Sum of the series:\n")
def add(x,y):
    return x+y
result=Data_df.apply(lambda row:add(row['A'],row['B']),axis=1)
print(result)
print("****Closed***")
print("#Updating the Values using map function")  #Remaining All set to NAN
df['genre']=df['genre'].map({'Drama':'Drama Film','Comedy':'Comedy film'})
print(df['genre'])
df.replace({'country':{'United States':'USA'}},inplace=True)
#df['country'].replace('USA','United States',inplace=True) #Keeps the remaining all same
print(df['country'])

print("\n#Creating a new column based on the Calculations")
df['title_year']=df['title']+"("+df['year'].astype(str)+")"
print(df['title_year'])

print("#Adding Columns using assign Function")
df=df.assign(
    is_older=lambda x: x['year']<2000,
    duration_hours=lambda x:x['duration']/60
    )
print(df.head())
print(df[['duration_hours','is_older']])

print("#Renaming the index of a DataFrame:")
df.index.names=['movie_id']
print(df.head())'''

df.rename(columns={'year':'release_year','title':'movie_title'},inplace=True)
'''print(df.head())
print(df[['release_year','movie_title']])

print("\n#Display Options")
pd.set_option('display.max_rows',7)
pd.set_option('display.max_columns',5)
print(df)

pd.reset_option('display') #displays previous number of rows
print(df)

print("\n#Grouping Data:")
genre_groups=df.groupby('genre')
print(genre_groups)

for genre,group_data in genre_groups:
    print(f"Genre:{genre}")
    print(group_data)
    print()'''

year_genre_groups=df.groupby(['release_year','genre'])
print(df.head())
print("****Aggregation:******")
avg_duration=df.groupby('genre')['duration'].mean()
print(avg_duration)
print("\n#Multiple Aggregations on single Column")
print(df.groupby('genre')['avg_vote'].agg(['mean','std','min','max']))

print("#Different Aggregations for diff Columns")
complex_aggregation=df.groupby('genre').agg({
    'duration':'mean',
    "avg_vote":['min','max'],
    'public_vote':'sum'
    })
print(complex_aggregation)

print("\n#Overall Summary Statistics")
overall_stats=df[['duration','avg_vote']].describe()
print(overall_stats)

print("#Counting Non Null Values in each column")
data={'A':[1,2,None],'B':[4,None,6],'C':[5,8,9]}
data_df=pd.DataFrame(data)
counts=data_df.count()
print(counts)
print("\n Counting the Frequency of unique values in a single column")
unique_value=df['movie_title'].value_counts()
print(unique_value)
print(df.columns)

print("\n#Using a custom function for Aggregation")
def range_func(series):
    return series.max()-series.min()
range_by_genre=df.groupby('genre')['duration'].agg(range_func)
print(range_by_genre)

print("\n#Renaming Aggregation results:")
renamed_aggregations=df.groupby('genre')['avg_vote'].agg([
    ('Aggregate rating','mean'),
    ('Rating Standard deviation','std')
    ])
print(renamed_aggregations)
print("**THE END**")


