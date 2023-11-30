import missingno as msno
import pandas as pd

class DataFrameTransform:
    """
    this class is used to perform transformations on a pandas dataframe
    
    attributes:
        self.df(str): the dataframe on which to perform the transformations
    """

    def __init__(self, df):
        self.df = df

    def check_null_values(self):
        """
        this method is used to check the number and % of missing values in each column
        """
        data_null = self.df.isnull()
        print ("numbers of missing data:")
        print (data_null.sum())
        print ("\n")
        print ("percentage missing data:")
        print (data_null.mean() * 100)

    def drop_column(self, column_name):
        """
        this method is used to drop a column in the dataframe
        
        arguments:
            column_name(str): the name of the column to drop
        """
        self.df.drop(column_name, axis=1, inplace=True)

    def drop_rows_with_missing(self, column_name):
        """
        this method drops all rows where the data is missing for the given column
        
        arguments:
            column_name(str): the name of the column to check for missing values
        """
        self.df.dropna(subset=[column_name], inplace=True)

    
    def fill_missing_from_column(self, column_to, column_from):
        """
        this method fills the missing values in a column with the value from another column in the same row
        
        arguments:
            column_to(str): the name of the column with missing values to fill
            column_from(str): the name of the column to take the values from
        """
        self.df[column_to].fillna(self.df[column_from], inplace=True)

    def impute_mean(self, column_name):
        """
        this method imputes missing values in a given column with the mean value of that column
        
        arguments:
            column_name(str): the name of the column to impute mean values
        """
        self.df[column_name].fillna(self.df[column_name].mean(), inplace=True)

    def visualise_missing(self):
        """
        this method prints a plot of the missing data in each column
        """
        print(msno.matrix(self.df))

    def save_changes(self, file_name):
        """
        this method saves the changes to a new csv file in the current directory
        
        arguments:
            file_name(str): the new file name, include the .csv extension
        """
        self.df.to_csv(file_name, index=False)

if __name__ == "__main__":
    data_load = pd.read_csv("C:/Users/Caroline/Documents/finance_project/exploratory-data-analysis---customer-loans-in-finance994/loan_payments_transformed_columns.csv")
    loan_df = DataFrameTransform(data_load)

    loan_df.check_null_values()
    loan_df.visualise_missing()
    
    ## dropping 3 columns with high % missing data that are highly correlated on the graph
    ## in reality would check if missing data should be 0 or not applicable in months columns
    ## in reality would check the significance of these columns with domain expert
    loan_df.drop_column("mths_since_last_delinq")
    loan_df.drop_column("mths_since_last_record")
    loan_df.drop_column("mths_since_last_major_derog")

    ## dropping columns with missing data that are unlikely to be useful in the analysis
    loan_df.drop_column("next_payment_date")
    loan_df.drop_column("last_payment_date")
    loan_df.drop_column("term_months")

    ## dropping rows with missing data where could be important to keep the column
    loan_df.drop_rows_with_missing("last_credit_pull_date")
    loan_df.drop_rows_with_missing("collections_12_mths_ex_med")
    loan_df.drop_rows_with_missing("employment_years")

    ## filling missing values in the funded_amount column using the loan_amount column as 50283 matches
    loan_df.fill_missing_from_column("funded_amount", "loan_amount")

    ## fill missing values with the mean for int_rate column
    loan_df.impute_mean("int_rate")

    ## check columns and rows dropped successfully
    loan_df.check_null_values()
    loan_df.visualise_missing()
    
    ## save the new df
    loan_df.save_changes("loan_payments_complete_data.csv")

