import pandas as pd

df_original = pd.read_csv("trip_data_1.csv")

df_decrypt = pd.read_csv("trip_data_1_decrypt.csv")

print(df_original.info())

print(df_decrypt.info())
