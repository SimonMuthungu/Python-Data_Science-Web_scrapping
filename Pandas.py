from statistics import median
import pandas as pd

# loading the dataset onto var: dataset
dataset = pd.read_csv('data.csv')

# getting some background info from the data
print(dataset.info())

# We know that the calories data ought to be worked on, theres some missing data
# I choose to remove them though you can use mean() or Median() or mode() to add the missing data
dataset.dropna(inplace=True)
print(dataset.info())

# showing first and last 10 rows
print(dataset.head())
print(dataset.tail())

# doing some simple data analysis
mean_duration = dataset['Duration'].mean()
median_duration = dataset['Duration'].median()
mode_duration = dataset['Duration'].mode()
print(f'mean: {mean_duration}, mode: {mode_duration} and median: {median_duration}')

# finding some correlations in the data
print(dataset.corr())
# very simply, we can see that when we increase the pulse value, the maxpulse value value increases. This is also 
# kinda true for calories and duration. Thus, the cor() function is an easy way of drawing insight to a tables'
# columns relationships!