# iris_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
def load_and_explore_data():
    # Load the Iris dataset
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target

    # Display the first few rows
    print("First few rows of the dataset:")
    print(iris_df.head())

    # Check data types and missing values
    print("\nData types and missing values:")
    print(iris_df.info())
    print(iris_df.isnull().sum())

    return iris_df

# Task 2: Basic Data Analysis
def basic_data_analysis(iris_df):
    # Basic statistics of numerical columns
    print("\nBasic statistics of numerical columns:")
    print(iris_df.describe())

    # Group by species and compute the mean of numerical columns
    species_mean = iris_df.groupby('species').mean()
    print("\nMean of numerical columns grouped by species:")
    print(species_mean)

    return species_mean

# Task 3: Data Visualization
def create_visualizations(iris_df, species_mean):
    # Set the aesthetic style of the plots
    sns.set(style="whitegrid")

    # Bar chart for average petal length per species
    plt.figure(figsize=(8, 5))
    sns.barplot(x=species_mean.index, y=species_mean['petal length (cm)'])
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.xticks(ticks=[0, 1, 2], labels=iris.target_names)
    plt.show()

    # Histogram of petal length
    plt.figure(figsize=(8, 5))
    sns.histplot(iris_df['petal length (cm)'], bins=10, kde=True)
    plt.title('Distribution of Petal Length')
    plt.xlabel('Petal Length (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # Scatter plot of sepal length vs. petal length
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species', labels=iris.target_names)
    plt.show()

# Findings and Observations
def findings():
    print("\nFindings and Observations:")
    print("- The average petal length varies significantly among different species.")
    print("- The scatter plot shows a clear separation between species based on sepal length and petal length, indicating that these features can be useful for classification.")

# Main function to run the analysis
def main():
    iris_df = load_and_explore_data()
    species_mean = basic_data_analysis(iris_df)
    create_visualizations(iris_df, species_mean)
    findings()

if __name__ == "__main__":
    main()