from os import path, scandir, mkdir
import json
import pandas as pd
from create_hashes import build_medallion_table, build_licence_table
from decrypt_pandas import decrypt_md5

medallion_table_path = path.join('tables', 'medallion_table.txt')
license_table_path = path.join('tables', 'license_table.txt')

# check if lookup tables have been created
if path.exists(medallion_table_path) and path.exists(license_table_path):
    print('Decryption tables found, loading...\n')

    # load md5 lookup table from txt file
    with open(medallion_table_path, 'r') as medallion, open(license_table_path, 'r') as licence:
        medallion_table = json.load(medallion)
        license_table = json.load(licence)
else:
    print('Decryption tables do not exist, creating...\n')

    # create folder for tables
    if not path.exists('tables'):
        mkdir('tables')

    # create and save medallion table
    medallion_table = build_medallion_table()
    with open(medallion_table_path, 'w') as output:
        json.dump(medallion_table, output)

    # create and save medallion license
    license_table = build_licence_table()
    with open(license_table_path, 'w') as output:
        json.dump(license_table, output)


# create folder for result
if not path.exists('results'):
    mkdir('results')

print('Start decrypting dataset...\n')

# iterate through data folder
with scandir('data') as it:
    for entry in it:
        # load dataset
        dataset_path = path.join('data', entry.name)
        df = pd.read_csv(dataset_path)

        # decrypt medallion and hack_license
        df['medallion'] = df['medallion'].map(lambda x: decrypt_md5(x, medallion_table))
        df['hack_license'] = df['hack_license'].map(lambda x: decrypt_md5(x, license_table))

        # print(df.head(10))

        # save result to file
        result_path = path.join('results', 'decrypted_' + entry.name)
        df.to_csv(result_path)

        print(f'dataset {path.basename(dataset_path)} decrypted.')
