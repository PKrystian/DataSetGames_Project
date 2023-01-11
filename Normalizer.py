import pandas as pd

class Normalizer:
    ''' Normalizer object contains functions for normalizing data '''
    def __init__(self):
        pass

    def one_hot_encoder(self, df, value_list, column_name):
        ''' One hot encodes a given column from DataFrame '''
        for value in value_list:
            df[value] = 0

        for i in range(len(df[column_name])):
            value = df[column_name].iloc[i]
            df[value].iloc[i] = 1

        df.drop(column_name, inplace = True, axis = 1)
