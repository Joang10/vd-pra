from datetime import datetime

import pandas as pd


def read_data():
    file_name = 'accidents_clean.csv'
    return pd.read_csv(file_name)


def clean(df):
    df = df[(df['district_name'] != 'Desconegut') & (df['district_name'] != '') & (df['weekday'] != '')]

    df = df.dropna(subset=['year'])
    df = df.dropna(subset=['month'])
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df['date'] = df.apply(lambda row: datetime(row['year'], row['month'], 1), axis=1)

    df['street_name'] = df['street_name'].str.strip()
    df.to_csv('accidents_clean.csv', index=False)


def explore(df):
    df_by_district = df.groupby('district_name').size().reset_index(name='count')
    df_by_district.to_csv('count_by_district.csv', index=False)

    df_by_neighborhood = df.groupby('neighborhood_name').size().reset_index(name='count')
    df_by_neighborhood.to_csv('count_by_neighborhood.csv', index=False)


def grouped_by_weekday(df):
    order = ['Dilluns', 'Dimarts', 'Dimecres', 'Dijous', 'Divendres', 'Dissabte', 'Diumenge']
    df_grouped = df.groupby('weekday_name').size().reindex(order, fill_value=0).reset_index(name='count')
    df_grouped.to_csv('accidents_by_weekday.csv', index=False)


def grouped_by_cause(df):
    df_grouped = df.groupby('cause_incident').size().reset_index(name='count')
    df_grouped = df_grouped.sort_values(by='count')
    df_grouped.to_csv('accidents_by_cause.csv', index=False)


if __name__ == '__main__':
    data = read_data()
    clean(data)
    # explore(data)
    # grouped_by_weekday(data)
    # grouped_by_cause(data)
