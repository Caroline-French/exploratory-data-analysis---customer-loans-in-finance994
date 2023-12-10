import pandas as pd

class DataTransform:
    """
    This class contains static methods to transform columns in a Pandas dataframe
    """

    @staticmethod    
    def transform_dtype(df, column_name, new_type):
        """
        this method transforms the datatype in a give column to a new datatype
        NB: does not work for transforming to datetime - see separate method
        Arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): name of column
            new_type(dtype): the datatype to transform the data into
        """
        df[column_name] = df[column_name].astype(new_type)
        
    
    @staticmethod
    def transform_datetime(df, column_name):
        """
        this method transforms a column to datetime format
        
        arguments:
        df(str): name of the dataframe to run the method on
        column_name(str): the name of the column to transform
        """
        date_format = '%b-%Y'
        df[column_name] = pd.to_datetime(df[column_name], format = date_format)

    
    @staticmethod
    def replace_col_entries(df, column_name, old_value, new_value):
        """
        this method replaces a selected value in a column with a new value
        
        Arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): name of column to change
            old_value(str): the value that should be replaced
            new_value(str): the new value to insert
        """
        df[column_name] = df[column_name].str.replace(old_value, new_value, regex=False)


    @staticmethod
    def rename_column(df, column_name, new_column_name):
        """
        this method renames columns in the dataframe
        
        arguments:
            df(str): name of the dataframe to run the method on
            column_name(str): the name of the column to rename
            new_column_name(str): the new column name
        """
        df.rename(columns = {column_name: new_column_name}, inplace=True)

   
    @staticmethod
    def cut_column(df, column_name, new_column_name, bins, labels):
        df[new_column_name] = pd.cut(df[column_name], bins=bins, labels=labels, right=False)
    
    


