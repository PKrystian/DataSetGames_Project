import pandas as pd

class DataManager:
    ''' Manager object for managing DataFrames, inserting values, displaying info and removing data '''
    def __init__(self):
        pass

    def get_data(self, dataset):
        ''' Reads a csv file and returns a DataFrame object '''
        return pd.read_csv(dataset)

    def get_unique_col(self, df, column):
        ''' Returns unique values for a given column in a dataframe '''
        return df[column].unique()

    def show_df_info(self, df):
        ''' Shows information about a given DataFrame '''
        return df.describe()

    def rename_cols(self, df, current_col_names, new_col_names):
        ''' Renames columns in a given DataFrame based on input '''
        col_dict = dict.fromkeys(current_col_names)

        iter = 0

        for key in col_dict.keys():
            col_dict[key] = new_col_names[iter]
            iter += 1

        df.rename(columns = col_dict, inplace = True)

    def drop_cols(self, df, column_list, axis = 1):
        ''' Removes cols based on column_list in a given DataFrame '''
        for column in column_list:
            if column in df.columns:
                df.drop(column, inplace = True, axis = axis)

    def remove_null_values(self, df):
        ''' Removes null values from a given DataFrame '''
        return df.dropna()

    def remove_null_cols(self, df):
        ''' Removes null columns from a given DataFrame '''
        return df.loc[:, df.columns.notna()]
