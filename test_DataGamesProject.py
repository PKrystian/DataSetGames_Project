import pytest
import numpy as np
import pandas as pd

from DataManager import DataManager
from Normalizer import Normalizer

class TestDataManager:
    def test_get_unique_col(self):
        data_test = [1,2,3,4,5]
        df_test = pd.DataFrame(data_test, columns=['name'])
        Manager = DataManager()

        expected = [1,2,3,4,5]
        result = Manager.get_unique_col(df_test, 'name')

        np.testing.assert_array_equal(expected, result)

    def test_rename_cols(self):
        test_df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
        Manager = DataManager()

        expected = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'two', 'three'])

        Manager.rename_cols(test_df, ['b', 'c'], ['two', 'three'])

        result = test_df

        np.testing.assert_array_equal(expected.columns, result.columns)

    def test_drop_cols(self):
        test_df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
        Manager = DataManager()

        expected = pd.DataFrame(np.array([1, 4, 7]), columns=['a'])

        Manager.drop_cols(test_df, ['b', 'c'])

        result = test_df

        np.testing.assert_array_equal(expected, result)

    def test_one_hot_encoder(self):
        abc=['a','b','c']

        test = pd.DataFrame(abc, columns=['name'])
        Norm = Normalizer()

        expected = np.array([[1,0,0],[0,1,0],[0,0,1]])
        Norm.one_hot_encoder(test, test['name'].unique(), 'name')
        result = test

        np.testing.assert_array_equal(expected, result)