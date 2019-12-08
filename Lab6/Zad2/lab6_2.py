import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

if __name__ == "__main__":
    df = pd.read_csv('beauty.csv')
    X = df['btystdave']
    Y = df['courseevaluation']
    X = sm.add_constant(X)  # adding a constant
    model = sm.OLS(Y, X).fit()
    predictions = model.predict(X)
    print(model.summary())
    const = 4.01
    btystdave_coef = 0.133
    for row in df:
        pred_courseev = const + btystdave_coef * btystdave_coef
    sns.residplot(df['btystdave'], df['courseevaluation'], lowess=True)
    plt.show()

    X = df[['btystdave', 'btystdf2u', 'btystdfl', 'btystdfu', 'btystdm2u', 'btystdml', 'btystdmu']]
    Y = df['courseevaluation']
    X = sm.add_constant(X)  # adding a constant
    model = sm.OLS(Y, X).fit()
    predictions = model.predict(X)
    print(model.summary())
    const = 4.0133
    btystdave_coef = -1.624e+04
    btystdf2u_coef = 2707.3177
    btystdfl_coef = 2707.2808
    btystdfu_coef = 2707.3709
    btystdm2u_coef = 2707.3324
    btystdml_coef = 2707.2220
    btystdmu_coef = 2707.3721
    sns.residplot(df['btystdave'], df['courseevaluation'], lowess=True)
    plt.show()
    sns.residplot(df['btystdf2u'], df['courseevaluation'], lowess=True)
    plt.show()
    sns.residplot(df['btystdfl'], df['courseevaluation'], lowess=True)
    plt.show()
    sns.residplot(df['btystdfu'], df['courseevaluation'], lowess=True)
    plt.show()
    sns.residplot(df['btystdm2u'], df['courseevaluation'], lowess=True)
    plt.show()
    sns.residplot(df['btystdml'], df['courseevaluation'], lowess=True)
    plt.show()
    sns.residplot(df['btystdmu'], df['courseevaluation'], lowess=True)
    plt.show()