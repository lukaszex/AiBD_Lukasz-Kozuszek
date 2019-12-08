import pandas as pd
from matplotlib import pyplot as plt

if __name__ == "__main__":
    df = pd.read_csv('weather_tidy.csv')
    df = df.dropna()
    print(df.head())
    print(df.info())
    print(df.describe())
    df.boxplot()
    plt.show()