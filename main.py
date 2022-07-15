# %%
import os.path
import re
import sys

import pandas as pd


# ATTENTION: THE DATA FILE MUST BE FORMATTED AS UTF-8
# There is two input ways of data: data_chuva.csv and data_clima.csv


def sum_n_days(array, n):
    right__sum = pd.Series(array).rolling(n, min_periods=n, closed='right').sum()
    return pd.Series(right__sum).dropna()


def validate_path(data_path):
    path = os.path.split(data_path)[-1].lower()
    if not ('chuva' in path or 'clima' in path):
        raise RuntimeError(
            f'File \"{data_path}\" must contain either \"chuva\" or \"clima\" to specify the desired format')


def load_clima(df: pd.DataFrame):
    cols = filter(lambda x: re.fullmatch(r'^Clima\d*$', x), df.columns)
    return df.where(df['ParametroClima'] == 70)[cols].dropna()


def load_chuva(df: pd.DataFrame):
    cols = filter(lambda x: re.fullmatch(r'^Chuva\d*$', x), df.columns)
    return df[cols].dropna()


def main(data_path):
    validate_path(data_path)

    is_clima = 'clima' in os.path.split(data_path)[-1].lower()
    print(f'Using data in [{"clima" if is_clima else "chuva"}] format')

    df = pd.read_csv(data_path, encoding='UTF8', delimiter=';', index_col=False, decimal=",")
    df_data = load_clima(df) if is_clima else load_chuva(df)

    if df_data.size == 0:
        raise RuntimeError("Check if the [Chuva] headers are available")

    flat = df_data.values.flatten()

    range_days = (1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 60)
    sums = {}

    for amount_days in range_days:
        sums[amount_days] = sum_n_days(flat, amount_days)
        print(f'Max for {amount_days} days: {sums[amount_days].max():.2f}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        raise RuntimeError('Must specify a valid path to data')
