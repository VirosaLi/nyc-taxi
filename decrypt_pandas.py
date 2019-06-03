import json
import pandas as pd


def decrypt_md5(hashed, table):
    if hashed not in table:
        return hashed
    else:
        return table[hashed]


def main():
    # read md5 lookup table from txt file
    with open('medallion_table.txt', 'r') as medallion, open('licence_table.txt', 'r') as licence:
        medallion_table = json.load(medallion)
        licence_table = json.load(licence)
    # read taxi data from file using pandas
    df = pd.read_csv("trip_data_1.csv")

    # decrypt medallion and hack_license
    df['medallion'] = df['medallion'].map(lambda x: decrypt_md5(x, medallion_table))
    df['hack_license'] = df['hack_license'].map(lambda x: decrypt_md5(x, licence_table))

    # print out the first 10 rows
    print(df.head(10))

    # save the result
    df.to_csv('trip_data_1_decrypt.csv')


if __name__ == '__main__':
    main()
