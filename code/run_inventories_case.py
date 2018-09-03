from __future__ import print_function
from __future__ import absolute_import
from sklearn import preprocessing
import pandas as pd
import numpy as np
from pipeline_gridsearch import *

if __name__ == '__main__':
    df = pd.read_csv('inventariosActivos.csv', index_col=0, na_values=['NaN', 'NA'])
    # remove client column
    df = df.drop(['client'], axis=1)

    # X and y
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # remove first 3 months and last 3 months
    X = X.iloc[:, 3:-3]
    
    X = X.dropna(how='all', axis=0)

    na_index = X.isnull().all(axis=1)

    out = open('inventories_performance.csv', 'w')
    out.write('model,slice,acc,mse\n')

    n_months = 6
    name = 'inventories'
    na_values = np.nan

    for i in range(1, n_months + 1):
        sub = str(i) + 'M'
        sub_X = X.iloc[:, :-i]
        sub_X = sub_X.dropna(how='all', axis=0)
        indx = sub_X.index
        sub_y = y[indx]
        sub_X = preprocess(sub_X, na_values)
        run_pipeline(sub_X, sub_y, 10, out, sub, name)

    out.close()
    