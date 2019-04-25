"""
Here is to transform raw data into features for modeling.
"""

"""
SET UP RELATIVE PATH
"""
import sys
import os
absFilePath = os.path.abspath(__file__)
fileDir = os.path.dirname(os.path.abspath(__file__))
rootDir = os.path.dirname(os.path.dirname(fileDir))
utility_path = os.path.join(rootDir, 'src', 'utility')   # Get the directory for StringFunctions
data_path = os.path.join(rootDir, 'data')
sys.path.extend([utility_path,data_path])

"""
IMPORTS
"""
from custom_func import read_csv,to_date
import pandas as pd
import datetime

"""
@return: pandas.core.frame.DataFrame
"""
def raw_data_processor():
    DATE_COLUMN_NAME = "date"
    df = read_csv(data_path+"/raw/data.csv")
    df[DATE_COLUMN_NAME] = df.date.map(lambda x: to_date(x))
    print("MESSAGE: data row before cleaning: " + str((df.shape)[0]))
    df = clean_data(df)
    print("MESSAGE: data row before cleaning: " + str((df.shape)[0]))
    return df

"""
@return: pandas.core.frame.DataFrame
"""
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    df = clean_outliner(df)
    return df

"""
@return: pandas.core.frame.DataFrame
"""
def clean_outliner(df: pd.DataFrame) -> pd.DataFrame:
    return df

"""
@param: String start, String end
Both in foramt of YYYYMMDD
@return: pandas.core.frame.DataFrame
"""
def get_historical_data(df, start: int, end:int=None):
    DATE_COLUMN_NAME = "date"
    if not(end):
        end = datetime.datetime.now()
    else:
        end = to_date(end)
    start = to_date(start)
    date_series = df[DATE_COLUMN_NAME]
    date_mask = (date_series > start) & (date_series <= end)
    return df.loc[date_mask]

if __name__ == '__main__':
    #testing purpose
    # df = pd.read_csv("../../data/raw/data.csv")
    df = raw_data_processor()
    print(get_historical_data(df, 20110109))
    # print(len(df.index))
    # df = clean_data(df)
    # print(len(df.index))
