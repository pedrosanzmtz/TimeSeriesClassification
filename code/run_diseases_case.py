from __future__ import print_function
from __future__ import absolute_import
from sklearn import preprocessing
import pandas as pd
import numpy as np
from pipeline_gridsearch import *

if __name__ == '__main__':    
    out = open('diseases_performance.csv', 'w')
    out.write('model,slice,acc,mse\n')

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
