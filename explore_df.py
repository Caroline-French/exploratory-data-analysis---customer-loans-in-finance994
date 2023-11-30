from matplotlib import pyplot as plt
import numpy as np
import pandas as pd 
import statsmodels.api as sm


class DataFrameInfo:

    def __init__(self, df):
        self.df = df

    def explore_df(self):
        """
        prints information about the dataframe
        """
        print ("Shape of the dataframe (number of rows, number of columns):", self.df.shape)
        print ("\n")
        print ("Dataframe head: \n", self.df.head())
        print ("\n")
        print ("Column names:\n", self.df.columns.to_list())
        print ("\n")

    
    def column_info(self, column_name=None):
        """
        prints information about a selected column in the database

        Arguments:
            column_name(str): name of column to check (if none given defaults to all columns)
        """
        if column_name is None:
            selected_columns = self.df.info()
        else:
            selected_columns = self.df[column_name].info()
        print ("\n\n",selected_columns)
        


    def print_unique_number(self, column_name):    
        """
        prints number of unique values in a column

        arguments:
            column_name(str): name of column to check
        """
        num_unique_values = self.df[column_name].nunique()
        print (f"\nNumber of unique values in column '{column_name}': {num_unique_values}\n")

    
    def print_unique(self, column_name):    
        """
        prints unique values in a column

        arguments:
        column_name(str): name of column to check
        """
        unique_values = self.df[column_name].unique()
        print (f"\nUnique values in column '{column_name}': {unique_values}\n")


    def check_max(self, column_name):
        """
        prints maximum value in a column
        
        Arguments:
            column_name(str): name of column to check
            """
        max_value = self.df[column_name].max()
        print (f"\nMaximum value in column '{column_name}': {max_value}")

    
    def describe_data(self, column_name=None):
        """
        describes the selected numeric column(s) in the database - count, mean, std, min, 25%, 50%, 75%, max

        Arguments:
            column_name(list or None): name(s) of column to check (if none given defaults to all columns, will not return columns that are not numeric)
        """
        if column_name is None:
            selected_columns = self.df.describe()
        else:
            selected_columns = self.df.loc[:, column_name].describe()  
        print (f"\nDescription of column '{column_name}':\n\n",selected_columns)

   
    def count_matching(self, column_A, column_B):
        """
        this method counts how many values match in 2 given columns
        
        arguments:
            column_A(str): the name of the first column to compare
            column_b(str): the name of the second column to compare
        """
        matching_values_count = (self.df[column_A] == self.df[column_B]).sum()
        print (f"Total number of matching values in {column_A} and {column_B}: {matching_values_count}")

   
    def sort_column(self, column_name):
        """
        this method sorts the dataframe by a given column in ascending order
        
        arguments:
            column_name(str): the name of the column to sort by
        """
        self.df.sort_values(by=column_name, ascending=True, inplace=True)

    
    def check_skew(self):
        numerical_columns = self.df.select_dtypes(include='number')
        skew_result = numerical_columns.skew()
        print(skew_result)
       
    def qq_plot(self, column_name):
        sm.qqplot(self.df[column_name], line="s")
        plt.title("QQ Plot")
        plt.show()


##data_load = pd.read_csv("C:/Users/Caroline/Documents/finance_project/exploratory-data-analysis---customer-loans-in-finance994/loan_payments.csv")

data_load = pd.read_csv("C:/Users/Caroline/Documents/finance_project/exploratory-data-analysis---customer-loans-in-finance994/loan_payments_complete_data.csv")
loan_df = DataFrameInfo(data_load)

## loan_df.explore_df()

#loan_df.column_info()

# make sure no duplicate loan ids
#loan_df.check_duplicates("id")

#check max value to decide best int type
# loan_df.describe_data(["loan_amount", "funded_amount", "dti"])

## loan_df.print_unique("mths_since_last_record")
# loan_df.describe_data("total_accounts")

## loan_df.count_matching("loan_amount", "funded_amount")

## loan_df.check_skew()
## loan_df.qq_plot("loan_amount")

loan_df.describe_data("loan_amount")