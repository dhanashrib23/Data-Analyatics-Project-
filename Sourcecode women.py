# Importing required libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns

# Defining a function to set title and y-axis label for the plot
def set_plot_properties(title, y_label):
    plt.title(title)
    plt.ylabel(y_label)
    plt.show()

# Reading the data from excel file into a pandas dataframe
women_data = pd.read_excel("D:/PROJECT/Data Analytics/WOMEN DATA.xlsx")

# Printing the first 5 rows of the dataframe
print(women_data.head())

# Printing the last 5 rows of the dataframe
print(women_data.tail())

# Plotting bar graph for women population in each year
years = ['2011', '2013', '2015', '2017', '2019', '2021', 'Total']
for year in years:
    women_data.plot(x='State', y=year, kind='bar', figsize=(10, 10))
    plt.xlabel(f"Women population in {year}")
    set_plot_properties(f"Women Population of India in {year}", "Population")

# Plotting line graph for women population trend over the years
women_data.plot(x='State', y=years, kind='line', figsize=(12, 8))
plt.xlabel("States")
plt.ylabel("Population")
plt.title("Women Population Trend in India")
plt.legend(years)
plt.show()

# Creating a new dataframe to compare the percentage increase in women population over the years
percent_increase = pd.DataFrame(columns=['Year', 'Percentage Increase'])
for i in range(1, len(years)):
    percent_increase.loc[i-1] = [f"{years[i-1]} to {years[i]}", round(((women_data.loc[:, years[i]] - women_data.loc[:, years[i-1]])/women_data.loc[:, years[i-1]])*100, 2).mean()]

# Plotting a bar graph for percentage increase in women population over the years
sns.barplot(x='Year', y='Percentage Increase', data=percent_increase)
plt.xlabel("Years")
plt.ylabel("Percentage Increase")
plt.title("Average Percentage Increase in Women Population in India")
set_plot_properties("", "Percentage Increase")

# Creating a new dataframe to compare the percentage of women population in each state
percent_women = pd.DataFrame(columns=['State', 'Percentage Women Population'])
percent_women['State'] = women_data['State']
for year in years:
    percent_women[f'{year}'] = (women_data[year]/women_data['Total'])*100

# Create a heatmap to visualize the correlation matrix
numeric_columns = ["2011", "2013", "2015", "2017", "2019", "2021", "Total"]
corr_matrix = women_data[numeric_columns].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")
plt.title("Correlation Matrix for Women Population Data")
plt.show()

