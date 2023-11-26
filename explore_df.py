import pandas as pd 

## load the data from the local file into a Pandas dataframe and define as a global variable
df = pd.read_csv("C:/Users/Caroline/Documents/finance_project/exploratory-data-analysis---customer-loans-in-finance994/loan_payments.csv")

def explore_df():
    """
    returns information about the dataframe
    """
    print ("Shape of the dataframe (number of rows, number of columns):", df.shape)
    print ("\n")
    print ("Dataframe head: \n", df.head())
    print ("\n")
    print ("Column names:\n", df.columns.to_list())
    print ("\n")
    print (df.info())


def check_duplicates():    
    """
    checks each loan has a unique id
    """
    print ("Number of unique ids (column 0):", df["id"].nunique())

def check_max(column):
    max_value = df[column].max()
    print ("maximum value in column:", max_value)

# explore_df()
# check_duplicates()
check_max("loan_amount")