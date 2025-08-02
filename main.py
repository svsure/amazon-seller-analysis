import pandas as pd  
df = pd.read_csv('bestsellers.csv') #works with file

#exploring the data/overview of dataset
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

#cleaning dataset
df.drop_duplicates(inplace=True) #editing file directly
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"] = df["Price"].astype(float)

#author popularity
print('Author Popularity')
author_counts = df['Author'].value_counts()
print(author_counts)

#average rating organized by genre
print("Average Rating Organized by Genre")
print(df.columns)  # <-- check column names
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

#exporting
author_counts.head(10).to_csv("top_authors.csv")
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")
