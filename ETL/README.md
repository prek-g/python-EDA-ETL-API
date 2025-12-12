# Python Data Cleaning Script

![terminal](terminal.png)

## Objective
This Python script provides a **reusable function** to clean datasets (CSV or Excel files). The main objectives are:  

- Automatically detect the file type (CSV or Excel) and read it.  
- Check for duplicates and missing values in the dataset.  
- Remove duplicates and handle missing values (replace numeric columns with mean, drop rows for object columns).  
- Save both the **duplicates** and **cleaned dataset** for logging and further analysis.  
- Make it reusable so it can be applied to any dataset by simply calling the function.  

---

## Features
- Supports `.csv` and `.xlsx` files.  
- Handles missing values intelligently depending on column type.  
- Creates a separate CSV for duplicate records.  
- Saves a cleaned version of the dataset automatically.  
- Includes random delays for simulation of processing time.  

---

## Python Script

```python
import pandas as pd
import numpy as np
import os
import time
import openpyxl
import xlrd
import random

def data_cleaning_function(data_path, data_name):
    print("Thank you for giving the details!")
    sec = random.randint(1,4)
    print(f"Please wait {sec} seconds...")
    time.sleep(sec)

    # checking if the path is correct or not
    if not os.path.exists(data_path):
        print("Please enter the correct data path")
        return

    else:
        # checking the file type
        if data_path.endswith('.csv'):
            print("Dataset is csv !")
            data = pd.read_csv(data_path, encoding_errors='ignore')
        elif data_path.endswith('.xlsx'):
            print("Dataset is excel !")
            data = pd.read_excel(data_path)
        else:
            print("Dataset is not csv or excel !")
            return

    print(f"Please wait for {sec} seconds! Checking total columns and rows")
    time.sleep(sec)
    print(f"Dataset contains total rows: {data.shape[0]}\n Total columns: {data.shape[1]}")

    # checking duplicates
    print(f"Please wait for {sec} seconds!")
    duplicates = data.duplicated()
    total_duplicates = data.duplicated().sum()
    print(f"Dataset has total duplicates: {total_duplicates}")

    # save duplicates for logging
    if total_duplicates > 0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index=None)

    # drop duplicates
    df = data.drop_duplicates().copy()

    # finding missing/null values
    null_colums_values = data.isnull().sum()
    total_null_values = data.isnull().sum().sum()
    print(f"Dataset has total missing values : {total_null_values}")
    print(f"Dataset has null values by columns :\n{null_colums_values}")

    if total_null_values > 0:
        columns = df.columns
        for col in columns:
            if df[col].dtype in [float, int]:
                df.loc[:, col] = df[col].fillna(df[col].mean())
            else:  # object columns
                df.dropna(subset=[col], inplace=True)

    # dataset is clean
    print(f"Congrats! Dataset is cleaned.\nNumber of rows:{df.shape[0]}\nNumber of columns:{df.shape[1]}")
    
    # saving the cleaned data
    df.to_csv(f'{data_name}_clean_data.csv', index=None)
    print("Dataset is saved!")

if __name__ == "__main__":
    print("Please enter your data path and name of the file you want to clean")
    data_path='day19_walmart.xlsx'
    data_name='wlm'
    data_cleaning_function(data_path, data_name)
```

### How to Use

Place your dataset (.csv or .xlsx) in the same directory or provide the full path.

Update data_path and data_name in the __main__ section.

Run the script.

The script will generate:

{data_name}_duplicates.csv → all duplicate rows

{data_name}_clean_data.csv → cleaned dataset


## Conclusions

- This script provides a flexible and reusable way to clean datasets.
- Automatically handles duplicates and missing values based on column types.
- Saves both cleaned and duplicate datasets for auditing and logging.
- Can be easily reused on any dataset by calling the data_cleaning_function.
- Reduces manual cleaning effort and ensures consistent preprocessing for data analysis or machine learning workflows.




