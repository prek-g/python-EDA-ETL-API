# Exploratory Data Analysis (EDA) on Airbnb Dataset

![Boxplot Outliers](Boxplot_outliers.png)

## Objective
The main goal of this project is to perform an exploratory data analysis (EDA) on an Airbnb dataset to understand the distribution of prices, availability, and other key factors. This analysis also aims to detect missing values, duplicates, and outliers, and visualize relationships between variables for better insights.

---

## 1. Importing Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

## 2. Loading the Dataset
```python
dataset = data = pd.read_csv("datasets.csv", encoding_errors='ignore')

dataset.head()
```
```python
data.tail()
```
```python
dataset.shape
```
```python
dataset.info()
```
**Records that have less than data.shape[0] non-null values are considered missing.**

## 3. Statistical Report
```python
dataset.describe()
```
**From the statistical report, we can see that there are 34 missing values in the price column out of 20,760 records.**

## 4. Data Cleaning
#### Checking for Missing Values
```python
dataset.isnull().sum()
```
#### Dropping Missing Values
```python
dataset.dropna(inplace=True)
```
#### Verifying Missing Values Again
```python
dataset.isnull().sum()
dataset.shape
```
**Since only 34 rows (0.16% of dataset) were missing, removing them is safe and doesn't significantly affect the analysis.**

## 5. Handling Duplicates
```python
dataset.duplicated().sum()
dataset[dataset.duplicated()]
df = dataset.drop_duplicates().copy()
df.duplicated().sum()
```

## 6. Data Analysis
### 6.1 Univariate Analysis
#### Identifying Outliers in Price
```python
plt.title('Price distribution', fontsize=15)
sns.boxplot(data=df, x='price')
plt.ylabel("Frequency", fontsize=15)
plt.xlabel("Price", fontsize=15)
plt.savefig("Boxplot_outliers.png")
```
**Most prices fall within [0, 10,000], with a few extreme values around 100,000. These outliers will be removed for better visualization.**
```python
df_plot = df[df['price'] < 2000]

plt.figure(figsize=(10,8))
plt.title('Price distribution', fontsize=15)
sns.histplot(data=df_plot, x='price', bins=50)
plt.ylabel("Frequency", fontsize=15)
plt.xlabel("Price", fontsize=15)

sns.boxplot(data=df_plot, x='price')
plt.title('Price distribution', fontsize=15)
plt.ylabel("Frequency", fontsize=15)
plt.xlabel("Price", fontsize=15)
plt.savefig("Boxplot_no_outliers.png")
```

#### Availability Distribution
```python
plt.figure(figsize=(10,8))
plt.title('Availability 365', fontsize=15)
sns.histplot(data=df_plot, x='availability_365')
plt.ylabel("Frequency", fontsize=15)
plt.xlabel("Availability", fontsize=15)
```

#### 6.2 Average Price by Neighbourhood
```python
df.groupby(by='neighbourhood_group')['price'].mean()
```

#### 6.3 Price Per Bed
```python
df['price per bed'] = df['price'] / df['beds']
df['price per bed']

df.groupby(by='neighbourhood_group')['price per bed'].mean()
```

## 7. Bi-Variable Analysis
### Price vs Neighbourhood and Room Type
```python
sns.barplot(data=df, x='neighbourhood_group', y='price', hue='room_type')
plt.title("Price with respect to neighbourhood", fontsize=15)
plt.ylabel("Price", fontsize=15)
plt.xlabel("Neighbourhood", fontsize=15)
```

### Number of Reviews vs Price
```python
plt.figure(figsize=(8,5))
plt.title('Price with respect to number of reviews', fontsize=15)
sns.scatterplot(data=df_plot, x='number_of_reviews', y='price', hue='neighbourhood_group')
plt.ylabel("Price", fontsize=15)
plt.xlabel("Number of Reviews", fontsize=15)
```

### Pair Plot of Numeric Features
```python
sns.pairplot(data=df_plot, vars=['price', 'minimum_nights', 'number_of_reviews','availability_365'], hue='room_type')
plt.figure(figsize=(14,8))
```

### 7.1 Geographical Distribution
```python
sns.scatterplot(data=df, x='longitude', y='latitude', hue='room_type')
plt.title('Geographical distribution', fontsize=15)
plt.ylabel("Latitude", fontsize=15)
plt.xlabel("Longitude", fontsize=15)
plt.savefig('Geographical_distribution.png')
```
## 8. Correlation Analysis
```python
corr = df[['latitude','longitude','price', 'minimum_nights','number_of_reviews','reviews_per_month','availability_365','beds']].corr()
corr
```
```python
sns.heatmap(data=corr, annot=True)
plt.title('Correlation Matrix', fontsize=15)
plt.figure(figsize=(10,8))
```
**Correlation values range from -1 to +1 and indicate the strength of linear relationships between features.**

## Conclusions

- The dataset contained a very small percentage of missing values (0.16%) which were safely removed.
- Outliers in price were identified and removed to improve visualizations and analysis.
- The average price and price per bed vary across different neighbourhood groups.
- Bi-variable analysis showed relationships between price, number of reviews, room type, and neighbourhood.
- Geographical scatterplots and correlation heatmaps provided insights into feature relationships and distribution patterns.
- Overall, the dataset is now clean, duplicates removed, and ready for further modeling or predictive analysis.
