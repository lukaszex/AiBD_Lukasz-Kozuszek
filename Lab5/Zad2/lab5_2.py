# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:00:23 2019

@author: student188
"""

import pandas as pd
from matplotlib import pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv('earthquake.csv')
    print(df.describe(include = 'all'))
    for i in range(len(df['In general, how worried are you about earthquakes?'])):
        if df.iat[i, 0] == "Not at all worried":
            df.iat[i, 0] = 0
        elif df.iat[i, 0] == "Not so worried":
            df.iat[i, 0] = 0
        elif df.iat[i, 0] == "Somewhat worried":
            df.iat[i, 0] = 1
        elif df.iat[i, 0] == "Extremely worried":
            df.iat[i, 0] = 1
        else:
            df.iat[i, 0] = 1
    regions = pd.crosstab(df['US Region'], df['In general, how worried are you about earthquakes?'])
    #df.boxplot(column = 'In general, how worried are you about earthquakes?')
    #plt.show()
    regions.plot.bar()
    plt.show()
    genders = pd.crosstab(df['What is your gender?'], df['In general, how worried are you about earthquakes?'])
    genders.plot.bar()
    plt.show()
    for i in range(len(df)):
        if df.iat[i, 3] == 'Yes, one or more major ones' or df.iat[i, 3] == 'Yes, one or more minor ones':
            df.iat[i, 3] = 'Yes'
    earnings = pd.crosstab(df['How much total combined money did all members of your HOUSEHOLD earn last year?'], df['Have you ever experienced an earthquake?'])
    earnings.plot.bar()
    plt.show()