from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 
import statsmodels.api as sm


class DataFrameInfo:

    
    @staticmethod
    def shape_df(df):
        """
        prints information about the dataframe

        arguments:
            df(str): name of the dataframe to run the method on
        """
        print ("Shape of the dataframe (number of rows, number of columns):", df.shape)
        print ("\n")
        print ("Dataframe head: \n", df.head())
        print ("\n")
        print ("Column names:\n", df.columns.to_list())
        print ("\n")

    
    @staticmethod
    def print_head(df, column_name=None):
        """
        prints the head of the dataframe
        
        Arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): name of column to check (if none given defaults to all columns)
        """
        if column_name is None:
            selected_columns = df.head()
        else:
            selected_columns = df.loc[:, column_name].head()  
        print (selected_columns)
    
    
    @staticmethod
    def column_info(df, column_name=None):
        """
        prints information about a selected column in the database

        Arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): name of column to check (if none given defaults to all columns)
        """
        if column_name is None:
            selected_columns = df.info()
        else:
            selected_columns = df[column_name].info()
        print ("\n\n",selected_columns)
        

    @staticmethod
    def print_unique_number(df, column_name):    
        """
        prints number of unique values in a column

        arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): name of column to check
        """
        num_unique_values = df[column_name].nunique()
        print (f"\nNumber of unique values in column '{column_name}': {num_unique_values}\n")

    
    @staticmethod
    def print_unique(df, column_name):    
        """
        prints unique values in a column

        arguments:
        df(str): name of the dataframe to run the method on
        column_name(str): name of column to check
        """
        unique_values = df[column_name].unique()
        print (f"\nUnique values in column '{column_name}': {unique_values}\n")

    
    @staticmethod
    def check_max(df, column_name):
        """
        prints maximum value in a column
        
        Arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): name of column to check
            """
        max_value = df[column_name].max()
        print (f"\nMaximum value in column '{column_name}': {max_value}")

    
    @staticmethod
    def describe_data(df, column_name=None):
        """
        describes the selected numeric column(s) in the database - count, mean, std, min, 25%, 50%, 75%, max

        Arguments:
            df(str): name of the dataframe to run the method on
            column_name(list or None): name(s) of column to check (if none given defaults to all columns, will not return columns that are not numeric)
        """
        if column_name is None:
            selected_columns = df.describe()
        else:
            selected_columns = df.loc[:, column_name].describe()  
        print (f"\nDescription of column '{column_name}':\n\n",selected_columns)

    
    @staticmethod
    def count_matching(df, column_A, column_B):
        """
        this method counts how many values match in 2 given columns
        
        arguments:
            df(str): name of the dataframe to run the method on
            column_A(str): the name of the first column to compare
            column_b(str): the name of the second column to compare
        """
        matching_values_count = (df[column_A] == df[column_B]).sum()
        print (f"Total number of matching values in {column_A} and {column_B}: {matching_values_count}")

    
    @staticmethod
    def sort_column(df, column_name):
        """
        this method sorts the dataframe by a given column in ascending order
        
        arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): the name of the column to sort by
        """
        df.sort_values(by=column_name, ascending=True, inplace=True)

    
    @staticmethod
    def check_skew(df):
        """
        this method checks the skewness of all numerical columns
        
        arguments:
            df(str): name of the dataframe to run the method on
        """
        numerical_columns = df.select_dtypes(include='number')
        skew_result = numerical_columns.skew()
        print(skew_result)
       
    
    @staticmethod
    def save_changes(df, file_name):
        """
        this method saves the changes to a new csv file in the current directory
        
        arguments:
            df(str): the name of the dataframe to run the method on
            file_name(str): the new file name, include the .csv extension
        """
        df.to_csv(file_name, index=False)


    @staticmethod
    def check_null_values(df):
        """
        this method is used to check the number and % of missing values in each column

        arguments:
            df(str): name of the dataframe on which to run the method
        """
        data_null = df.isnull()
        print ("numbers of missing data:")
        print (data_null.sum())
        print ("\n")
        print ("percentage missing data:")
        print (data_null.mean() * 100)


    @staticmethod
    def value_counts(df, column_name):
        """
        this method prints the counts of each individual value in a column
        Arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): the name of the column to run the method on
        """
        value_counts = df[column_name].value_counts()
        print (value_counts)






