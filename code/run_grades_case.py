from __future__ import print_function
from __future__ import absolute_import
from sklearn import preprocessing
import pandas as pd
import numpy as np
from pipeline_gridsearch import *


def get_data():
    df = pd.read_csv('grades.csv')
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    return X, y


def main():
    X, y = get_data()
    out = open('grades_performance.csv', 'w')
    out.write('model,slice,acc,mse,time\n')

    name = 'grades'
    na_values = 'NaN'

    for i in range(2, 6):
        cols = ['c1', 'mc']
        sub = str(i) + "H"
        for j in range(2, i+1):
            cols.append('c' + str(j))
        sub_X = preprocess(X[cols], na_values)
        run_pipeline(sub_X, y, 10, out, sub, name)
    out.close()


if __name__ == '__main__':
   main()

