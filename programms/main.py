import pandas as pd
import os

df = pd.read_csv("C:/Users/Barsik/Desktop/AARI/LEAC/diploma/db_data/baranova/log_11_2022,cpb/221101.csv",
                 skiprows=[0, 2, 3], header=0)

print(df.head())

files_lst = (os.listdir('C:/Users/Barsik/Desktop/AARI/LEAC/diploma/db_data/baranova/log_11_2022,cpb'))

print(files_lst)


