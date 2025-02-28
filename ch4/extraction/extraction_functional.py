import sqlite3
import certifi
import pandas as pd
import urllib3

def source_data_from_parquet(parquet_file_name):
    try:
        df_parquet = pd.read_parquet(parquet_file_name)
    except Exception as e:
        df_parquet = pd.DataFrame()
    return df_parquet

def source_data_from_csv(csv_file_name):
    try:
        df_csv = pd.read_csv(csv_file_name)
    except Exception as e:
        df_csv = pd.DataFrame()
    return df_csv



