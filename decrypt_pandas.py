import json
import pandas as pd


def decrypt_medallion(m):
    """
    decrypt medallion using a lookup table
    :param m: the encrypt medallion
    :return: the decrypt medallion if it's in the table, the original encrypt medallion if not
    """
    if m not in medallion_table:
        # print('miss medallion: ', m)
        return m
    else:
        return medallion_table[m]


def decrypt_licence(m):
    """
    decrypt licence using a lookup table
    :param m: the encrypt licence
    :return: the decrypt licence if it's in the table, the original encrypt licence if not
    """
    if m not in licence_table:
        # print('miss licence: ', m)
        return m
    else:
        return licence_table[m]


# read md5 lookup table from txt file
with open('medallion_table.txt', 'r') as medallion, open('licence_table.txt', 'r') as licence:
    medallion_table = json.load(medallion)
    licence_table = json.load(licence)


def main():
    # read taxi data from file using pandas
    df = pd.read_csv("trip_data_1.csv")

    # decrypt medallion and hack_license
    df['medallion'] = df['medallion'].map(lambda x: decrypt_medallion(x))
    df['hack_license'] = df['hack_license'].map(lambda x: decrypt_licence(x))

    # print out the first 10 rows
    print(df.head(10))

    # save the result
    df.to_csv('trip_data_1_decrypt.csv')


if __name__ == '__main__':
    main()
