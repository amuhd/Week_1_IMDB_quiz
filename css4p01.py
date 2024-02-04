import pandas as pd

df = pd.read_csv("movie_dataset.csv")

pd.set_option('display.max_rows', None)

print(df)

x = df["Metascore"].mean()

df["Metascore"].fillna(x, inplace=True)

x = df["Revenue (Millions)"].mean()

df["Revenue (Millions)"].fillna(x, inplace=True)

print(df)

highest_rated_movie_index = df['Rating'].idxmax()

highest_rated_movie = df.loc[highest_rated_movie_index]

print("Highest Rated Movie:")
print(highest_rated_movie[['Title', 'Rating']])

average_revenue = df["Revenue (Millions)"].mean()

print("Average Revenue of The Movies:", average_revenue)


filter_movies = df[(df['Year'] >= 2015) & (df['Year'] <= 2017)]

average_revenue_of_movies_from_2015_to_2017 = filter_movies['Revenue (Millions)'].mean()

print("Average Revenue of Movies from 2015 to 2017:", average_revenue_of_movies_from_2015_to_2017)


movies_count_for_2016 = (df['Year'] == 2016).sum()

print("Number of Movies Released in 2016:", movies_count_for_2016)



Christopher_Nolan_movies_count = (df['Director'] == 'Christopher Nolan').sum()

print("Number of Movies Directed by Christopher Nolan:", Christopher_Nolan_movies_count)

movies_with_high_rating_count = (df['Rating'] >= 8.0).sum()

print("Number of Movies with a Rating of at Least 8.0:", movies_with_high_rating_count)

Christopher_Nolan_movies = df[df['Director'] == 'Christopher Nolan']

median_rating_of_Christopher_Nolan_movies = Christopher_Nolan_movies['Rating'].median()

print("Median Rating of Movies Directed by Christopher Nolan:", median_rating_of_Christopher_Nolan_movies)

average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_with_highest_average_rating = average_rating_by_year.idxmax()

print("Year with the Highest Average Rating:", year_with_highest_average_rating)

movies_from_2006_to_2016 = df[(df['Year'] >= 2006) & (df['Year'] <= 2016)]

movies_count_by_year = movies_from_2006_to_2016.groupby('Year').size()

count_of_2006 = movies_count_by_year.loc[2006]
count_of_2016 = movies_count_by_year.loc[2016]

percentage_increase = ((count_of_2016 - count_of_2006) / count_of_2006) * 100


print("Percentage Increase in Number of Movies (2006 to 2016): {:.2f}%".format(percentage_increase))

all_actors = df['Actors'].str.cat(sep=',')
all_actors_list = all_actors.split(',')

actor_counts = pd.Series(all_actors_list).value_counts()

most_common_actor = actor_counts.idxmax()

print("Most Common Actor in All Movies:", most_common_actor)

all_genres = df['Genre'].str.split(',').explode()

unique_genres_count = all_genres.nunique()

print("Number of Unique Genres in the Dataset:", unique_genres_count)

numerical_features = df[['Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']]

correlation_matrix = numerical_features.corr()

print("Correlation Matrix:")
print(correlation_matrix)

