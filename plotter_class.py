from matplotlib import pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd 
import plotly.express as px
import seaborn as sns
import statsmodels.api as sm

class Plotter:
 
    @staticmethod
    def qq_plot(df, column_name):
        """
        this method generates a qq plot of the data in a given column
        
        arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): the name of the column to use
        """
        sm.qqplot(df[column_name], line="s")
        plt.title(f"QQ Plot {column_name}")
        plt.show()

    @staticmethod
    def histogram(df, column_name):
        """
        this method returns a histogram of a given column with a KDE plot overlay, to visualise the skewness of the data
        
        arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): the name of the column to create a histogram on
        """
        plt.figure(figsize=(10, 6))
        plt.subplot(1, 2, 1)
        sns.histplot(df[column_name], kde=True)
        plt.title('Histogram with KDE')
        plt.show()

    @staticmethod
    def visualise_missing(df):
        """
        this method prints a plot of the missing data in each column

        arguments:
            df(str): name of the dataframe to run the method on
        """
        print(msno.matrix(df))


    @staticmethod
    def box_plot(df, column_name):
        """
        this method returns a box plot of a given column
        
        arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): name of the column to run the method on
        """
        sns.boxplot(x=df[column_name])
        plt.show()
       
    @staticmethod
    def correlation_heatmap(df):
        """
        this method returns a correlation heatmap of the dataframe
        
        arguments:
            df(str): the name of the dataframe to run the method on
        """
        fig = px.imshow(df.corr(), title="Correlation heatmap of dataframe")
        fig.show()