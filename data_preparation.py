import pandas as pd


df = pd.read_csv('data.csv')


def data_cleaning_preparation():
    """ Data Cleaning and Preparation"""

    # using median as representation for missing values since the data contain outliers.
    median_salalry = df[(df['Salary'] != "not_applicable") & (df['Salary'] != "not_available")]['Salary'].astype(float).median()

    # replace "not_applicable", and 'not_available' values with median salary
    df['Salary'][df['Salary'] == "not_applicable"] = median_salalry
    df['Salary'][df['Salary'] == "not_available"] = median_salalry

    df['Salary'].fillna(median_salalry, inplace=True)

    # convert data type of Salary to float
    df['Salary'] = df['Salary'].astype(float)
    # remove negative values
    df['Salary'] = df['Salary'].abs()

    # since the ID is sorted incrementally from 1 to 20 (the end of the dataset)
    # then fill the missing ID wth a number that represent the order of the row
    for i in range(len(df)):
        if df['ID'][i] != i+1:
            df['ID'][i] = i+1

    # convert ID to int
    df['ID'] = df['ID'].astype(int)

    # unify the datetime format where "-" is the separator
    df['Date_of_Birth'] = df['Date_of_Birth'].str.replace('/', '-')
    # replace "not_available" with missing values to facilitate imputation
    df['Date_of_Birth'] = df['Date_of_Birth'].str.replace('not_available', 'NaN')
    # convert "Date_of_Birth" to datetime and using backward fill to fill the missing values
    df['Date_of_Birth'] = pd.to_datetime(df['Date_of_Birth'], format='%Y-%m-%d', errors='coerce').bfill()
    
    return df