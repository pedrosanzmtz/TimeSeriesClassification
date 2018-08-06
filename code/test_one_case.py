from __future__ import print_function
from __future__ import absolute_import
from sklearn import preprocessing
import pandas as pd
import numpy as np
from pipeline_gridsearch import *

if __name__ == '__main__':


    ####################################################
    # For grades case

    # df = pd.read_csv('grades.csv')
    # X = df.iloc[:, :-1]
    # y = df.iloc[:, -1]

    # out = open('grades_performance.csv', 'w')
    # out.write('model,slice,accuracy\n')

    # name = 'grades'
    # na_values = 'NaN'

    # for i in range(2, 6):
    #     cols = ['c1', 'mc']
    #     sub = 'M_T' + str(i)
    #     print(sub)
    #     for j in range(2, i+1):
    #         cols.append('c' + str(j))
    #     print(cols)
    #     sub_X = preprocess(X[cols], na_values)
    #     run_pipeline(sub_X, y, 10, out, sub, name)
    # out.close()
    ####################################################

    ####################################################
    # For purchases example

    # df = pd.read_csv('inventariosActivos.csv', index_col=0, na_values=['NaN', 'NA'])
    # remove client column
    # df = df.drop(['client'], axis=1)

    # X and y
    # X = df.iloc[:, :-1]
    # y = df.iloc[:, -1]

    # print(X.shape)
    # remove first 3 months and last 3 months
    # X = X.iloc[:, 3:-3]
    # print(X.shape)
    # X = X.dropna(how='all', axis=0)
    # print(X.shape)
    # print(X.index)

    # na_index = X.isnull().all(axis=1)
    # print(na_index)

    # out = open('inventories_performance.csv', 'w')
    # out.write('model,slice,accuracy\n')

    # n_months = 6
    # name = 'inventories'
    # na_values = np.nan

    # for i in range(1, n_months + 1):
    #     sub = str(i) + 'M'
    #     sub_X = X.iloc[:, :-i]
    #     sub_X = sub_X.dropna(how='all', axis=0)
    #     indx = sub_X.index
    #     sub_y = y[indx]
    #     sub_X = preprocess(sub_X, na_values)
    #     run_pipeline(sub_X, sub_y, 10, out, sub, name)

    # out.close()
    # ####################################################

    # For diseases example

    out = open('diseases_performance.csv', 'w')
    out.write('model,slice,accuracy\n')

    df = pd.read_csv("diseases.csv")
    X = df.iloc[:, :-1]
    X_true = X.sum(axis=1) > 0
    X = X[X_true]
    le = preprocessing.LabelEncoder()
    y = pd.Series(le.fit(df['class']).transform(df['class']))
    y = y[X_true]

    n_weeks = 6
    name = 'diseases'
    na_values = np.nan
    for i in range(1, n_weeks + 1):
        sub = str(i) + 'W'
        sub_X = X.iloc[:, :-i]
        sub_X = sub_X.dropna(how='all', axis=0)
        indx = sub_X.index
        sub_y = y[indx]
        print("subX shape:", sub_X.shape)
        print("suby shape:", y.shape)
        sub_X = preprocess(sub_X, na_values)
        run_pipeline(sub_X, sub_y, 10, out, sub, name)
