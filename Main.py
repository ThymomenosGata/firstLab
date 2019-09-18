import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def open_file_get_date_frame():
    df = pd.read_csv('AB_NYC_2019.csv', sep=',')
    df = df.dropna()
    return df


def get_max_price():
    df = open_file_get_date_frame()
    print('max price: ')
    print(max(df['price']))
    print('\n')


def get_min_price():
    df = open_file_get_date_frame()
    print('min price: ')
    print(min(df['price']))
    print('\n')


def get_max():
    df = open_file_get_date_frame()
    print('top 5 min price: \n')
    print(df['price'].sort_values(ascending=[False]).head(5))
    print('\n')


def get_min():
    df = open_file_get_date_frame()
    print('top 5 min price: \n')
    print(df['price'].sort_values(ascending=[True]).head(5))
    print('\n')


def plot_graf():
    df = open_file_get_date_frame()
    df.groupby("neighbourhood_group")['price'].mean().plot(kind='bar')
    plt.show()


if __name__ == '__main__':
    get_max_price()
    get_min_price()
    get_max()
    get_min()
    plot_graf()

