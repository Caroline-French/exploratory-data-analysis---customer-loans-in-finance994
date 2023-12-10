from matplotlib import pyplot as plt
from scipy.stats import yeojohnson
import missingno as msno
import numpy as np
import pandas as pd 
import seaborn as sns
import statsmodels.api as sm


class DataFrameTransform:
    """
    this class is used to perform transformations on a pandas dataframe
    
    """
       
    @staticmethod
    def drop_column(df, column_name):
        """
        this method is used to drop a column in the dataframe
        
        arguments:
            df(str): name of the dataframe on which to run the method
            column_name(str): the name of the column to drop
        """
        df.drop(column_name, axis=1, inplace=True)

    
    @staticmethod
    def drop_rows_with_missing(df, column_name):
        """
        this method drops all rows where the data is missing for the given column
        
        arguments:
            df(str): name of the dataframe on which to run the method
            column_name(str): the name of the column to check for missing values
        """
        df.dropna(subset=[column_name], inplace=True)

    
    @staticmethod
    def fill_missing_from_column(df, column_to, column_from):
        """
        this method fills the missing values in a column with the value from another column in the same row
        
        arguments:
            df(str): name of the dataframe on which to run the method
            column_to(str): the name of the column with missing values to fill
            column_from(str): the name of the column to take the values from
        """
        df[column_to].fillna(df[column_from], inplace=True)

    
    @staticmethod
    def impute_mean(df, column_name):
        """
        this method imputes missing values in a given column with the mean value of that column
        
        arguments:
            df(str): name of the dataframe on which to run the method
            column_name(str): the name of the column to impute mean values
        """
        df[column_name].fillna(df[column_name].mean(), inplace=True)

 
    @staticmethod
    def log_transform(df, column_name):
        """
        this method performs a log transform on a skewed column

        arguments:
            df(str): name of the dataframe on which to run the method
            column_name(str): the column on which to perform the log transform
        """
        df[column_name] = df[column_name].map(lambda i: np.log(i) if i > 0 else 0)
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column_name], kde=True, label="Skewness: %.2f" % (df[column_name].skew()))
        plt.title(f"Log-Transformed Population Distribution: {column_name}")
        plt.xlabel("Log(Population)")
        plt.legend()
        plt.show()
    

    @staticmethod
    def yeo_johnson_transform(df, column_name):
        """
        this method perfoms a Yeo Johnson transformation on a given column
        
        arguments:
            df(str): name of the dataframe on which to run the method
            column_name(str): name of the column on which to perform the transformation
        """
        yeojohnson_population = df[column_name]
        yeojohnson_population = yeojohnson(yeojohnson_population)
        yeojohnson_population= pd.Series(yeojohnson_population[0])
        sns.histplot(yeojohnson_population,label="Skewness: %.2f"%(yeojohnson_population.skew()) )
        plt.title(f"YJ-Transformed Population Distribution: {column_name}")
        plt.xlabel("Log(Population)")
        plt.legend()
        plt.show()
        df[column_name] = yeojohnson_population
        
        
    @staticmethod
    def remove_outliers(df, column_name):
        """
        this method removes outliers from given columns using the IQR method
        
        arguments:
        df(str): name of the dataframe on which to run the method
        column_name(str): name of the column on which to remove outliers
        """
        Q1 = df[column_name].quantile(0.25)
        Q3 = df[column_name].quantile(0.75)
        IQR = Q3 - Q1
        lower_fence = Q1 - 1.5 * IQR
        upper_fence = Q3 + 1.5 * IQR
        df_no_outliers = df[(df[column_name] >= lower_fence) & (df[column_name] <= upper_fence)]
   



