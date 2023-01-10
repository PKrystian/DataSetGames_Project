import pandas as pd

class Normalizer:
    def __init__(self):
        pass

    def drop_cols(df, column_list):
        for column in column_list:
            if column in df.columns:
                df.drop(column, inplace = True, axis = 1)

    def one_hot_encoder(df, value_list, column_name):
        for value in value_list:
            df[value] = 0

        for i in range(len(df[column_name])):
            value = df[column_name].iloc[i]
            df[value].iloc[i] = 1

        df.drop(column_name, inplace = True, axis = 1)
