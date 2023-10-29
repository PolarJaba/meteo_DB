import pandas as pd
import os

# Reading baranova files
# df = pd.read_csv("C:/Projects/AARI/LEAC/diploma/stations_data/baranova/log_11_2022,cpb/221101.csv",
#                  skiprows=[0, 2, 3], header=0)
# print(df.head())
#
# files_lst = (os.listdir('C:/Projects/AARI/LEAC/diploma/stations_data/baranova/log_11_2022,cpb'))
# print(files_lst)
#
# Reading Barentsburg files
# df_barburg = pd.read_csv("C:/Projects/AARI/LEAC/diploma/stations_data/barentsburg/TOA5_12816.Daily_2022_0509_1209.dat",
#                          sep="/s+", skiprows=[0, 2, 3], index_col=None, header=0)
# print(df_barburg.head(10))

# Rename all lsp files
# dir = 'C:/Projects/AARI/LEAC/diploma/stations_data/lsp/hours'
# lsp_files_lst = os.listdir(dir)
# for file in lsp_files_lst:
#     old_file = os.path.join(dir, file)
#     new_file = os.path.join(dir, file.replace(" ", "-"))
#     os.rename(old_file, new_file)

# Reading lsp files
# df_lsp = pd.read_csv("C:/Projects/AARI/LEAC/diploma/stations_data/lsp/hours/NP-41-Enc#3_Public2023-08-01_1h.csv",
#                      skiprows=[0, 2, 3], header=0)
# print(df_lsp.head(10))

# file is reading, flow loading id possible
dir = 'C:/Projects/AARI/LEAC/diploma/stations_data/tiksy/fluxT'
tiksy_files_lst = os.listdir(dir)

df_tiksy = pd.read_csv(f"{dir}/{tiksy_files_lst[0]}", skiprows=[0, 2, 3], index_col=None, header=0)

# Datasets in files are different -> don't work
# for file in tiksy_files_lst[1:]:
#     new_data = pd.read_csv(f"{dir}/{file}", skiprows=[0, 2, 3], index_col=None, header=0)
#     df_tiksy.loc[len(df_tiksy)] = new_data

print(df_tiksy.head(10))


