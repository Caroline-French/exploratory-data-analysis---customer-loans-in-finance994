import pandas as pd

class DataTransform:
    """
    This class contains methods to transform columns in a Pandas dataframe
    
    Attributes:
        self.df(str): the dataframe on which to perform the transformations
    """

    def __init__(self, df):
        self.df = df
        
    def transform_dtype(self, column_name, new_type):
        """
        this method transforms the datatype in a give column to a new datatype
        NB: does not work for transforming to datetime - see separate method
        Arguments:
            column_name(str): name of column
            new_type(dtype): the datatype to transform the data into
        """
        self.df[column_name] = self.df[column_name].astype(new_type)
        
    def transform_datetime(self, column_name):
        """
        this method transforms a column to datetime format
        
        arguments:
        column_name(str): the name of the column to transform
        """
        date_format = '%b-%Y'
        self.df[column_name] = pd.to_datetime(self.df[column_name], format = date_format)

    def replace_col_entries(self, column_name, old_value, new_value):
        """
        this method replaces a selected value in a column with a new value
        
        Arguments:
            column_name(str): name of column to change
            old_value(str): the value that should be replaced
            new_value(str): the new value to insert
        """
        self.df[column_name] = self.df[column_name].str.replace(old_value, new_value, regex=False)


    def rename_column(self, column_name, new_column_name):
        """
        this method renames columns in the dataframe
        
        arguments:
            column_name(str): the name of the column to rename
            new_column_name(str): the new column name
        """
        self.df.rename(columns = {column_name: new_column_name}, inplace=True)

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

    def print_head(self, column_name=None):
        if column_name is None:
            selected_columns = self.df.head()
        else:
            selected_columns = self.df.loc[:, column_name].head()  
        print (selected_columns)

    def save_changes(self, file_name):
        """
        this method saves the changes to a new csv file in the current directory
        
        arguments:
            file_name(str): the new file name, include the .csv extension
        """
        self.df.to_csv(file_name, index=False)


if __name__ == "__main__":
    
    data_load = pd.read_csv("C:/Users/Caroline/Documents/finance_project/exploratory-data-analysis---customer-loans-in-finance994/loan_payments.csv")
    loan_df = DataTransform(data_load)

    ## 0 transform id to int32 for memory efficiency
    loan_df.transform_dtype("id", "int32")

    ## 1 transform member_id to int32 for memory efficiency
    loan_df.transform_dtype("member_id", "int32")

    ## 2 transform loan_amount to int16 for memory efficiency
    loan_df.transform_dtype("loan_amount", "int16")

    ## 3 transform funded_amount to float16 for memory efficiency
    loan_df.transform_dtype("funded_amount", "float16")

    ## 4 transform funded_amount_inv to float16 for memory efficiency
    loan_df.transform_dtype("funded_amount_inv", "float16")

    ## 5 remove 'months' from term column, transform dtype to int8, change column name to include "months"
    loan_df.replace_col_entries("term", "months", "")
    ## need to deal with missing data first - loan_df.transform_dtype("term", "int8")
    loan_df.rename_column("term", "term_months")

    ## 7 change instalment to float16
    loan_df.transform_dtype("instalment", "float16")
    
    ## 8 transform grade to category
    loan_df.transform_dtype("grade", "category")

    ## 9 transform sub_grade to category
    loan_df.transform_dtype("sub_grade", "category")

    ## 10 transform employment_length to category and column name to employment_years (may want to bring together categories more later)
    loan_df.transform_dtype("sub_grade", "category")
    loan_df.rename_column("employment_length", "employment_years")

    ## 11 transform home_ownership to category
    loan_df.transform_dtype("home_ownership", "category")

    ## 12 transform annual_inc to float16 for memory efficiency
    loan_df.transform_dtype("annual_inc", "float16")

    ## 13 transform verification_status to category
    loan_df.transform_dtype("verification_status", "category")

    ## 14 transform issue_date to datetime
    loan_df.transform_datetime("issue_date")

    ## 15 transform loan_status to category
    loan_df.transform_dtype("loan_status", "category")

    ## 16 transform payment_plan to category
    loan_df.transform_dtype("payment_plan", "category")

    ## 17 transform purpose to category
    loan_df.transform_dtype("purpose", "category")

    ## 19 transform delinq_2yrs to int8
    loan_df.transform_dtype("delinq_2yrs", "int8")

    ## 20 transform earliest_credit_line to datetime
    loan_df.transform_datetime("earliest_credit_line")

    ## 21 transform inq_last_6mths to int8
    loan_df.transform_dtype("inq_last_6mths", "int8")

    ## 22 transform mths_since_last_delinq to float16 (possibly could be integer?)
    loan_df.transform_dtype("mths_since_last_delinq", "float16")

    ## 23 transform mths_since_last_record to float16 (possibly could be integer?)
    loan_df.transform_dtype("mths_since_last_record", "float16")

    ## 24 transform open_accounts to int8
    loan_df.transform_dtype("open_accounts", "int8")

    ## 25 transform total_accounts to int8
    loan_df.transform_dtype("total_accounts", "int8")

    ## 26 transform out_prncp to float16
    loan_df.transform_dtype("out_prncp", "float16")

    ## 27 transform out_prncp_inv to float16
    loan_df.transform_dtype("out_prncp_inv", "float16")

    ## 28 transform total_payment to float16
    loan_df.transform_dtype("total_payment", "float16")

    ## 29 transform total_payment_inv to float16
    loan_df.transform_dtype("total_payment_inv", "float16")

    ## 30 transform total_rec_prncp to float16
    loan_df.transform_dtype("total_rec_prncp", "float16")

    ## 31 transform total_rec_int to float16
    loan_df.transform_dtype("total_rec_int", "float16")

    ## 32 transform total_rec_late_fee to float16
    loan_df.transform_dtype("total_rec_late_fee", "float16")

    ## 33 transform recoveries to float16
    loan_df.transform_dtype("recoveries", "float16")

    ## 34 transform collection_recovery_fee to float16
    loan_df.transform_dtype("collection_recovery_fee", "float16")

    ## 35 transform last_payment_date to datetime
    loan_df.transform_datetime("last_payment_date")

    ## 36 transform last_payment_amount to float16
    loan_df.transform_dtype("last_payment_amount", "float16")

    ## 37 transform next_payment_date to datetime
    loan_df.transform_datetime("next_payment_date")

    ## 38 transform last_credit_pull_date to datetime
    loan_df.transform_datetime("last_credit_pull_date")

    ## 39 transform collections_12_mths_ex_med to int8
    loan_df.transform_dtype("collections_12_mths_ex_med", "float16")

    ## 40 transform mths_since_last_major_derog to int8
    loan_df.transform_dtype("mths_since_last_major_derog", "float16")

    ## 41 transform policy_code to category
    loan_df.transform_dtype("policy_code", "category")

    ## 42 transform application_type to category
    loan_df.transform_dtype("application_type", "category")



    ## checking the changes
    loan_df.column_info()
    loan_df.print_head("last_payment_date")
    loan_df.print_head("term_months")

    ## saving the changes as a new .csv file
    loan_df.save_changes("loan_payments_transformed_columns.csv")