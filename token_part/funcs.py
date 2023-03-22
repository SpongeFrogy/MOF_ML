import pandas as pd
import numpy as np
import json


def numberDict(dataframe, column_name):
    """
    Выбирает в dataframe столбец column_name,
    выбирает из него уникальные значения и выводит {'val': number,...}
    """
    if dataframe[column_name].dtypes in [np.dtype(object), np.dtype(str)]:
        res_dict = dict(zip(dataframe[column_name].unique(), list(range(len(dataframe[column_name].unique())))))
    else:
        res_dict = dict(zip(dataframe[column_name], dataframe[column_name]))

    return res_dict

class Dataset:
    def __init__(self, path_to_csv):
        dataframe = pd.read_csv(path_to_csv, sep=',', index_col=0)
        self.df = dataframe
        self.columns = dataframe.columns
        # self.tokenDictFunc = dict(zip(list(dataframe.columns), 
        #                      list((lambda val: numberDict(dataframe, _col)[val]) for _col in dataframe.columns))) # попробовать без лист  
        self.token_dicts = dict(zip(list(dataframe.columns), [None]*len(dataframe.columns)))     
        
    def tokenize_column(self, column, token_func=None):
        if token_func == None:
            token_func = numberDict(self.df, column)
            if self.token_dicts[column] == None:
                self.token_dicts[column] = token_func
        self.df[column] = self.df[column].map(token_func)
        return self.token_dicts[column]
    def tokenize_df(self, token_funcs=None):
        for _col in self.columns:
            self.tokenize_column(_col)
    def dset2csv(self, **params):
        self.df.to_csv(**params)
    def dset2json(self, **params):
        self.df.to_json(**params)
    def token2csv(self, column, filename, sep=','):
        with open(filename, 'w') as f:
            for key in self.token_dicts[column].keys():
                f.write("%s%s %s\n" % (key, sep, self.token_dicts[column][key]))
    def token2json(self, column, filename):
        with open(filename, "w") as f:
            json.dump(self.token_dicts[column], f)
        

