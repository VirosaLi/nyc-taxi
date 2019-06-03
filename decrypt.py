from os import path, scandir, mkdir
import json
import pandas as pd
from create_hashes import build_medallion_table, build_licence_table
from decrypt_pandas import decrypt_medallion, decrypt_licence

# check if lookup tables have been created
if path.exists('medallion_table.txt') and path.exists('licence_table.txt'):
    print('decryption tables found, loading...\n')

    # load md5 lookup table from txt file
    with open('medallion_table.txt', 'r') as medallion, open('licence_table.txt', 'r') as licence:
        medallion_table = json.load(medallion)
        licence_table = json.load(licence)
else:
    print('decryption tables do not exist, creating...\n')

    medallion_table = build_medallion_table()
    with open('medallion_table.txt', 'w') as output:
        json.dump(medallion_table, output)

    licence_table = build_licence_table()
    with open('licence_table.txt', 'w') as output:
        json.dump(licence_table, output)

# create folder for result
if not path.exists('result'):
    mkdir('result')

# iterate through data folder
with scandir('data') as it:
    for entry in it:
        # load dataset
        dataset_path = path.join('data', entry.name)
        df = pd.read_csv(dataset_path)

        # decrypt medallion and hack_license
        df['medallion'] = df['medallion'].map(lambda x: decrypt_medallion(x))
        df['hack_license'] = df['hack_license'].map(lambda x: decrypt_licence(x))

        # save result to file
        result_path = path.join('result', 'decrypted_' + entry.name)
        df.to_csv(result_path)

        print(f'dataset {path.basename(dataset_path)} decrypted.')
