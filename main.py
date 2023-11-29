import csv

import pandas as pd


def read_data():
    file_name = 'accidents.csv'
    return pd.read_csv(file_name)


def explore(df):
    years = df["year"].unique()
    print(years)
    return years


if __name__ == '__main__':
    data = read_data()
    explore(data)
