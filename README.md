# Netflix Data Analysis

## Project Overview

This project performs Exploratory Data Analysis (EDA) on a Netflix Movies and TV Shows dataset using Python, Pandas, and Matplotlib.

The goal of this project is to understand content trends on Netflix by analyzing genres, content types, countries producing content, and yearly growth trends.

---

## Objectives

* Analyze Movies vs TV Shows distribution
* Find the most common genres on Netflix
* Identify countries producing the highest content
* Analyze content trends over years
* Practice data wrangling and visualization techniques

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* PyCharm

---

## Dataset Information

Dataset: Netflix Movies and TV Shows Dataset

The dataset contains information such as:

* Show ID
* Type
* Title
* Director
* Cast
* Country
* Release Year
* Rating
* Duration
* Genres
* Description

---

## Project Structure

netflix_data_analysis/
│
├── data/
│   └── netflix_titles.csv
│
├── src/
│   └── netflix_analysis.py
│
├── visuals/
│   ├── movies_vs_tvshows.png
│   ├── top_genres.png
│   ├── top_country.png
│   └── year_trend.png
│
├── requirements.txt
│
└── README.md

---

## Features Implemented

### 1. Data Exploration

* Display first rows of dataset
* Dataset information
* Missing value analysis
* Statistical summary

### 2. Movies vs TV Shows Analysis

A bar chart is generated to compare:

* Total Movies
* Total TV Shows

### 3. Most Common Genres Analysis

Genre data is split and transformed using:

* split()
* explode()

Top 10 genres are visualized.

### 4. Country Content Analysis

Countries are analyzed to determine which produce the highest amount of Netflix content.

### 5. Trend Analysis Over Years

A line chart is used to visualize Netflix content growth over time.

---

## Concepts Practiced

### Data Wrangling

* Handling missing values
* String manipulation
* Data transformation
* explode()

### Exploratory Data Analysis (EDA)

* Value counts
* Trend analysis
* Category analysis

### Visualization

* Bar charts
* Line plots
* Labels and titles
* Saving figures

---

## Output Visualizations

Generated charts:

* Movies vs TV Shows
* Top Genres on Netflix
* Top Countries Producing Content
* Netflix Content Trend Over Years

Charts are automatically saved inside the visuals folder.

---

## How to Run

Install required libraries:

pip install -r requirements.txt

Run:

python src/netflix_analysis.py

---

## Future Improvements

* Add Seaborn visualizations
* Build interactive dashboard using Streamlit
* Add advanced EDA
* Add sentiment analysis for descriptions

---

## Author

Harish Ragavendra
