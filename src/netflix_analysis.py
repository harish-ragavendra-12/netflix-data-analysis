
import pandas as pd
import matplotlib.pyplot as plt

# Load data
ott_data = pd.read_csv("../data/netflix_titles.csv")

print("Dataset:\n")
print(ott_data.head())

print("\nDataset Info")
ott_data.info()

print("\nMissing Values")
print(ott_data.isnull().sum())

print("\nStatistics")
print(ott_data.describe())

#Movies vs TV Shows
content_count = ott_data["type"].value_counts()

plt.figure(figsize=(8,5))

content_count.plot(kind="bar")

plt.xlabel("Content Type")

plt.ylabel("Count")

plt.title("Movies vs TV Shows")

plt.savefig("../visuals/movies_vs_tvshows.png")

plt.show()

#Most common genres
genre = (ott_data["listed_in"].str.split(", ").explode())

top_genres = genre.value_counts().head(10)

plt.figure(figsize=(10,6))

top_genres.plot(kind="bar")

plt.xlabel("Genre")
plt.ylabel("Count")
plt.title("Top 10 Genres on Netflix")

plt.xticks(rotation=45)

plt.savefig("../visuals/top_genres.png")

plt.show()

#Country with most content
country = (ott_data["country"].dropna().str.split(", ").explode())

top_country = (country.value_counts().head(10))

plt.figure(figsize=(10,6))

top_country.plot(kind="bar")

plt.xlabel("Country")
plt.ylabel("Number of Shows")
plt.title("Top Countries Producing Netflix Content")

plt.xticks(rotation=45)

plt.savefig("../visuals/top_country.png")

plt.show()

#Trend over years
year_count = (ott_data["release_year"].value_counts().sort_index())

plt.figure(figsize=(12,6))

plt.plot(year_count.index,year_count.values)

plt.xlabel("Release Year")
plt.ylabel("Count")
plt.title("Netflix Content Trend Over Years")

plt.savefig("../visuals/year_trend.png")

plt.show()