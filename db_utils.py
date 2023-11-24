from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import yaml

class RDSDatabaseConnector:
    """
    This class is used to access the loans dataset from AWS RDS, create a Pandas dataframe, and save the data locally as a .csv file
     
    Attributes:
        credentials (dict): the host, port, database, user, and password needed to access the database
        engine (function): the function in the class that initialises the SQLAlchemy engine
    """


    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = self.initialise_SQLAlchemy()

    def initialise_SQLAlchemy(self):
        """
        This function initialises a SQLAcademy engine from credentials provided to RDSDatabaseConnector class

        Returns:
            SQLAcademy engine
        """
        
        database_type = "postgresql"
        DBAPI = "psycopg2"      
        host = self.credentials["RDS_HOST"]
        port = self.credentials["RDS_PORT"]
        database = self.credentials["RDS_DATABASE"]
        user = self.credentials["RDS_USER"]
        password = self.credentials["RDS_PASSWORD"]

        conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
        )
        
        engine = create_engine(f"{database_type}+{DBAPI}://{user}:{password}@{host}:{port}/{database}")
        conn.close()
        return engine 
 
    def create_df(self):
        """
        extracts data from the RDS database and returns as a Pandas dataframe

        Returns:
          The loan payments data as a Pandas dataframe
        """

        loan_payments_df = pd.read_sql_table('loan_payments', self.engine)
        return loan_payments_df

    def save_data(self):
        """
        saves the data as a .csv file to the specified file path on the local machine
        """

        loan_payments_df = self.create_df() 
        loan_payments_df.to_csv("C:/Users/Caroline/Documents/finance_project/exploratory-data-analysis---customer-loans-in-finance994/loan_payments.csv", index=False)


def load_credentials():
    """
    loads credentials to access the RDS database, to be passed as an argument into the RDSDatabaseConnector class
    """

    file_path = "C:/Users/Caroline/Documents/finance_project/exploratory-data-analysis---customer-loans-in-finance994/credentials.yaml"
    with open(file_path, "r") as file:
        credentials = yaml.safe_load(file)
        return credentials

credentials = load_credentials()
test_database = RDSDatabaseConnector(credentials)
test_database.initialise_SQLAlchemy()
test_database.create_df()
test_database.save_data()

def create_df():
    """
    loads the data into a Pandas dataframe and returns information about the dataframe
    """

    df = pd.read_csv("C:/Users/Caroline/Documents/finance_project/exploratory-data-analysis---customer-loans-in-finance994/loan_payments.csv")
    print ("Shape of the dataframe (number of rows, number of columns):", df.shape)
    print ("\n")
    print ("Dataframe head: \n", df.head())
    print ("\n")
    print ("Column names:\n", df.columns.to_list())

create_df()

