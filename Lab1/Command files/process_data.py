import pandas as pd

def processData ():
    df = pd.read_csv ('../Original data/weather.csv')
    #print (df)
    df = pd.melt (df, id_vars = ['id', 'year', 'month', 'element'], value_vars = list (df.columns)[4:], var_name = 'date', value_name = 'value')
    #print (df)
    df ['date'] = df ['date'].str[1:].astype ('int')
    df ['date'] = df [['year', 'month', 'date']].apply (lambda row: '{:4d}-{:02d}-{:02d}'.format (*row), axis = 1)
    #print (df)
    df = df.loc [df['value'] != '---', ['id', 'date', 'element', 'value']]
    df = df.set_index (['id', 'date', 'element'])
    df = df.unstack ()
    df.columns = list (df.columns.get_level_values ('element'))
    df = df.reset_index ()
    #print (df)
    df.to_csv ('../Analysis data/weather_tidy.csv', index = False)

if __name__ == "__main__":
    processData()