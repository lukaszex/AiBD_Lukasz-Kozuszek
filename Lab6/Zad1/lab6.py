# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:19:05 2019

@author: student188
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns

if __name__ == "__main__":
    df = pd.read_csv('exercise.csv')
    df = df[:40]
    print(df.info())
    X = df[['x1', 'x2']]
    Y = df['y']
    X = sm.add_constant(X)
    results = sm.OLS(Y, X).fit()
    print(results.summary())
    const = 1.3151
    x1_coef = 0.5148
    x2_coef = 0.8069
    df = pd.read_csv('exercise.csv')
    df = df[40:]
    x1 = df['x1']
    x2 = df['x2']
    for row in df:
        predY = const + x1_coef * x1 + x2_coef * x2
    print(predY)
    df = pd.read_csv('exercise.csv')
    Ypred = results.predict(X)
    sns.residplot(df['x1'], df['y'], lowess = True)
    plt.show()
    sns.residplot(df['x2'], df['y'], lowess = True)
    plt.show()