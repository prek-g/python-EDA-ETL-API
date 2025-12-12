import pandas as pd
import numpy as np
import os
import time
import openpyxl
import xlrd
import random

# data_path = 'day19_sales.xlsx'
# data_name = 'sales'

# Its important I save this as a function so i can call it whenever i want to clean other files
def data_cleaning_function(data_path, data_name):

    print("Thank you for giving the details!")
    sec=random.randint(1,4)
    print(f"Please wait {sec} seconds...")
    time.sleep(sec)

    # checking if the path is correct or not

    if not os.path.exists(data_path):
        print("Please enter the correct data path")
        return #if this file doesnt exist return is going to cancel the function

    else:
        # all the logic here if the path exists
        # checking the file type
        if data_path.endswith('.csv'):
            print("Dataset is csv !")
            # now we have to read the csv file
            data = pd.read_csv(data_path, encoding_errors='ignore')

        elif data_path.endswith('.xlsx'):
            print("Dataset is excel !")
            data = pd.read_excel(data_path) # no encoding error here

        else:
            print("Dataset is not csv or excel !")
            return
    print(f"Please wait for {sec}seconds! Checking total columns and rows")
    time.sleep(sec)

    print(f"Dataset contains total rows: {data.shape[0]}\n Total columns: {data.shape[1]}")

    # cleaning
    print(f"Please wait for {sec}seconds!")
    #checking duplicates
    duplicates = data.duplicated()
    total_duplicates = data.duplicated().sum()

    # now we want to show the duplicates
    print(f"Dataset has total duplicates: {total_duplicates}")

    # saving the duplicates for logging purposes
    if total_duplicates > 0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)

    # deleting duplicates and saving the new duplicate-less df as a new clean dataset
    df = data.drop_duplicates().copy() # VERY IMPORTANT.
    # Pandas considers df a slice of the original DF and you need to consider it as a copy so pandas wont show errors
    #of the sort that you might risk changing the original dataframe unintentionally
    # guarantees DF to be an independent real DataFrame object and not a view

    # finding missing/null values
    null_colums_values = data.isnull().sum()
    total_null_values = data.isnull().sum().sum()
    print(f"Dataset has total missing values : {total_null_values}")
    print(f"Dataset has null values by columns :\n{null_colums_values}")
    if total_null_values > 0:

    # replacing null values with mean
        columns = df.columns
        """
        returns all columns and then check their type
        depending on their type, missing values will either be replaces with mean or dropped
        """
        for col in columns:
            if df[col].dtype in [float, int]:
                df.loc[:, col] = df[col].fillna(df[col].mean())

                """
                if you want to exclude 2 columns that are object type then:
                
                # Columns you want to exclude from dropping
                exclude_cols = ['col_to_keep1', 'col_to_keep2']
                
                for col in df.columns:
                    if df[col].dtype in [float, int]:  # numeric columns
                        df[col] = df[col].fillna(df[col].mean())
                    else:  # object columns
                        if col not in exclude_cols:
                            df.dropna(subset=[col], inplace=True)  # drop rows with NaN in this column
                """

            else: #object
                df.dropna(subset=[col], inplace=True)

    # data is clean
    print(f"Congrats! Dataset is cleaned.\nNumber of rows:{df.shape[0]}\nNumber of columns:{df.shape[1]}")

    #saving the clean data
    df.to_csv(f'{data_name}_clean_data.csv', index=None)
    print("Dataset is saved!")

# either we can go to this file and call this function or write :

if __name__ == "__main__":
    print("Please enter your data path and name of the file you want to clean")
    data_path='day19_walmart.xlsx'
    data_name='wlm'
    data_cleaning_function(data_path, data_name)