import pandas as pd

class DataTransform:

    def __init__(self, df):
        self.df = df
        
    def transform_dtype(self, column, new_type):
        """
        this method transforms the datatype in a give column to a new datatype
        
        Arguments:
            column(str): name of column
            new_type(dtype): the datatype to transform the data into
        """
        self.df[column] = self.df[column].astype(new_type)
        

data_load = pd.read_csv("C:/Users/Caroline/Documents/finance_project/exploratory-data-analysis---customer-loans-in-finance994/loan_payments.csv")
loan_df = DataTransform(data_load)

## transform id to int32 for memory efficiency
loan_df.transform_dtype("id", "int32")

## transform member_id to int32 for memory efficiency
loan_df.transform_dtype("member_id", "int32")

## transform loan_amount to int16 for memory efficiency
loan_df.transform_dtype("loan_amount", "int16")



print(loan_df.df.info()) 