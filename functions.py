import pandas as pd

def remove_outliers(df, column):
    print('Column: ', column)
    print(pd.cut(df[column], bins=3).value_counts())
    print('\n')
    
    Q1 = df[column].quantile(.25)
    Q3 = df[column].quantile(.75)

    #Interquatile range
    IQR = Q3 - Q1

    inferior_threshold = Q1 - 1.5 * IQR
    superior_threshold = Q3 + 1.5 * IQR

    print('Column: ', column)
    print('IIQ: ', IQR, '\nQ1: ', Q1, '\nQ3: ', Q3)
    print('Inferior threshold: ', inferior_threshold, '\nSuperior threshold: ', superior_threshold)
    
    df = df[(df[column] >= inferior_threshold) & (df[column] <= superior_threshold)]
    return df